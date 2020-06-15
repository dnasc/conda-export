#!/usr/bin/env python

import re
import subprocess
import sys


def main():
    p = subprocess.Popen(['conda', 'env', 'list'], stdout=subprocess.PIPE, universal_newlines=True)
    lines = p.stdout.readlines()
    env_names = []
    for line in lines:
        found = re.search('^[^#][^\s]+', line)
        if found is not None:
            env_names.append(found.group())
    p.wait()

    for env_name in env_names:
        with open(f'{env_name}.yaml', 'w') as f:
            p = subprocess.Popen(['conda', 'env', 'export', '-n', env_name], stdout=f)
            p.wait()


if __name__ == '__main__':
    sys.exit(main())
