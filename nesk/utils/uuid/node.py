# -*- coding: UTF-8 -*-

"""
 Module
     node.py
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
     Defined class Node with attribute(s) and method(s).
     Created API for getting or setting node uuid and MAC address.
"""

from dataclasses import dataclass
from uuid import getnode

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/nesk'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/nesk/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass
class Node:
    """
        Defined class Node with attribute(s) and method(s).
        Created API for getting or setting node uuid and MAC address.
        It defines:

            :attributes:
                | __uuid - node uuid.
            :methods:
                | uuid - property methods for node uuid.
                | get_default_uuid - method for getting default node uuid.
                | mac_from_uuid - method for getting MAC address from uuid.
    """

    __uuid: int

    @property
    def uuid(self) -> int:
        """
            Property method for getting node uuid.

            :return: node uuid.
            :rtype: <int>
            :exceptions: None
        """
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: int):
        """
            Property method for setting node uuid.

            :param uuid: node uuid.
            :type uuid: <int>
            :return: None
            :exceptions: None
        """
        self.__uuid = uuid

    def get_default_uuid(self) -> int:
        """
            Method for getting default node uuid.

            :return: node uuid.
            :rtype: <int>
            :exceptions: None
        """
        self.__uuid = getnode()
        return self.__uuid

    def mac_from_uuid(self):
        """
            Method for getting MAC address from uuid.

            :return: MAC address.
            :rtype: <str>
            :exceptions: None
        """
        mac_address = []
        for elements in range(0, 2 * 6, 2)[::-1]:
            mac_address.append(
                '{:02x}'.format((self.__uuid >> elements) & 0xff)
            )
        return ':'.join(mac_address)
