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

from re import compile, search

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/nesk'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/nesk/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MACAddress:
    """
        Defined class MACAddress with attribute(s) and method(s).
        Created API for getting/setting/checking MAC address.
        It defines:

            :attributes:
                | MAC_REGEX_CHECK_1 - regex for checking MAC address format.
                | MAC_REGEX_CHECK_2 - regex for checking MAC address format.
                | MAC_REGEX_CHECK_3 - regex for checking MAC address format.
                | MAC_REGEX_CHECK_4 - regex for checking MAC address format.
                | MAC_REGEX_CHECK_5 - regex for checking MAC address format.
                | __mac_address - MAC address object-instance container.
            :methods:
                | __init__ - initial constructor.
                | mac_address - property methods for MAC address.
                | is_mac_address - check for MACAddress format.
                | __str__ - dunder method for MACAddress.
    """

    MAC_REGEX_CHECK_1 = '^([0-9A-Fa-f]{2}[:-])'
    MAC_REGEX_CHECK_2 = '{5}([0-9A-Fa-f]{2})|'
    MAC_REGEX_CHECK_3 = '([0-9a-fA-F]{4}\\.'
    MAC_REGEX_CHECK_4 = '[0-9a-fA-F]{4}\\.'
    MAC_REGEX_CHECK_5 = '[0-9a-fA-F]{4})$'

    def __init__(self, mac_address: str):
        """
            Initial constructor.

            :param mac_address: MAC address for checking.
            :type mac_address: <str>
            :return: None
            :exceptions: None
        """
        self.__mac_address = mac_address

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
            ''.join([
                MACAddress.MAC_REGEX_CHECK_1,
                MACAddress.MAC_REGEX_CHECK_2,
                MACAddress.MAC_REGEX_CHECK_3,
                MACAddress.MAC_REGEX_CHECK_4,
                MACAddress.MAC_REGEX_CHECK_5
            ])
        )
        patter_search = compile(compile_regex)
        if not bool(self.__mac_address):
            return False
        if search(patter_search, self.__mac_address):
            return True
        else:
            return False

    def __str__(self) -> str:
        """
            Dunder method for MACAddress.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        """
        return '{0} ({1})'.format(self.__class__.__name__, self.__mac_address)
