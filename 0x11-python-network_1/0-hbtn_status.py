#!/usr/bin/python3
# this script fetches https://alx-intranet.hbtn.io/status
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print('Body response:')
        print('    - type: {}'.format(type(the_page)))
        print('    - content: {}'.format(the_page))
        print('    - utf8 content: {}'.format(the_page.decode("utf-8")))
