#!/usr/bin/env python

from __future__ import print_function
import sys
import os.path
import argparse

libdir=os.path.normpath(os.path.sep.join([os.path.dirname(sys.argv[0]),'..','lib']))
eggs = [ 
            'passlib-1.6.5-py2.py3-none-any.whl',
       ]

for i in eggs:
    sys.path.append(os.path.sep.join([libdir,i]))

import passlib

passwdfile=os.path.normpath(os.path.sep.join([os.path.dirname(sys.argv[0]),'..','etc','passwd']))

def spl_getpwent(user):


def do_edit(args):
    print(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers=parser.add_subparsers(help='sub-command help',dest='subcommand')
    edit=subparsers.add_parser('edit-user',help='edit user')

    edit.add_argument("username", help="user name")
    edit.add_argument("--password")
    edit.add_argument("--roles")
    edit.add_argument("--realname")
    edit.add_argument("--email")


    args=parser.parse_args()
    if args.subcommand == 'edit-user':
        do_edit(args)    
 


