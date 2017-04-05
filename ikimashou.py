#!/usr/bin/python3

import os
import argparse
import errno

def check_path(args):
    if vars(args)['project'][0][0] == '/':
        p = vars(args)['project'][0]
    else:
        p = os.getcwd() + '/' + vars(args)['project'][0]
    return p

def make_dir(p, parser):
    if not os.path.exists(p):
        try:
            os.makedirs(p)
        except OSError as error:
            if error.errno == errno.EEXIST:
                print(parser.prog + ': error: ' + '\'' + p + '\'' + ' already exists.')
            elif error.errno == errno.EACCES:
                print(parser.prog + ': cannot stat ' + '\'' + p + '\''+ ': Permission denied')
    else:
        print(parser.prog + ': error: ' + '\'' + p + '\'' + ' already exists.')
        quit()

def main():
    c_project_dirs = ['lib', 'include', 'src']
    parser = argparse.ArgumentParser(description='Initialize a project', prog='ikimashou')
    parser.add_argument('project', metavar='NAME', nargs='+',
                        help='path for project creation')
    parser.add_argument('--non-c', '-n', action='store_const', const=1,
                        help='Do not add C related initialization folders')
    args = parser.parse_args()
    p = check_path(args)
    make_dir(p, parser)
    if vars(args)['non_c'] is None:
        for elem in c_project_dirs:
            make_dir(p + '/' + elem, parser)
#    with open(p + '/' + '.gitignore'):

    quit()

main()

# with open(filepath, 'w') as my_file:
#     do_stuff(my_file)
