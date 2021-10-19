import json


def get_str(name: str):
    """
    Gets a string from the translation file.
    :param name:
    :return:
    """
    translation = open("translation.json", "r")
    content = json.loads(translation.read())
    translation.close()
    return content[name]
