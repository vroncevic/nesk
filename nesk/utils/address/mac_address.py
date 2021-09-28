# -*- coding: UTF-8 -*-

"""
 Module
     mac_address.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
     nesk is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     nesk is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class MACAddress with attribute(s) and method(s).
     Created API for getting/setting/checking MAC address.
"""

import sys
from dataclasses import dataclass
from re import compile, search

try:
    from nesk.utils.address.mac_regex import MacRegex
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/nesk'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/nesk/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass
class MACAddress:
    """
        Defined class MACAddress with attribute(s) and method(s).
        Created API for getting/setting/checking MAC address.
        It defines:

            :attributes:
                | __mac_address - MAC address object-instance container.
            :methods:
                | mac_address - property methods for MAC address.
                | is_mac_address - check for MACAddress format.
    """

    __mac_address: str

    @property
    def mac_address(self) -> str:
        """
            Property method for getting IP address.

            :return: MAC address for checking.
            :rtype: <str>
            :exceptions: None
        """
        return self.__mac_address

    @mac_address.setter
    def mac_address(self, mac_address: str):
        """
            Property method for setting MAC address.

            :param mac_address: MAC address for checking.
            :type mac_address: <str>
            :return: None
            :exceptions: None
        """
        self.__mac_address = mac_address

    def is_mac_address(self) -> bool:
        """
            Check for MAC address format.

            :return: status for MAC address format.
            :rtype: <bool>
            :exceptions: None
        """
        compile_regex = (
            ''.join(['{0}'.format(mac_check.value) for mac_check in MacRegex])
        )
        patter_search = compile(compile_regex)
        if not bool(self.__mac_address):
            return False
        if search(patter_search, self.__mac_address):
            return True
        else:
            return False
