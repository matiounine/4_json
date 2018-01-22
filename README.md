# Prettify JSON

The script **`pprint_json.py`** re-formats data from a given raw *JSON*-file for it to be more readable by the human eye, providing proper indentations and sorting the data by the key, and prints the result to a new file ( *pretty.json* ) and to the console, still in the *JSON*-format.

# Quickstart

You may import the function **`pretty_print_json()`** from the script **`pprint_json.py`** to your code, pass in, as an argument, a path* and a *JSON*-file to be re-formatted, as follows:

```python

	from pprint_json import pretty_print_json
	pretty_print_json("https:\\... ...\<file_name>.json")
	# output is written in the file <pretty.json>
	# and printed to the console

```

Or you may use the script **`pprint_json.py`** as a stand-alone utility, providing the path and file needed right in the command line, as follows:

(Example of script launch on Windows, Python 3.5)

```cmd

	python pprint_json.py "https:\\... ...\<file_name>.json"
	# output is written in the file <pretty.json>
	# and printed to the console

```

(Example of script launch on Linux, Python 3.5)

```bash

	$ python pprint_json.py <path to file>
	# output is written in the file <pretty.json>
	# and printed to the console

```

*Both local and web kinds of path are supported.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
