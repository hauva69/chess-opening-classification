#!/usr/bin/env python3
"""
MKSJON

mkjson creates chess opening classification JSON file from the Python library.
"""

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
        item['fen'] = fen
        item['nic'] = nic_key
        items[fen] = item
    for fen, eco_key in openingclassification.ECO_DATA.items():
        if fen in items:
            items[fen]['eco_key'] = eco_key
        else:
            item = dict()
            item['fen'] = fen
            item['eco'] = eco_key
            items[fen] = item
    for fen, name in openingclassification.LONG_NAME_DATA.items():
        if fen in items:
            items[fen]['name'] = name
        else:
            item = dict()
            item['fen'] = fen
            item['name'] = name
            items[fen] = item

    json.dump(items, sys.stdout)


if __name__ == '__main__':
    main()
