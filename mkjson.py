#!/usr/bin/env python3

import collections
import json
import logging
import sys

import openingclassification

logging.basicConfig(level=logging.DEBUG)


# class ClassificationItem(json.JSONEncoder):
class ClassificationItem(dict):
    eco = ''
    nic = ''
    name = ''
    fen = ''
    moves = ''

    def __init__(self, fen=fen, eco=eco, name=name, nic=nic):
        self.fen = fen
        self.eco = eco
        self.name = name
        self.nic = nic

    # def default(self, o):
    #     logging.debug("default o={0}".format(o))
    #     return json.JSONEncoder.default(self, o)

    # def encode(self, o):
    #     logging.debug("encode o={0]".format(o))

    # def iterencode(self, o):
    #     logging.debug("iterencode o={0]".format(o))


def main():
    #items = collections.OrderedDict()
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
    # http://www.marcstober.com/blog/2007/07/07/serializing-arbitrary-python-objects-to-json-using-__dict__/
    # json.dumps(items)
    # This works, but does not preserve the order of the properties
    # print(json.dumps([item.__dict__ for item in items.values()]))
    # print(json.dumps(items))
    # https://stackoverflow.com/questions/36880065/how-to-serialize-python-dict-to-json
    fen = 'rnbqkbnr/ppp2ppp/8/3pp3/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -'
    logging.debug("FEN=%s NIC=%s" % (fen, items[fen].nic))
    print(json.dump(
        # items[fen].__dict__
        items, sys.stdout
    ))


if __name__ == '__main__':
    main()
