import os
import json

trdd_json = "transmodel6.json"
with open(trdd_json) as trdd:
    tr_dict = json.load(trdd)

twg3_list = ['TRAIN', 'TRAIN COMPONENT', 'TRAIN ELEMENT', 'TRAIN IN COMPOUND TRAIN', 'VEHICLE', 'VEHICLE MODE', 'VEHICLE TYPE', 'COMPOUND TRAIN', 'BOARDING AND ALIGHTING', 'BOARDING BASED PASSENGER COUNT', 'ONBOARD DEVICE BASED PASSENGER COUNT', 'PASSENGER EQUIPMENT' ]

twg3_list.sort()


dd_extract = dict()

for k, v in tr_dict.items():
    if k in twg3_list:
        dd_extract[k] = v

for k, v in dd_extract.items():
    print(f"### {k} ###")
    print(v)