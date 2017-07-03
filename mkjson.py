#!/usr/bin/env python3

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
    logging.debug(openingclassification.NIC_DATA)
    for k, v in openingclassification.NIC_DATA.items():
        print(k, v)

if __name__ == '__main__':
    main()
