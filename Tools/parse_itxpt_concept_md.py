#!/usr/bin/env python

""" Creates JSON Concepts file(s) based on ITxPT Concepts Markdown.

Together with create_markdown.py this can be used to go MD -> JSON (-> processing) -> MD.
All **bold:** sections are preserved. 
"""

import json
import argparse
from collections import defaultdict
import os.path

def parse_markdown_file(sourcefile):
    first_concept_found = False

    concept_dict = None
    concept_list = list()

    error_list = []

    lines = open(sourcefile).readlines()

    i = 0
    while i < len(lines):
        if not first_concept_found and not lines[i].startswith("##"):
            # skip all text about the first concept
            i += 1
            continue
        first_concept_found = True
        if lines[i].startswith("##"):
            # Found the first/next concept
            # Stored previous concept, create empty dict for next
            concept_dict = {}
            concept_dict['name'] = lines[i].strip("# \n")
            concept_list.append(concept_dict)
            i += 1
            continue

        if lines[i].startswith("**"):
        # if line starts with **, that is a "key"
            _, p1, p2 = lines[i].split("**", maxsplit=2)
            key = p1.strip("* :")
            text = p2.strip(" ")
            i += 1
            while i < len(lines) and not lines[i].startswith("**") and not lines[i].startswith("##"):
                text += lines[i].strip(" ")
                i += 1
            concept_dict[key.lower()] = text.strip("\n ")
            continue
        if lines[i].strip() == "":
            i += 1
            continue
        print(f"Hmmmm {i}, {lines[i]}")
        break

    return concept_list, error_list

def print_error_list(error_list):
    if error_list:
        print("Errors encountered during parsing:")
        for e in error_list:
            print(e)

def print_parsed(sourcefile):
    concept_list, error_list = parse_markdown_file(sourcefile)    
    for cncpt in concept_list:
        keys = cncpt.keys()
        if 'name' in keys:
            keys.remove('name')
            print(f"## {cncpt['name']} ##\n\n")
        else:
            print(f"## NO CONCEPT! ##\n\n")
        for k in keys:
            print(f"**{k.capitalize()}:** {cncpt[k]}\n\n")
    print_error_list(error_list)


def save_as_json(sourcefile, outputfile):
    concept_list, error_list = parse_markdown_file(sourcefile)
    with open(outputfile, 'w') as outfile:
        json.dump({'source_file': sourcefile, 'concepts': concept_list}, outfile, indent=4)
        print(f"Parsed data saved to {outputfile}")
    print_error_list(error_list)

def save_as_json_per_source(sourcefile, outputfile):
    concept_list, error_list = parse_markdown_file(sourcefile)
    dl = defaultdict(list)
    for cncpt in concept_list:
        dl[cncpt['source'].upper()].append(cncpt) 
    folder, fn = os.path.split(outputfile)
    for k, l in dl.items():
        fn_source = os.path.join(folder, f"{k}_{fn}")
        with open(fn_source, 'w') as outfile:
            json.dump({'source_file': sourcefile, 'concepts': l}, outfile, indent=4)
            print(f"For {k} parsed data saved to {fn_source}")
    print_error_list(error_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--print", help="only print parsed content",
                        action="store_true")
    parser.add_argument("--per-source", help="save in separate files for each Source",
                        action="store_true")
    parser.add_argument("--input-file", help="Markdown file to parse", required=True)
    parser.add_argument("--output-file", help="Filename of json save file", 
                        default="ConceptDefinitions.json")
    args = parser.parse_args()    

    if args.print:
        print_parsed(args.input_file)
    else:
        if args.per_source:
            save_as_json_per_source(args.input_file, args.output_file)
        else:
            save_as_json(args.input_file, args.output_file)
