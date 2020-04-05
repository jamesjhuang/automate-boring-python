#!/usr/bin/env python3

# mclip.py - A multi-clipboard program
# This program lets you save multiple things to a clipboard.

import sys
import os
import pyperclip
import pickle

if os.path.exists('clipboard.pickle'):
    with open('clipboard.pickle', 'rb') as f:
        clipboard = pickle.load(f)
else:
    clipboard = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [key] [value]')
    sys.exit()

keyphrase = sys.argv[1]
if len(sys.argv) > 2:
    phrase = sys.argv[2]
    clipboard[keyphrase] = phrase
    with open('clipboard.pickle', 'wb') as f:
        pickle.dump(clipboard, f)

if keyphrase in clipboard:
    pyperclip.copy(clipboard[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyphrase)

