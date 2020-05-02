#!/usr/bin/env python3

import re
import sys
from random import choice
from collections import defaultdict
from abbreviations import abbr
from nltk.stem import PorterStemmer
import nltk

wordlist = []

sentence_pat = re.compile(r"[.?!][ \n\t]")
word_pat = re.compile(r"[a-z]+[']?[a-z]+", re.IGNORECASE)

ps = PorterStemmer()


def getfile(fname):
    all = ""
    with open(fname, 'r') as fd:
        for line in fd:
            s = line.replace("\n", " ")
            all += s
    return all


def parse_sentence(s):
    global ps

    for w in word_pat.finditer(s):
        x, y = w.span()
        oldkey = s[x:y]
        newkey = ps.stem(oldkey)
        print(oldkey, newkey)


def abfilter(s):
    for k in abbr:
        s = re.sub(k, abbr[k], s)
    return s


if __name__ == "__main__":

    doc = getfile(sys.argv[1])
    doc = abfilter(doc)

    for x in sentence_pat.split(doc):
        parse_sentence(x)
        s = input("? ")
        if len(s) > 0 and s[0] == 'q':
            break
