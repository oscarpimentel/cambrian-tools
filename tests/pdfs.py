#!/usr/bin/env python3
# -*- coding: utf-8 -*
import argparse
import os
import sys

sys.path.append('../../cambrian-tools')  # or just install the module
import cambriantools as ct  # noqa


# parser and settings
parser = argparse.ArgumentParser(prefix_chars='--')
parser.add_argument('--model', type=str)
parser.add_argument('--kf', type=str)
parser.add_argument('--config', type=str)
parser.add_argument('--uses_da', action='store_true')
main_args = parser.parse_args()

filedirs = ct.files.get_filedirs(os.path.join('..', 'data'), fext='pdf')
for filedir in filedirs:
    save_path = os.path.split(filedir)[0].replace('../data', '../save')
    print(f'filedir={filedir}; save_path={save_path}')
    ct.pdfs.save_imgs_from_pdf(filedir, save_path)