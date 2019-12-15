#!/usr/bin/env python3
"""
MKSJON

mkjson creates chess opening classification JSON file from the Python library.
"""

import collections
import json
import logging
import sys

import openingclassification

logging.basicConfig(level=logging.DEBUG)


def main():
    items = dict()
    for k, v in openingclassification.NIC_DATA.items():
        item = dict()
        item['epd'] = k
        item['nic'] = v
        items[k] = item
    for k, v in openingclassification.ECO_DATA.items():
        if k in items:
            items[k]['eco'] = v
        else:
            item = dict()
            item['epd'] = k
            item['eco'] = v
            items[k] = item
    for k, v in openingclassification.LONG_NAME_DATA.items():
        if k in items:
            items[k]['name'] = v
        else:
            item = dict()
            item['epd'] = k
            item['name'] = v
            items[k] = item

    fenlist = list()
    for k, v in items.items():
        fenlist.append(v)

    json.dump(items, sys.stdout)


if __name__ == '__main__':
    main()
