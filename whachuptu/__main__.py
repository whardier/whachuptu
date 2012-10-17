#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2012  Shane R. Spencer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Whachuptu: Active Work/Project Logger"""

import sys
import argparse
import logging

import whachuptu

def main(argv=[]):
    assert isinstance(argv, list)

    if not argv:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description=whachuptu.__description__)

    subparsers = parser.add_subparsers(title='Command', dest='command')

    server_parser = subparsers.add_parser('server', help='Server commands')

    server_parser.add_argument('listen',
        action='store',
        help='http://host[:port]',
        metavar='LISTENURI')

    server_parser.add_argument('mongodb',
        action='store',
        help='mongodb://[user[:pass]@]host[:port]',
        metavar='MONGODBURI')

    server_parser.add_argument('-v',
        dest='verbose',
        action='count',
        help='Add multiple times for increased verbosity')

    args = parser.parse_args(argv)

    loglevel = logging.CRITICAL

    if args.verbose >= 4:
        loglevel = logging.DEBUG
    elif args.verbose == 3:
        loglevel = logging.INFO
    elif args.verbose == 2:
        loglevel = logging.WARNING
    elif args.verbose == 1:
        loglevel = logging.ERROR

    logging.basicConfig(level=loglevel)

    logger = logging.getLogger('Arguments')

    for arg, value in vars(args).iteritems():
        logger.debug('%s:%s' % (arg, value))

    logger = logging.getLogger('General')
    logger.info('Lets get SHT done!')

    if args.command == 'server':
        whachuptu.serve_forever(vars(args))            
    else:
        logger.info('Interesting... I should not have been called.')


if __name__ == '__main__':
    sys.exit(main())
