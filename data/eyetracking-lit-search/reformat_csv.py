#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reformat_csv.py

Script to format csv lit search into JSON objects for D3-process-map springform visualization (https://github.com/nylen/d3-process-map).

Authors:
    – Jon Clucas, 2017 (jon.clucas@childmind.org)
    – Bonhwang Koo, 2017 (bonhwang.koo@childmind.org)
    – James Nylen, 2013–2014+ (jnylen@gmail.com)

© 2017, Child Mind Institute, MIT License

@author: jon.clucas
"""

import json, numpy as np, pandas as pd

with open('compilation.csv', 'r') as f:
    data = pd.read_csv(f)

new_json = {}
new_markdown = {}

for index, row in data.iterrows():
    article = row["Article Citation"].strip().replace("&", "and")
    article = article[0:article.find(')')+1]
    new_json[article] = {"name" : article,
             "type" : "article", "depend" : [row[
             "Eyetracking Hardware"].strip(), row[
             "Disorder"].strip(), row["Analysis Method"], row[
             "Analysis Software"]]}
    new_markdown[article] = {"year" : row["Year"], "hardware": row[
                 "Eyetracking Hardware"].strip(), "Disorder" : row[
                 "Disorder"].strip(), "Task" : row["Task"].strip(),
                 "Method" : row["Analysis Method"], "Software" : row[
                 "Analysis Software"], "Conclusion" : row["Conclusion"].strip(
                 )}
    if row["Eyetracking Hardware"].strip() not in new_json:
        new_json[row["Eyetracking Hardware"].strip()] = {"name" : row[
                 "Eyetracking Hardware"].strip(), "type" : "hardware"}
    for disorders in str(row["Disorder"]).split(';'):
        for disorder in str(disorders).split(','):
            if disorder.strip() not in new_json:
                new_json[disorder.strip()] = {"name" : disorder.strip(),
                         "type" : "disorder"}
    for methods in str(row["Analysis Method"]).split(';'):
        for method in str(methods).split(','):
            if method.strip() not in new_json:
                new_json[method.strip()] = {"name" : method.strip(),
                         "type" : "method"}
    if (type(row["Analysis Software"]) == str and row[
        "Analysis Software"].strip() not in new_json):
        new_json[row["Analysis Software"].strip()] = {"name" : row[
                 "Analysis Software"].strip(), "type" : "software", "depend" :
                  [row["Analysis Method"]]}

new_json_list = []
for key in new_json:
    if "depend" in new_json[key]:
        new_json[key]["depends"] = []
        for depend in new_json[key]["depend"]:
            if(type(depend) == str):
                for new_depends in depend.split(';'):
                    for new_depend in new_depends.split(','):
                        new_json[key]["depends"].append(new_depend.strip())
        else:
            new_json[key]["depend"].remove(depend)
        new_json[key].pop("depend", None)

for na in [np.nan, "nan", "Not applicable", "Not Applicable", "Not Specified"]:
    new_json.pop(na, None)
    for key in new_json:
        if "depends" in new_json[key]:
            while na in new_json[key]["depends"]:
                new_json[key]["depends"].remove(na)

for key in new_json:
    if "depends" not in new_json[key]:
        new_json[key]["depends"] = []
    new_json_list.append(new_json[key])


with open('new_objects.json', 'w') as f:
    json.dump(new_json_list, f)

for key in new_markdown:
    mkstring = ''.join(["### Conclusion\n", new_markdown[key]["Conclusion"]])
    with open(''.join([key.strip(), ".mkdn"]), "w") as f:
        f.write(mkstring)