#!/usr/bin/env python3
# -*- coding: utf-8 -*
import argparse
import time
import os
import pprint
import json

from dynaconf import settings

import cambriantools as ct


# parser and settings
parser = argparse.ArgumentParser(prefix_chars='--')
parser.add_argument('--model', type=str)
parser.add_argument('--kf', type=str)
parser.add_argument('--config', type=str)
parser.add_argument('--uses_da', action='store_true')
main_args = parser.parse_args()


# do things
# load
filedir = os.path.join(settings.CONFIG_PATH, f'{main_args.config}.json')
print(filedir)
file = open(filedir)
setting_file = json.load(file)
d = {}
d.update(setting_file)
pprint.pprint(d)
# save
filedir = os.path.join(settings.SAVE_PATH, f'kf={main_args.kf}~model={main_args.model}', 'd.pkl')
ct.files.create_dir_for_filedir(filedir)
ct.files.save_pickle(filedir, d)
time.sleep(5)