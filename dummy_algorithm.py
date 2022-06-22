#!/usr/bin/env python3
# -*- coding: utf-8 -*
import argparse
import time
import os
import pprint
import json

import toml
import cambriantools as ct
from dynaconf import settings

from utils import DummyClass


# parser and settings
parser = argparse.ArgumentParser(prefix_chars='--')
parser.add_argument('--model', type=str)
parser.add_argument('--kf', type=str)
parser.add_argument('--config', type=str)
parser.add_argument('--uses_da', action='store_true')
main_args = parser.parse_args()


# do things
dummy_class = DummyClass()
print(dummy_class)
# load
d = {
    'uses_da': main_args.uses_da,
}
filedir = os.path.join(settings.CONFIG_PATH, f'{main_args.config}.json')
file = open(filedir)
setting_file = json.load(file)
persons = setting_file['persons']
pprint.pprint(persons)
d.update(setting_file)
filedir = os.path.join(settings.DATA_PATH, 'lists.toml')
toml_file = toml.load(filedir)
d.update(toml_file)
pprint.pprint(d)
# save
filedir = os.path.join(settings.SAVE_PATH, f'kf={main_args.kf}~model={main_args.model}', 'd.pkl')
ct.files.create_dir_for_filedir(filedir)
ct.files.save_pickle(filedir, d)
time.sleep(5)
raise SystemExit