<img align="right" src="https://raw.githubusercontent.com/vroncevic/nesk/dev/docs/nesk_logo.png" width="25%">

# nesk

**nesk** is framework for network administration.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/nesk/workflows/Python%20package%20nesk/badge.svg?branch=main) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/nesk.svg)](https://github.com/vroncevic/nesk/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/nesk.svg)](https://github.com/vroncevic/nesk/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Framework structure](#framework-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python3 Package](https://github.com/vroncevic/nesk/workflows/Install%20Python3%20Package%20nesk/badge.svg?branch=main)

Currently there are three ways to install framework:
* Install process based on using pip
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/nesk/)**.

You can install by using pip
```
# python3
pip3 install nesk
```

##### Install using setuptools

Navigate to **[release page](https://github.com/vroncevic/nesk/releases)** download and extract release archive.

To install modules, locate and run setup.py with arguments
```
tar xvzf nesk-x.y.z.tar.gz
cd nesk-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

[![nesk docker checker](https://github.com/vroncevic/nesk/workflows/nesk%20docker%20checker/badge.svg)](https://github.com/vroncevic/nesk/actions?query=workflow%3A%22nesk+docker+checker%22)

### Dependencies

These modules requires other modules and libraries:


### Framework structure

**nesk** is based on OOP.

Framework structure:
```

```

### Docs

[![Documentation Status](https://readthedocs.org/projects/nesk/badge/?version=latest)](https://nesk.readthedocs.io/projects/nesk/en/latest/?badge=latest)

More documentation and info at:
* [nesk.readthedocs.io](https://nesk.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2021 by [vroncevic.github.io/nesk](https://vroncevic.github.io/nesk/)

**nesk** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/nesk/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
