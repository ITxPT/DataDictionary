import argparse
import json
import parse_definitions as md_parser
import create_markdown 


def filter(concepts_to_filter_for, concept_list):
    new_list = [x for x in concept_list if x['name'] in concepts_to_filter_for]
    return new_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", help="Markdown file to parse",
                        default="../Concepts/Concepts.md")
    parser.add_argument("--output-file", help="Filename of where to save save file", 
                        default=None)
    parser.add_argument("--filter", help="Concept Names to filter for", required=True, nargs="+")                        
    
    parser.add_argument("--format", help="""'MDcond' - Markdown, condensed
                                            'MD' - as Concept.md
                                            'TXTcond - plain text, condensed""",
                        default="MDcond")                        
    args = parser.parse_args()    

    if args.input_file.endswith(".md"):
        concept_list, error_list = md_parser.parse_markdown_file(args.input_file)
    elif args.input_file.endswith(".json"):
        concept_list = create_markdown.combine_input([args.input_file,])

    filtered_list = filter(args.filter, concept_list)

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
