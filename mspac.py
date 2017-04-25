#!/usr/bin/env python
# encoding: utf-8
# mspac (c) 2017 baltasarq@gmail.com MIT License

import argparse
import os


PACMAN_EXECUTABLE = "pacman"
PACMAN_SYNC_ARGS = "-Sy"
PACMAN_UPGRADE_ARGS = "-Su"
PACMAN_INSTALL_ARGS = "-S"
PACMAN_REMOVE_ARGS = "-R"
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


def install(package_list):
    """Installs a list of packages"""
    execute("Installing packages", "{} {}".format(PACMAN_INSTALL_ARGS, " ".join(package_list)))


def remove(package_list):
    """Removes a list of packages"""
    execute("Removing packages", "{} {}".format(PACMAN_REMOVE_ARGS, " ".join(package_list)))


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
                        help="Selects the operation to execute with a list of packages to target, if needed. "
                        "Supported operations: update, upgrade, autoremove, install, remove. "
                        "Example: mspac.py install package1 package2",
                        nargs="*")

    args = parser.parse_args()
    args.operation = [x.lower() for x in args.operation]

    if args.operation[0] == "update":
        if len(args.operation) > 1:
            print("Update needs no parameters. Ignoring them")
        update()
    elif args.operation[0] == "upgrade":
        if len(args.operation) > 1:
            print("Upgrade needs no parameters. Ignoring them")
        upgrade()
    elif args.operation[0] == "autoremove":
        if len(args.operation) > 1:
            print("Autoremove needs no parameters. Ignoring them")
        autoremove()
    elif args.operation[0] == "install":
        install(args.operation[1:])
    elif args.operation[0] == "remove":
        remove(args.operation[1:])
    else:
        print("Operation unsupported. See help.")

    print("End\n")
