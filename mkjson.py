#!/usr/bin/env python3

import json
import logging

import openingclassification

logging.basicConfig(level=logging.DEBUG)

class ClassificationItem(object):
    eco = ''
    nic = ''
    name = ''
    fen = ''
    moves = ''

def main():
    items = dict()
    for k, v in openingclassification.NIC_DATA.items():
        item = ClassificationItem()
        item.fen = k
        item.nic = v
        items[k] = item
    for k, v in openingclassification.ECO_DATA.items():
        if k in items:
            items[k].eco = v
        else:
            item = ClassificationItem()
            item.fen = k
            item.eco = v
            items[k] = item
    for k, v in openingclassification.LONG_NAME_DATA.items():
        if k in items:
            items[k].name
        else:
            item = ClassificationItem()
            item.fen = k
            item.name = v
            items[k] = item

    # this does not work, see https://stackoverflow.com/questions/10252010/serializing-python-object-instance-to-json
    # json.dumps(items)

if __name__ == '__main__':
    main()
