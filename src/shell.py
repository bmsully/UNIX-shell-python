#!/usr/bin/python

import os, sys

# Loop forever
while True:
    user_input = input("$ ")
    if user_input == "exit":
        break
    if user_input == "":
        continue

    tokens = user_input.split()

    fork_id = os.fork()
    if fork_id == 0: # we are the child
        os.execvp(tokens[0], tokens)
    if tokens[-1] != "&": # continue without waiting
        os.wait()

"""
Todo List:
- pipes with |
- '<' and '>' symbols for I/O passing
- review paper for others
- help with exiting the shell
- testing suite
"""
