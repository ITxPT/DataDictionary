import os
import json
import argparse

header = """# ITxPT Data Dictionary Concepts #

This is the ITxPT Data Dictionary Concepts with Concept Definitions, incorporating the Transmodel Definitions. ...

"""

def order_concept_dict(cncpt):
    d = dict()
    # Make sure some know items are first in a specific order
    for k in ['concept', 'source', 'definition']:
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
                if 'concept' not in cncpt:
                    print(f"In {fn}, found concept-less item: {cncpt}")
                    cncpt['concept'] = f"_-{fn}-No-Concept-{e}"
                if cncpt['concept'] in concept_key_list:
                    print(f"When processing {fn}, it seems Concept {cncpt['concept']} already present!")
                concept_key_list.append(cncpt['concept'])
                merged_concept_list.append(order_concept_dict(cncpt))
    merged_concept_list.sort(key=lambda x: x.get('concept'))
    return merged_concept_list

def concept_list_to_markdown(concept_list, header):
    str_list = []
    for cncpt in concept_list:
        s = f"## {cncpt['concept']} ##\n\n"
        for k, v in cncpt.items():
            if k == 'concept':
                continue
            s += f"**{k.capitalize()}:** {v}\n\n"
        str_list.append(s)
    #previously str_list was sorted here, but should already be in order now!(?)
    return header + "".join(str_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--print", help="print of markdown only",
                        action="store_true")
    parser.add_argument("--input-files", help="JSON files with data", required=True, nargs="+")
    parser.add_argument("--output-file", help="Filename of Markdown save file", 
                        default="ConceptDefinitions.md")
    args = parser.parse_args()    

    concept_list = combine_input(args.input_files)
    md = concept_list_to_markdown(concept_list, header)

    if args.print:
        print(md)
    else:
        with open(args.output_file, 'w') as f:
            f.write(md)
            print(f"Wrote markdown to {args.output_file}")

