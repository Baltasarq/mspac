#!/usr/bin/env python
# encoding: utf-8
# mspac (c) 2017 baltasarq@gmail.com MIT License


__version__ = "0.3.2 20170608"

import argparse
import subprocess


CMD_ROOT = "sudo"
CMD_PKGR = "pacman"
UPDATE_ARGS = "-Sy"
FORCE_ARG = "--force"
UPGRADE_ARGS = "-Su"
INSTALL_ARGS = "-S"
REMOVE_ARGS = "-R"
SHOW_ARGS = "-Qi"
LIST_ARGS = "-Ss"
PURGE_ARGS = "-Rns"
ORPHAN_ARGS = "-Qtdq"


def update(force):
    """Updates pacman's databases."""
    args = [CMD_ROOT, CMD_PKGR]

    if force:
        args.append(FORCE_ARG)

    ret_info = execute("Updating", args + [UPDATE_ARGS])
    
    if ret_info.returncode == 0:
        print("Databases updated.")


def upgrade(force):
    """Upgrades all available packages."""
    args = [CMD_ROOT, CMD_PKGR]
    
    if force:
        args.append(FORCE_ARG)


    ret_info = execute("Upgrading", args + [UPGRADE_ARGS])

    if ret_info.returncode == 0:
        print("All pending packages upgraded.")


def autoremove():
    """Removes all unneeded packages."""
    ret_info = execute("Obtaining orphans", [CMD_PKGR, ORPHAN_ARGS])
    pkg_info = ret_info.stdout.split()

    if ret_info.returncode == 0:
        print( "pks:", ' '.join(pkg_info))
        ret_info = execute("Removing orphans",
                           [CMD_ROOT, CMD_PKGR, PURGE_ARGS] + pkg_info)

        if ret_info.returncode == 0:
            print("Orphaned packages removed.")



def install(pkg_list, force):
    """Installs a list of packages."""
    args = [CMD_ROOT, CMD_PKGR]

    if force:
        args.append(FORCE_ARG)

    ret_info = execute("Installing packages", args + [INSTALL_ARGS] + pkg_list)

    if ret_info.returncode == 0:
        print("Packages installed successfully.")


def remove(pkg_list, force):
    """Removes a list of packages."""
    args = [CMD_ROOT, CMD_PKGR]

    if force:
        args.append(FORCE_ARG)

    ret_info = execute("Removing packages", args + [REMOVE_ARGS] + pkg_list)

    if ret_info.returncode == 0:
        print("Packages removed successfully.")


def show(pkg_list):
    """Shows detailed info about a given package."""
    ret_info = execute("Showing details", [CMD_PKGR, SHOW_ARGS] + pkg_list)
    if ret_info.returncode == 0:
        print(ret_info.stdout)

def lists(pkg_list):
    """Shows a list of packages given keywords."""
    ret_info = execute("Listing packages", [CMD_PKGR, LIST_ARGS] + pkg_list)
    if ret_info.returncode == 0:
        print(ret_info.stdout)


def execute(msg, call_args):
    """Executes a generic command for pacman.

        :param msg: The msg to show describing the operation.
        :param args: The arguments for the command, after "pacman".
    """
    print(msg + " with: " + " ".join(call_args))

    ret_info = subprocess.run(
        call_args,
        universal_newlines=True,
        stdout=subprocess.PIPE)

    if ret_info.returncode != 0:
        print("finished with code:", ret_info.returncode)

    return ret_info

def main():
    print("MSPacman v" + __version__ + '\n')
    parser = argparse.ArgumentParser()
    parser.add_argument("operation",
                        help="Selects the operation to execute with a list of packages to target, if needed. "
                        "Supported operations: sync, update, upgrade, autoremove, install, remove, show, list. "
                        "Example: mspac install package1...",
                        nargs="+")
    parser.add_argument("-f", "--force",
                        action="store_true",
                        help="Forces the operation even when conflicts or errors are found. Example: mspac --force install package1")

    args = parser.parse_args()

    if len(args.operation) > 0:
        args.operation = [x.lower() for x in args.operation]

        if args.operation[0] == "sync":
            if len(args.operation) > 1:
                print("Sync needs no parameters. Ignoring them")
            update(args.force)
            upgrade(args.force)
        elif args.operation[0] == "update":
            if len(args.operation) > 1:
                print("Update needs no parameters. Ignoring them")
            update(args.force)
        elif args.operation[0] == "upgrade":
            if len(args.operation) > 1:
                print("Upgrade needs no parameters. Ignoring them")
            upgrade(args.force)
        elif args.operation[0] == "autoremove":
            if len(args.operation) > 1:
                print("Autoremove needs no parameters. Ignoring them")
            autoremove()
        elif args.operation[0] == "install":
            install(args.operation[1:], args.force)
        elif args.operation[0] == "remove":
            remove(args.operation[1:], args.force)
        elif args.operation[0] == "show":
            show(args.operation[1:])
        elif args.operation[0] == "list":
            lists(args.operation[1:])
        else:
            print("Operation unsupported. See help.")

    print("End\n")

if __name__ == "__main__":
    main()
