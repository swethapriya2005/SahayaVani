class MemoryStore:
    def __init__(self):
        self.data = {}

    def update(self, key, value):
        if key in self.data and self.data[key] != value:
            return "CONTRADICTION"
        self.data[key] = value
        return "OK"

    def get_all(self):
        return self.data
