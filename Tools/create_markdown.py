#!/usr/bin/env python

""" 
Based on the Concepts JSON file(s), creates Markdown output. 
"""

import os
import json
import argparse

itxpt_dd_md_header = """# ITxPT Data Dictionary Concepts #

This is the ITxPT Data Dictionary Concepts with Concept Definitions, incorporating the Transmodel Definitions. ...

"""

def order_concept_dict(cncpt):
    d = dict()
    # Make sure some know items are first in a specific order
    for k in ['name', 'source', 'definition']:
        d[k] = cncpt.pop(k, "")  # pop() removes the item
    # Then put the others in the order they had in source (from python 3.6 dicts are ordered)
    for k, v in cncpt.items():
        d[k] = v
    return d

def combine_input(input_files):
    merged_concept_list = list()
    concept_key_list = list()
    for fn in input_files:
        with open(fn) as f:
            top = json.load(f)
            concept_list = top['concepts']
            for e, cncpt in enumerate(concept_list):
                if 'name' not in cncpt:
                    print(f"In {fn}, found concept-less item: {cncpt}")
                    cncpt['name'] = f"_-{fn}-No-Concept-{e}"
                if cncpt['name'] in concept_key_list:
                    print(f"When processing {fn}, it seems Concept {cncpt['name']} already present!")
                concept_key_list.append(cncpt['name'])
                merged_concept_list.append(order_concept_dict(cncpt))
    merged_concept_list.sort(key=lambda x: x.get('name'))
    return merged_concept_list

def concept_list_to_markdown(concept_list, header):
    str_list = []
    for cncpt in concept_list:
        s = f"## {cncpt['name']} ##\n\n"
        for k, v in cncpt.items():
            if k == 'name':
                continue
            s += f"**{k.capitalize()}:** {v}\n\n"
        str_list.append(s)
    #previously str_list was sorted here, but should already be in order now!(?)
    return header + "".join(str_list)

def create_markdown(input_files, output_file, header, print_only=False):
    concept_list = combine_input(input_files)
    md = concept_list_to_markdown(concept_list, header)

    if print_only:
        print(md)
    else:
        with open(output_file, 'w') as f:
            f.write(md)
            print(f"Wrote markdown to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--print", help="print of markdown only",
                        action="store_true")
    parser.add_argument("--input-files", help="JSON files with data", required=True, nargs="+")
    parser.add_argument("--output-file", help="Filename of Markdown save file", 
                        default="Concepts.md")
    args = parser.parse_args()  

    create_markdown(args.input_files, args.output_file, itxpt_dd_md_header, print_only=args.print)  

