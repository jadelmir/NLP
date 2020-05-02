#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET
import re
from collections import defaultdict
from fileParsing import ParseFile
from Contractions import handleContractions
from checkSpell import SpellText
from process import ProcessArr
if __name__ == "__main__":
    wordcount = []

    if len(sys.argv) < 2:
        print("1 arg file needed")
        sys.exit(1)
    filepath = sys.argv[1]
    parsedFile = ParseFile(filepath)
    newText = handleContractions(parsedFile)
    count = 0
    for i in newText:
        x = i.split()
        count += len(x)
    print(count)
    x = SpellText(newText)
    # t = ProcessArr(x)
    # print(t)



