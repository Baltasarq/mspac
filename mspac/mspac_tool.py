#!/usr/bin/env python
# encoding: utf-8
# mspac (c) 2017 baltasarq@gmail.com MIT License


__version__ = "0.3.1 20170605"

import argparse
import subprocess


CMD_ROOT = "sudo"
CMD_PKGR = "pacman"
SYNC_ARGS = "-Sy"
UPGRADE_ARGS = "-Su"
INSTALL_ARGS = "-S"
REMOVE_ARGS = "-R"
SHOW_ARGS = "-Qi"
LIST_ARGS = "-Ss"
AUTOREMOVE_ARGS = "-Rns $(" + CMD_PKGR + " -Qtdq)"


def update():
    """Updates pacman's databases."""
    execute("Updating", [CMD_ROOT, CMD_PKGR, SYNC_ARGS])


def upgrade():
    """Upgrades all available packages."""
    execute("Upgrading", [CMD_ROOT, CMD_PKGR, UPGRADE_ARGS])


def autoremove():
    """Removes all unneeded packages."""
    execute("Removing orphans", [CMD_ROOT, CMD_PKGR, AUTOREMOVE_ARGS])


def install(pkg_list):
    """Installs a list of packages."""
    execute("Installing packages", [CMD_ROOT, CMD_PKGR, INSTALL_ARGS] + pkg_list)


def remove(pkg_list):
    """Removes a list of packages."""
    execute("Removing packages", [CMD_ROOT, CMD_PKGR, REMOVE_ARGS] + pkg_list)


def show(pkg_list):
    """Shows detailed info about a given package."""
    execute("Showing details", [CMD_PKGR, SHOW_ARGS] + pkg_list)

def lists(pkg_list):
    """Shows a list of packages given keywords."""
    execute("Listing packages", [CMD_PKGR, LIST_ARGS] + pkg_list)


def execute(msg, call_args):
    """Executes a generic command for pacman.

        :param msg: The msg to show describing the operation.
        :param args: The arguments for the command, after "pacman".
    """
    print(msg + " with: " + " ".join(call_args))
    ret_code = subprocess.call(call_args)
    print("finished with code: " + str(ret_code))

def main():
    print("MSPacman v" + __version__ + '\n')
    parser = argparse.ArgumentParser()
    parser.add_argument("operation",
                        help="Selects the operation to execute with a list of packages to target, if needed. "
                        "Supported operations: sync, update, upgrade, autoremove, install, remove, show, list. "
                        "Example: mspac install package1...",
                        nargs="+")

    args = parser.parse_args()

    if len(args.operation) > 0:
        args.operation = [x.lower() for x in args.operation]

        if args.operation[0] == "sync":
            if len(args.operation) > 1:
                print("Sync needs no parameters. Ignoring them")
            update()
            upgrade()
        elif args.operation[0] == "update":
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
        elif args.operation[0] == "show":
            show(args.operation[1:])
        elif args.operation[0] == "list":
            lists(args.operation[1:])
        else:
            print("Operation unsupported. See help.")

    print("End\n")

if __name__ == "__main__":
    main()
