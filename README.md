# mspac

An apt-like wrapper for pacman.

## Getting Started

Just clone this repository and execute mspac.py with the supported arguments. Run it without arguments to check the available options.

In order to run this software, you need **Python**, it does not matter what version (provided it is updated enough), **mspac** will run in **Python 2** and **Python 3**.

## Installation

You can use pip in order to retrieve the package from PyPI:
`sudo pip install mspac`

Remember that, in that case, this script will be available system-wide, and that, instead of using `python mspac.py`, you will be able to use just `mspac`. This is important for the examples given below.

## Usage

`python mspac.py [-h] [operation [packages ...]]`

## Examples

### Installing a package

That will install package1 and package2 with pacman

`python mspac.py install package1 package2`

### Updating the repositories

That will update the repositories with pacman

`python mspac.py update`

### Upgrading packages

Upgrades with pacman all packages that are not up-to-date

`python mspac.py upgrade`

### Remove unused / orphan packages

That will remove packages that are no longer needed in the system

`python mspac.py autoremove`
