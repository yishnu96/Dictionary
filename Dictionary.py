# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 20:00:14 2019

@author: yishnu
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        ans = input("Did you mean %s ? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if ans=="Y" or "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif ans== "N" or "n":
            return "The word doesn't exist. Please check it!!!"
    else:
            return "The word doesn't exist. Please check it!!!"

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)