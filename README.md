# mspac

An apt-like wrapper for pacman.

## Getting Started

Just clone this repository and execute mspac.py with the supported arguments.

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

## Installation

You can install mspac as a system binary for easier operation. Open a terminal in the project folder and run:

`sudo mv mspac.py /usr/bin/mspac && sudo chmod +x /usr/bin/mspac`

You should be prompted with a password input. After doing this you can execute mspac this way:

`mspac install package1 package2`

## License

MIT License

Copyright (c) 2017 Baltasar García Perez-Schofield

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
