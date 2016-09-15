# coding=utf-8
import sys

import pyperclip
from upsidedown import transform


def print_usage():
    print "Call this function by inputting `python flip.py text to flip`"


def flip_text(text):
    flip_master = u"(╯°□°）╯︵ {:s})"
    flip_result = flip_master.format(transform(text))
    pyperclip.copy(flip_result)
    print "The flip has been copied!"
    print flip_result


def main(args):
    if len(args) < 2:
        print_usage()
        sys.exit()
    else:
        flip_text(" ".join(args[1:]))


if __name__ == '__main__':
    main(sys.argv)
