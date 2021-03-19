#! python3
# whitespace-rem.py - Remove white spaces from provided text.

import re

def remove(string):
    pattern = re.compile(r'\s+') # \s matches spaces, tabs, and linebreaks | + matches one or more of \s
    return re.sub(pattern, '', string)

text  = input('Enter or paste text to remove whitespaces: ')
print(remove(text))