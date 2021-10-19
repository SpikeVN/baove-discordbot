import json


def read(entry: str):
    """
    Reads the current value in config file.

    :param entry: The name of the entry. Must be a string.
    :return: The value of the entry
    """
    config = open("config.json", "r")
    content = json.loads(config.read())
    config.close()
    return content[entry]


def write(entry: str, value):
    """
    Writes an entry to the config file.

    :param entry: The name of the entry
    :param value: The value to write to it.
    """
    old_config = open("config.json", "r")
    content = json.loads(old_config.read())
    content[entry] = value
    old_config.close()
    config = open("config.json", "w")
    config.write(json.dumps(content))
    config.close()
