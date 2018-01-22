import json
import sys
from os import remove
from urllib.request import urlretrieve


def usg_msg_err():
    """Return usage reference and error boilerplate."""
    usg = "python.exe pprint_json.py [path][*.json]"
    err = "pprint_json.py: error: "
    return "Usage: " + usg + "\n\n" + err


def load_data(data):
    """Parse a *.json file sent as an argument."""
    f = open(data, encoding="UTF-8")
    res = json.load(f)
    f.close()
    return res


def pretty_print_json(data):
    """Re-format data from a *.json file
    and send the result to a new file and to the console.
    """
    s = json.dumps(load_data(data),
                   ensure_ascii=False, sort_keys=True, indent=4)
    f = open("pretty.json", "w")
    f.write(s)
    f.close()
    try:
        print(s)
    except UnicodeEncodeError:
        print("Cannot print to console")
        print(usg_msg_err() + "data not supported by code page")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:  # handle a command line input
            sys.argv[1] = sys.argv[1].replace("'", "")
            if sys.argv[1].find("http:") == 0\
                    or sys.argv[1].find("https:") == 0:
                file = "temp.json"  # a temporary file to store a web *.json
                urlretrieve(sys.argv[1], file)
                pretty_print_json(file)
                remove(file)
            else:
                pretty_print_json(sys.argv[1])
        else:
            print(usg_msg_err() + "no file or path provided")
    except OSError:
        print(usg_msg_err() + "invalid *.json file or path")
