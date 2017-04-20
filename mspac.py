#!/usr/bin/env python
# encoding: utf-8
# mspac (c) 2017 baltasarq@gmail.com MIT License

import argparse
import os


PACMAN_EXECUTABLE = "pacman"
PACMAN_SYNC_ARGS = "-Sy"
PACMAN_UPGRADE_ARGS = "-Su"
PACMAN_AUTOREMOVE_ARGS = "-Rns $(" + PACMAN_EXECUTABLE + " -Qtdq)"


def update():
    """Updates pacman's databases."""
    execute("Updating", PACMAN_SYNC_ARGS)
    
def upgrade():
    """Upgrades all available packages."""
    execute("Upgrading", PACMAN_UPGRADE_ARGS)
    
def autoremove():
    """Removes all unneeded packages."""
    execute("Removing orphans", PACMAN_AUTOREMOVE_ARGS)

def execute(msg, args):
    """Executes a generic command for pacman.
    
        :param msg: The msg to show describing the operation.
        :param args: The arguments for the command, after "pacman".
    """
    cmd = PACMAN_EXECUTABLE + " " + args
    print(msg + " with: " + cmd)
    ret_code = os.system(cmd)
    print("finished with code: " + str(ret_code))


if __name__ == "__main__":
    print("MSPacman v0.1 20170420\n")
    parser = argparse.ArgumentParser()
    parser.add_argument("operation",
                        help="selects the operation to execute.",
                        choices=["update", "upgrade", "autoremove"])
    args = parser.parse_args()
    args.operation = args.operation.lower()
    
    if args.operation == "update":
        update()
    elif args.operation == "upgrade":
        upgrade()
    elif args.operation == "autoremove":
        autoremove()
    else:
        print("Operation unsupported.")
        
    print("End\n")
