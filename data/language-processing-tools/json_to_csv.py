#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
json_to_csv.py

Script to create a csv from the DOT from the Dia diagram.

Authors:
	– Jon Clucas, 2017 (jon.clucas@childmind.org)
"""
import csv, json, os

# get `def short_ref(long_citation, year)` and `def ref_exists(ref)` from `../
# eyetracking-lit-search/reformat_csv.py`
def_flag = False
fxns = ['short_ref', 'ref_exists']
for fxn in fxns:
    short = ''
    with open('../eyetracking-lit-search/reformat_csv.py', 'r') as r_s:
        for line in r_s:
            if ''.join(['def ', fxn]) in line:
                def_flag = True
            elif 'def' in line:
                def_flag = False
            if def_flag:
                short += line
            if "return ref" in line:
                def_flag = False
    exec(short)

def main():
    filepath = 'objects.json'
    jd = {}
    with open(filepath, 'r') as jf:
        jd = json.load(jf)
    cd = {}
    for item in jd:
        mkdn = ''
        if os.path.exists(''.join([item['name'], '.mkdn'])):
            with open (''.join([item['name'], '.mkdn']), 'r') as md:
                for line in md:
                    mkdn += line
        item['markdown'] = mkdn
        if item['type'] == 'paper':
            new_name = short_ref(item['name'].strip().replace("&", "and"),
                       item['name'].split('(')[1][:4])
            while new_name in cd:
                new_name = ref_exists(new_name)
            item['name'] = new_name
        cd[item['name']] = item
    with open('objects.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'type', 'depends',
                 'markdown'])
        writer.writeheader()
        for item in cd:
            writer.writerow(cd[item])
            

# ============================================================================
if __name__ == '__main__':
    main()