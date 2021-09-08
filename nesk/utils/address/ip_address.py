# -*- coding: UTF-8 -*-

"""
 Module
     ip_address.py
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
     Defined class IPAddress with attribute(s) and method(s).
     Created API for getting/setting/checking IP address.
"""

from dataclasses import dataclass

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/nesk'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/nesk/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass
class IPAddress:
    """
        Defined class IPAddress with attribute(s) and method(s).
        Created API for getting/setting/checking IP address.
        It defines:

            :attributes:
                | __ip_address - IP address object-instance container.
            :methods:
                | ip_address - property methods for IP address.
                | is_ipv4 - check IPv4 address format.
                | is_ipv6 - check IPv6 address format.
    """

    __ip_address: str

    @property
    def ip_address(self) -> str:
        """
            Property method for getting IP address.

            :return: IP address for checking MAC address.
            :rtype: <str>
            :exceptions: None
        """
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str):
        """
            Property method for setting IP address.

            :param ip_address: IP address for checking MAC address.
            :type ip_address: <str>
            :return: None
            :exceptions: None
        """
        self.__ip_address = ip_address

    def is_ipv4(self) -> bool:
        """
            Check IPv4 address format.

            :return: status about IPV4 format.
            :rtype: <bool>
            :exceptions: None
        """
        status = []
        if self.__ip_address.count('.') == 3:
            for i in self.__ip_address.split('.'):
                if str(int(i)) == i and 0 <= int(i) <= 255:
                    status.append(True)
                else:
                    status.append(False)
        else:
            status.append(False)
        return all(status)

    def is_ipv6(self) -> bool:
        """
            Check IPv6 address format.

            :return: status about IPV6 format.
            :rtype: <bool>
            :exceptions: None
        """
        status = []
        if self.__ip_address.count(':') == 7:
            for i in self.__ip_address.split(':'):
                if len(i) > 4:
                    status.append(False)
                else:
                    if int(i, 16) >= 0 and i[0] != '-':
                        status.append(True)
                    else:
                        status.append(False)
        else:
            status.append(False)
        return all(status)
