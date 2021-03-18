#!/usr/bin/env python3
"""
MKSJON

mkjson creates chess opening classification JSON file from the Python library.
"""

__author__ = 'Ari Makela'
__copyright__ = 'Copyright 2017-2021'
__credits__ = ['Ari Makela']
__license__ = 'GPL'
__version__ = '0.1.0'
__maintainer__ = 'Ari Makela'
__email__ = 'ari.makela@iki.fi'
__status__ = 'Development'

import json
import logging
import sys

import openingclassification

logging.basicConfig(level=logging.DEBUG)


def main():
    """The main function."""
    items = dict()
    for fen, nic_key in openingclassification.NIC_DATA.items():
        item = dict()
        item['nic'] = nic_key
        items[fen] = item
    for fen, eco_key in openingclassification.ECO_DATA.items():
        if fen in items:
            items[fen]['eco'] = eco_key
        else:
            item = dict()
            item['eco'] = eco_key
            items[fen] = item
    for fen, name in openingclassification.LONG_NAME_DATA.items():
        if fen in items:
            items[fen]['name'] = name
        else:
            item = dict()
            item['name'] = name
            items[fen] = item

    json.dump(items, sys.stdout)


if __name__ == '__main__':
    main()
