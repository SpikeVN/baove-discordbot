import json


class Cache:
    """
    A Cache object that can store everything.
    """

    def __init__(self):
        with open("storage/cache.tmp", "r") as f:
            self.data = json.loads(f.read())

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def flush(self):
        self.data = {}

    def commit(self):
        """
        Permanently saves the cache.
        """
        with open("storage/cache.tmp", "w") as f:
            f.write(str(self.data))
