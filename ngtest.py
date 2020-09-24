#!/usr/bin/env python
import os
import sys


def main(argv=None):
    '''
    Handle various pre-commit config options:
    - args:
        - if set, a bare double-dash is needed to distinguish options from the list of filenames
        - args before '--' are test options and args after '--' are filenames
    - pass_filenames:
        - if false, ng test should run over the full project
    '''
    cmd = ['ng', 'test'] # If no args, run ng test over the whole project

    if len(sys.argv) > 1: # sys.argv => command + args; length >= 1
        if '--' in sys.argv:
            # argv items before '--' are test options
            bare_dd_index = sys.argv.index('--')
            cmd = cmd + sys.argv[1:bare_dd_index]

            # argv items after '--' are filenames (if provided)
            filenames = sys.argv[bare_dd_index+1:]
            if len(filenames):
                cmd += ['--files'] + filenames
        else:
            # argv items are the filenames
            cmd = (cmd + ['--files'] + sys.argv[1:])
    print(cmd)
    os.execvp(cmd[0], cmd)

if __name__ == '__main__':
    exit(main())
