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


def load_dict(file):
    try:
        with open(file, "r") as open_file:
            content = json.load(open_file)
    except FileNotFoundError:
        content = "Dict Not Found"
    return content


def load_value(file, key):
    try:
        with open(file, "r") as open_file:
            content = json.load(open_file)
            value = content.get(key)
    except FileNotFoundError:
        value = "Value Not Found"
    return value


def counter_up(file, top_key, key):
    try:
        with open(file, "r") as open_file:
            content = json.load(open_file)
    except FileNotFoundError:
        content = {}

    # raise counter at specified key by one
    content[top_key][str(key)] += 1

    with open(file, "w") as open_file:
        json.dump(content, open_file, indent=5)


""" 

unsolved problem with GET-Method on questions html, hence below code is not used and input data only stored in counter_data json
EDIT: After calling & sorting Data, decision was made to not use a list but dict for purpose counters too --> so counter_up works fine

def purpose_counter(video_id, purpose):

    # purpose_counter raises the purpose counts in both video_data and counter_data json
    # first counter_data:
    try:
        with open("counter_data.json", "r") as open_file:
            content = json.load(open_file)
    except FileNotFoundError:
        content = {}

    # raise counter at right purpose-list-index in counter_data
    if purpose == "repost":
        content["purpose"][0] += 1

    elif purpose == "fun":
        content["purpose"][1] += 1

    elif purpose == "creator":
        content["purpose"][2] += 1

    else:
        return "Invalid download purpose stated"

    with open("counter_data.json", "w") as open_file:
        json.dump(content, open_file, indent=5)

    # second video_data:
    try:
        with open("video_data.json", "r") as open_file:
            content = json.load(open_file)
    except FileNotFoundError:
        content = {}

    # raise counter at right purpose-list-index in video_data
    if purpose == "repost":
        content[video_id]["purpose"][0] += 1

    elif purpose == "fun":
        content[video_id]["purpose"][1] += 1

    elif purpose == "creator":
        content[video_id]["purpose"][2] += 1

    else:
        return "Invalid download purpose stated"

    with open("video_data.json", "w") as open_file:
        json.dump(content, open_file, indent=10)
        
"""
