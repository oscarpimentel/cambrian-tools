#!/usr/bin/env python3
# -*- coding: utf-8 -*
import argparse


# parser and settings
parser = argparse.ArgumentParser(prefix_chars='--')
parser.add_argument('--version', type=str)
parser.add_argument('--increase_simple_version', action='store_true')
main_args = parser.parse_args()


# export version
version = main_args.version
counters = [int(c) for c in version.split('.')]
assert len(counters) == 3
if main_args.increase_simple_version:
    counters[2] += 1
new_version = '.'.join([str(c) for c in counters])
text_file = open('version', 'w')
text_file.write(new_version)
text_file.close()
