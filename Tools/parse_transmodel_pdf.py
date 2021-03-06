#!/usr/bin/env python
"""
Parses the Transmodel Data Defintions PDF and output as JSON-file.

The Transmodel Data Dictionary pdf can be found at:
http://www.transmodel-cen.eu/wp-content/uploads/sites/2/2015/01/TRM6_DataDefinitions.pdf

This script has been tweaked to this particular document; any changes/updates of the pdf may 
require adjustments of the "parsing parameters" used.

The output is a json file with all concepts. The json file is input to other scripts/tools.
"""

import os
import sys
import json

import pdfplumber  # pip install pdfplumber

tr_pdf = "TRM6_DataDefinitions.pdf"
tr_json = "Transmodel6_Concepts.json"

pdf = pdfplumber.open(tr_pdf)

tm_dict = dict()
tm_list = list()

prev_key = "Cant start here"
for p in range(63) :
    page = pdf.pages[p]
    if p == 0:
        page = page.within_bbox((0, 260, 590, 840))

    settings = {
        "vertical_strategy": "lines", 
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [],
        "explicit_horizontal_lines": [] if p==0 else [68],
        "snap_tolerance": 3,
        "join_tolerance": 3,
        "edge_min_length": 3,
        "min_words_vertical": 3,
        "min_words_horizontal": 1,
        "keep_blank_chars": False,
        "text_tolerance": 3,
        "text_x_tolerance": None,
        "text_y_tolerance": None,
        "intersection_tolerance": 3,
        "intersection_x_tolerance": None,
        "intersection_y_tolerance": None,
    }

    table = page.extract_table(settings)
    for k, v in table:
        definition = v.replace('\n', '')
        # If a defintion is missing in Transmodel, make a note of that
        if definition == "":
            definition = "_No definition in Transmodel source pdf_"
        # Fix the cases where non-upper case looks really strange 
        if k in ['View',]:
            k = k.upper()
        k = k.replace('\n', '')
        # Fix a few cases where Term gets two spaces internally
        k = k.replace('  ', ' ')
        if k == "":
            tm_dict[prev_key] = tm_dict[prev_key] + ' ' + definition
        else:
            if k in tm_dict:
                print(f"Key {k} already in dict!")
            tm_dict[k] = definition
            tm_list.append({'name': k, 'source': 'Transmodel', 'definition': definition})
            prev_key = k

with open(tr_json, 'w') as outfile:
    json.dump({'source_file': tr_pdf, 'concepts': tm_list}, outfile, indent=4)
print(f"Processing {tr_pdf} wrote {len(tm_list)} concepts to {tr_json}")
