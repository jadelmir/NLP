import xml.etree.ElementTree as ET
import re
from collections import defaultdict
import json


def getDict():
    with open('sentimentDict.json', 'r') as myfile:
        data = myfile.read()
    return json.loads(data)


reversevideo = "".join([chr(27), '[', '7', 'm'])
normalvideo = "".join([chr(27), '[', '0', 'm'])
positivideo = "".join([chr(27), '[', '42', 'm'])
negativideo = "".join([chr(27), '[', '41', 'm'])
wordpat = re.compile(r"[A-Za-z]+[A-Za-z'][A-Za-z]+", re.IGNORECASE)
sentdict = getDict()


def process(s):

    tmpdict = defaultdict(lambda: 0)
    xylist = []
    nwords = 0
    for w in wordpat.finditer(s):
        x, y = w.span()
        key = s[x:y].lower()
        if key in sentdict:
            pos, neg, l = sentdict[key]
            xylist.append((x, y, pos >= neg))
            tmpdict[key] += 1
            nwords += 1
    score = 1.0
    slist = []
    for k in tmpdict:
        factors = sentdict[k]
        f = int(factors[0]) / int(factors[1])
        score *= f
        slist.append((k, f))
    return score, xylist, slist


def prepare(s, xylist):

    xylist.reverse()           # (x, y, True/False)
    for x, y, p in xylist:
        s1 = s[:x]             # the review portion that comes before this word
        s2 = s[x:y]            # the word
        s3 = s[y:]             # the portion after the word
        if p:
            s = s1 + positivideo + s2 + normalvideo + s3
        else:
            s = s1 + negativideo + s2 + normalvideo + s3
    return s


def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text


def ParseFile(filepath):
    wordcount = []
    doctree = ET.parse(filepath)
    root = doctree.getroot()
    for child in root:
        for item in child:
            if item.tag == "review_text":
                t = remove_special_characters(item.text)
                t = t.strip()
                # t = SpellSentence(t)
                score, xy, slist = process(t)
                highlight = prepare(t, xy)
                wordcount .append(t)
    return wordcount
