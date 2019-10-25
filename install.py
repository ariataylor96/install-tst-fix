#!/usr/bin/env python3

import argparse
import os


def main(args):
    os.chdir(os.path.dirname(__file__))

    chrome_path = os.path.join(
        os.path.expanduser('~/.mozilla/firefox/'),
        args.profile,
        'chrome'
    )

    css_additions = ''
    js_additions = ''

    with open('userChrome.css', 'r') as f:
        css_additions = f.read()

    with open('userChrome.js', 'r') as f:
        js_additions = f.read()

    with open(os.path.join(chrome_path, 'userChrome.css'), 'a') as f:
        f.write('\n')
        f.write(css_additions)

    with open(os.path.join(chrome_path, 'userChrome.js'), 'a') as f:
        f.write('\n')
        f.write(js_additions)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make TST tabs a little more agreeable')
    parser.add_argument('profile', help='Name of the profile to use')
    main(parser.parse_args())
