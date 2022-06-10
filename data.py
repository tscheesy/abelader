import json


# JSON-functions save & load as basically provided by fabod, modified & commented by tscheesy
def new_dict(file, top_key):
    try:
        with open(file) as open_file:
            content = json.load(open_file)
    except FileNotFoundError:
        content = {}

    # open new dict with top level Key (internal video id)
    content[str(top_key)] = {}

    with open(file, "w") as open_file:
        json.dump(content, open_file)


def save(file, top_key, second_key, value):
    try:
        with open(file, "r") as open_file:
            content = json.load(open_file)
    except FileNotFoundError:
        content = {}

    # save new contents to dict: open new dict with video ID-key,
    content[top_key][str(second_key)] = value

    with open(file, "w") as open_file:
        json.dump(content, open_file, indent=10)


def load(file, key):
    try:
        with open(file, "r") as open_file:
            content = json.load(open_file)
            value = content.get(key)
    except FileNotFoundError:
        value = "Value Not Found"
    return value


def counter_up(file, key):
    try:
        with open(file, "w") as open_file:
            content = json.load(open_file)
    except FileNotFoundError:
        content = {}

    # raise counter at specified key by one
    content[str(key)] += 1

    with open(file, "w") as open_file:
        json.dump(content, open_file)


# def search_for_entry
