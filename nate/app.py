"""
app.py

The entry point of the program from Python Scripts. It drives the program, and allows to
use the program in console.
"""

author = "eanorambuena"
author_email = "eanorambuena@uc.cl"

#	MIT License
#	
#	Copyright (c) 2021 Emmanuel Norambuena Sepulveda
#	
#	Permission is hereby granted, free of charge, to any person obtaining a copy
#	of this software and associated documentation files (the "Software"), to deal
#	in the Software without restriction, including without limitation the rights
#	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#	copies of the Software, and to permit persons to whom the Software is
#	furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all
#	copies or substantial portions of the Software.
#	
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#	SOFTWARE.

import sys

from nate.error import FileError
from nate.trees import make_tree

def get_argument(position, plural = False):
    """
Get an argument from command line, with a specific position.
You can get more than one argument, if you set 'plural' to True.

It receives the following arguments:
    position: The position of the argument in the command line.
    plural:   If you want to get more than one argument, set it to True.
"""

    if plural:

        try:
            return sys.argv[position:]
        except:
            return ["none"]

    try:
        return sys.argv[position]
    except:
        return "none"

def main():
    params = sys.argv[:]

    if len(params) >= 2:
        file_name = params[1]
        tree = make_tree(file_name, get_argument(2, True))
        return tree

    else:
        FileError(None, "no file or argument specified")