json:
	./mkjson.py | python3 -m json.tool > openingclassification.json

test:
	@openingclassification/__init__.py 'rnbqkbnr/ppp2ppp/8/3pp3/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -'
