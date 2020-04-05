#!/usr/bin/env python3

# bulletPointAdder.py - A program to add bullets to multiple lines of text


import sys
import pyperclip

text = pyperclip.paste()
text = text.splitlines()
altered = []
for line in text:
    line = '* ' + line
    altered.append(line)
text = '\n'.join(altered)
pyperclip.copy(text)
