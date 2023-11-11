from array import array
import re

def split_on_empty_lines(s):
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

pairs = split_on_empty_lines(open('./data.txt').read())

pairs = [pair.split() for pair in pairs]

for pair in pairs:
    for item in pair:
        strs = item.replace('[','').split('],')
        lists = [map(int, s.replace(']','').split(',')) for s in strs]
        for list_ in lists:
            for l in list_:
                print(l)

