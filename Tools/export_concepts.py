#!/usr/bin/env python

""" Based on Concepts Markdown or JSON, outputs all or a selection of Concepts in different formats. 

See --help for usage/options. 

Adding new formats should be easy.  

Note that it can currently only be used on the command line, but 
changing it to a script that can be called from other scripts should be easy.
"""

import argparse
import json

import parse_itxpt_concept_md as md_parser
import create_markdown

def filter(concepts_to_filter_for, concept_list):
    new_list = [x for x in concept_list if x['name'] in concepts_to_filter_for]
    # Add "UNKNOWN" for concepts that where not found
    found = {x['name'] for x in new_list}
    print(found)
    not_found = set(concepts_to_filter_for) - found
    print(not_found)
    for nf in not_found:
        new_list.append({'name': nf, 'source': 'Not found in source', 'definition': 'Not found in source'})    
    return new_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", help="Markdown file to parse, or json file to read",
                        default="../Concepts/Concepts.md")
    parser.add_argument("--output-file", help="Filename of where to save save file",
                        default=None)
    parser.add_argument("--filter", help='Concept Names to filter for. Can include one or more .json files on format {"usedConcepts": [<concept>,...]}" ', required=True, nargs="+")
    parser.add_argument("--format", help="""'MDcond' - Markdown, condensed
                                            'MD' - as Concept.md
                                            'TXTcond - plain text, condensed""",
                        default="MDcond")
    args = parser.parse_args()

    concepts_filter_set = set()
    for c in args.filter:
        if c.endswith(".json"):
            with open(c) as f:
                d = json.load(f)
                concepts_filter_set.update(d["usedConcepts"])
        else:
            concepts_filter_set.add(c)

    if args.input_file.endswith(".md"):
        concept_list, error_list = md_parser.parse_markdown_file(args.input_file)
    elif args.input_file.endswith(".json"):
        concept_list = create_markdown.combine_input([args.input_file,])

    filtered_list = filter(concepts_filter_set, concept_list)

    if args.format == 'MDcond':
        output = "\n\n".join([f"**{c['name']}** - {c['definition']}" for c in filtered_list])
    elif args.format == 'TXTcond':
        output = "\n".join([f"{c['name']} - {c['definition']}" for c in filtered_list])
    elif args.format == 'MD':
        output = create_markdown.concept_list_to_markdown(filtered_list, "")
    if args.output_file:
        with open(args.output_file, 'w') as of:
            of.write(output)
    else:
        print(output)

print(f"len(filters)={len(concepts_filter_set)}; len(extracted-concepts)={len(filtered_list)}. Should normally match!")
