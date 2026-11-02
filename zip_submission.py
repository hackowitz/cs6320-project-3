#!/usr/bin/env python3
"""Build the submission zip for CS 6320 Project.

Run from inside the project directory:

    python zip_submission.py --uid u1234567

Produces <uid>.zip containing everything listed in .zip_dir_list.yml. Caches, checkpoints,
and OS junk files are excluded automatically.
"""

import argparse
import glob as globlib
import os
import shutil
import sys

import yaml

MAX_ZIP_BYTES = 25_000_000   

IGNORE = shutil.ignore_patterns(
    '__pycache__', '*.pyc', '*.pyo',
    '.ipynb_checkpoints', '.DS_Store', 'Thumbs.db', '*.egg-info',
)


def copy(src, dest, directory, required):
    kind = 'Directory' if directory else 'File'
    try:
        if directory:
            shutil.copytree(src, dest, ignore=IGNORE)
        else:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy(src, dest)
        return True
    except (shutil.Error, OSError) as e:
        if required:
            print(f'ERROR: required {kind.lower()} "{src}" could not be copied: {e}')
            print('Exiting. SUBMISSION NOT ZIPPED.')
            shutil.rmtree('temp_submission', ignore_errors=True)
            sys.exit(1)
        print(f'Note: optional {kind.lower()} "{src}" is missing, skipping.')
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--uid', required=True, type=str,
                        help='your uID, which begins with "u"')
    args = parser.parse_args()

    if not args.uid.startswith('u'):
        raise ValueError('Your uID must begin with "u" (e.g. u1234567).')

    if not os.path.isfile('.zip_dir_list.yml'):
        print('ERROR: run this from inside the project directory.')
        sys.exit(1)

    shutil.rmtree('temp_submission', ignore_errors=True)
    os.mkdir('temp_submission')

    with open('.zip_dir_list.yml') as f:
        spec = yaml.load(f, Loader=yaml.BaseLoader) or {}

    def section(key):
        return spec.get(key) or []

    for name in section('required_directories'):
        copy(name, os.path.join('temp_submission', name), True, True)
    for name in section('required_files'):
        copy(name, os.path.join('temp_submission', name), False, True)
    for name in section('optional_directories'):
        copy(name, os.path.join('temp_submission', name), True, False)
    for name in section('optional_files'):
        copy(name, os.path.join('temp_submission', name), False, False)

    # patterns, e.g. "additional_data/my*" -- we want the student's own two images but not
    # the copies of the images we already gave them
    for pattern in section('optional_globs'):
        matches = sorted(globlib.glob(pattern))
        if not matches:
            print(f'Note: nothing matched the optional pattern "{pattern}".')
        for path in matches:
            copy(path, os.path.join('temp_submission', path), os.path.isdir(path), False)

    out_file = args.uid + '.zip'
    if os.path.exists(out_file):
        os.remove(out_file)
    shutil.make_archive(args.uid, 'zip', 'temp_submission')
    shutil.rmtree('temp_submission', ignore_errors=True)

    size = os.path.getsize(out_file)
    if size > MAX_ZIP_BYTES:
        print(f'WARNING: {out_file} is {size / 1e6:.1f} MB, over the {MAX_ZIP_BYTES / 1e6:.0f} MB '
              f'guideline.')
        print('This is usually caused by very large images in additional_data/ or by an '
              'enormous number of figures in the notebook. Shrink your own images to '
              '512x512 or smaller and re-run.')
        print('The zip was still created -- check it before submitting.')
    else:
        print(f'Created {out_file} ({size / 1e6:.2f} MB). Upload this to Canvas.')


if __name__ == '__main__':
    main()
