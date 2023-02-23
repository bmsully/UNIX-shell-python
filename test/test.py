#!/usr/bin/python

import unittest, os

class TestShell(unittest.TestCase):
    def runShell(self, input_text):
        tokens = input_text.split()
        os.execvp(tokens[0], tokens)

