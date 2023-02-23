#!/usr/bin/python

import os, sys

def loop():
    while True:
        user_input = input("$ ")
        if user_input == "exit":
            break
        if user_input == "":
            continue
        if user_input == '|': #Augment with other operators
            print("Invalid null command.")
            continue
        if user_input in ['>', '>>', '<', '<<']: #Augment this list with other operators
            print("Missing name for redirect.")
            continue

        # Parse & Tokenize input
        tokens = parse(user_input)

        # Fork Processes
        fork_processes(tokens)

def parse(user_input):
    tokens = user_input.split()
    print("command", tokens[0])
    print("args", tokens)
    return tokens

def fork_processes(tokens):
    fork_id = os.fork()
    if fork_id == 0: # Child process
        os.execvp(tokens[0], tokens)
    if tokens[-1] != "&": # continue without waiting
        os.wait()
    return

if __name__ == "__main__":
    loop()

# How to differentiate between files and commands?

# Reorganize into python functions

"""
Todo List:
- pipes with |
- '<' and '>' symbols for I/O passing
- review paper for others
- help with exiting the shell
- testing suite
"""
