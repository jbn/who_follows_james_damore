#!/usr/bin/env python
#
# Note: If this script fails half-way, relationships break and the whole
# thing is fucked.
from __future__ import print_function

import json
import os
import random

from collections import defaultdict


RAW_DIR = os.path.join("data", "raw")
CLEAN_DIR = os.path.join("data", "clean")
CUR_SYM = 0


def gensym():
    global CUR_SYM

    CUR_SYM += 1
    return CUR_SYM


if __name__ == '__main__':
    remapped = defaultdict(gensym)

    for file_name in os.listdir(RAW_DIR):
        if not file_name.endswith(".json"):
            continue

        print(file_name, end=': ')

        with open(os.path.join(RAW_DIR, file_name)) as fp:
            ids = json.load(fp)

        random.shuffle(ids)
        anonymized_ids = [remapped[i] for i in ids]

        # Sanity Check
        j, k = sum(ids), sum(anonymized_ids)
        print(j, k)
        assert j != k

        with open(os.path.join(CLEAN_DIR, file_name), 'w') as fp:
            json.dump(anonymized_ids, fp)
