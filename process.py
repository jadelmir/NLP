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
        if f < 1 :
            f *= -3
        score += f
        slist.append((k, f))
    return score, xylist, slist


def ProcessArr(arr):
    a = [] 
    for i in arr :
        score, xylist, slist = process(i)
        a.append(score)
        break
    return a
