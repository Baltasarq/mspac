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

Add '-f' or '--force' to force operations in case of errors.

### Installing a package

The following command will install package1 and package2:

`mspac install package1 package2`

### Removing a package

Remove package1 and package2:

`mspac remove package1 package2`

### Updating the repositories

You can easily update the repositories:

`mspac update`

### Upgrading packages

Upgrades all packages that are not up-to-date:

`mspac upgrade`

### Syncing packages

Updates the repositories and then updates all packages that are not up-to-date:

`mspac sync`

### Remove unused / orphan packages

Remove packages that are no longer needed in the system:

`mspac autoremove`
