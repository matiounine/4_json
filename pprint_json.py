import json
import sys
from os import remove
from urllib.request import urlretrieve


def usage_and_error():
    usage_msg = "python.exe pprint_json.py [path][.json]"
    error_stub = "pprint_json.py: error: "
    return "Usage: " + usage_msg + "\n\n" + error_stub


def load_data(json_to_decode):
    file_obj = open(json_to_decode, encoding="UTF-8")
    json_decoded = json.load(file_obj)
    file_obj.close()
    return json_decoded


def pretty_print_json(json_to_format):
    json_formatted = json.dumps(load_data(json_to_format),
                                ensure_ascii=False, sort_keys=True, indent=4)
    new_json_file = open("pretty.json", "w")
    new_json_file.write(json_formatted)
    new_json_file.close()
    try:
        print(json_formatted)
    except UnicodeEncodeError:
        print("Cannot print to console")
        print(usage_and_error() + "data not supported by code page")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            sys.argv[1] = sys.argv[1].replace("'", "")
            if sys.argv[1].find("http:") == 0\
                    or sys.argv[1].find("https:") == 0:
                tmp_json_file = "temp.json"
                urlretrieve(sys.argv[1], tmp_json_file)
                pretty_print_json(tmp_json_file)
                remove(tmp_json_file)
            else:
                pretty_print_json(sys.argv[1])
        else:
            print(usage_and_error() + "no file or path provided")
    except OSError:
        print(usage_and_error() + "invalid .json file or path")
