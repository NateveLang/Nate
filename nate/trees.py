"""
build.py

This module is responsible for building the source code.

It contains the following functions:
    build: builds the source code.
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

from nate.file import       read_module
from nate.lex import        scanner
from nate.syntax import     parser

def make_tree(file, args = ["none"]):
    """
This function builds the source code.

It takes the following arguments:
    file: the name of the file to be built.
    args: the arguments used to build the source code.
    main: the main argument passed to the generator.
    exceptions: the exceptions argument passed to the generator.
    driver: the driver used to format the generated code.
"""

    dev_mode = "dev" in args
    save_to_file_mode = "file" in args

    text = read_module(file)
    file_name = file
    file = file.split(".")[0]

    if text == None:
        text = ""

    tokens, errors, lex_log, templates, modules = scanner(text, args)
    tree, tokens, errors = parser(tokens, file, errors)

    if dev_mode:
        print(tokens)
        tree.display()

    if save_to_file_mode:
        
        with open(file_name + "_file_saved.evelog", "w") as f:
            print(tokens, file = f)
            print("", file = f)
            tree.display(file = f)

    return tree
