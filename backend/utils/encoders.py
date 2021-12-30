from json.encoder import JSONEncoder


class PoMEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj)
        return JSONEncoder.default(self, obj)
