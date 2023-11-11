import re

def split_on_empty_lines(s):
    blank_line_regex = r"(?:\r?\n){2,}"
    return re.split(blank_line_regex, s.strip())


def get_list_of_lists(file):
    pairs = split_on_empty_lines(open(file).read())

    pairs = [pair.split() for pair in pairs]

    pairs2 = pairs.copy()
    pairs = []

    for pair in pairs2:
        pair2 = pair.copy()
        pair = []
        for item in pair2:
            strs = item.replace('[','').split('],')
            lists = [map(str, s.replace(']','').split(',')) for s in strs]
            item = []
            for l in lists:
                new_list = list(l)
                item.append(new_list)
            pair.append(item)
        pairs.append(pair)
    return pairs

