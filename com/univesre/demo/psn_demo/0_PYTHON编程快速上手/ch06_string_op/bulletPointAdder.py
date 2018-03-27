#! /usr/bin/env python3
# p108: second in-chapter project: unordered list, @20170111;
# bulletPointAdder.py - adds Wikipedia bullet points to the
# start of each line of text on clipboard;

import pyperclip
text = pyperclip.paste()

# TODO: Sepatate lines and add stars
# Separate lines and add stars;
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list;
    lines[i] = '* ' + lines[i]  # add star;
text = '\n'.join(lines)         # join new lines back to text;

pyperclip.copy(text)            # copy back to system;
