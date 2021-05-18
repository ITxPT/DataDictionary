import os
import sys
import json

# This script parses the Transmodel Data Defintions which can be found at 
# http://www.transmodel-cen.eu/wp-content/uploads/sites/2/2015/01/TRM6_DataDefinitions.pdf
# It has been tweaked to this particular document; andy changes my require adjustments.
trpdf = "TRM6_DataDefinitions.pdf"

import pdfplumber
pdf = pdfplumber.open(trpdf)

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
        if k == 'View':
            k = 'VIEW'
        key = k.replace('\n', '')
        if key == "":
            tm_dict[prev_key] = tm_dict[prev_key] + ' ' + definition
        else:
            if key in tm_dict:
                print(f"Key {key} already in dict!")
            tm_dict[key] = definition
            tm_list.append({'concept': key, 'source': 'Transmodel', 'definition': definition})
            prev_key = key

trdd_json = "transmodel6.json"

with open(trdd_json, 'w') as outfile:
    json.dump({'source_file': trpdf, 'concepts': tm_list}, outfile, indent=4)
