#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A quick, dumb script to format HTML bolding of my name in publication lists.

Created on Sat Nov 28 17:11:27 2020

@author: earnestt1234
"""

# names here are regex replaced
names = ['Earnest, T.',
         'Earnest, T. W.']

# replaces longest names first
names = sorted(names, reverse=True)

regex = "(" + '|'.join(names) + ")"

import argparse
import os
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename
    with open(filename) as file:
        data = file.read()

    count = data.count('csl-entry')
    data, n = re.subn(regex, r'<b>\1</b>', data)

    base, ext = os.path.splitext(filename)
    new_name = base + '_bolded' + ext
    with open(new_name, 'w') as dest:
        dest.write(data)

    # reporting
    print('',
          f'Output written to {new_name}',
          f'Counted entries: {count}',
          f'Counted replacments: {n}',
          '', sep='\n')

if __name__ == '__main__':
    main()