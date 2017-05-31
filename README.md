# mspac

An apt-like wrapper for pacman.

## Getting Started

In order to run this software, you need **Python**, it does not matter what version (provided it is updated enough), **mspac** will run in **Python 2** and **Python 3**.

## Installation

You can (and you are encouraged to) use pip in order to retrieve the package from PyPI:
`sudo pip install mspac`
Then run it without arguments (`mspac`), to check the available options.

Alternately, just clone this repository and execute `mspac/mspac_tool.py` with the supported arguments.

## Usage

`mspac [-h] [operation [packages ...]]`

## Examples

### Installing a package

That will install package1 and package2 with pacman

`mspac install package1 package2`

### Updating the repositories

That will update the repositories with pacman

`mspac update`

### Upgrading packages

Upgrades with pacman all packages that are not up-to-date

`mspac upgrade`

### Remove unused / orphan packages

That will remove packages that are no longer needed in the system

`mspac autoremove`
