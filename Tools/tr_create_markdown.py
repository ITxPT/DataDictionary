import os
import json

header = """### ITxPT Data Dictionary Terms and Definitions ###
This is the ITxPT Data Dictionary Terms and Definitions, incorporating the Transmodel Definitions. ..."""

trdd_json = "transmodel6.json"
with open(trdd_json) as trdd:
    tr_dict = json.load(trdd)

str_list = []
for d in tr_dict['concepts']:
    s = f"""## {d['concept']} ## 
    
**Source:** {d['source']}
    
**Definition:** {d['definition']}

"""
#    print(s)
#    print("***")
    str_list.append(s)

str_list.sort()

with open('ITxPTDefinitions.md', 'w') as f:
    for s in str_list:
        f.write(s)
