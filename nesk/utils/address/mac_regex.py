# -*- coding: UTF-8 -*-

"""
 Module
     mac_regex.py
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
     Defined class MacRegex with attribute(s).
     Created regex for checking MAC address.
"""

from enum import Enum, unique

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/nesk'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/nesk/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@unique
class MacRegex(Enum):
    """
        Defined class MacRegex with attribute(s).
        Created regex for checking MAC address.
        It defines:

            :attributes:
                | MAC_ADDRESS_CHECK_1 - regex for checking MAC address format.
                | MAC_ADDRESS_CHECK_2 - regex for checking MAC address format.
                | MAC_ADDRESS_CHECK_3 - regex for checking MAC address format.
                | MAC_ADDRESS_CHECK_4 - regex for checking MAC address format.
                | MAC_ADDRESS_CHECK_5 - regex for checking MAC address format.
            :methods:
                | None
    """
    MAC_ADDRESS_CHECK_1 = '^([0-9A-Fa-f]{2}[:-])'
    MAC_ADDRESS_CHECK_2 = '{5}([0-9A-Fa-f]{2})|'
    MAC_ADDRESS_CHECK_3 = '([0-9a-fA-F]{4}\\.'
    MAC_ADDRESS_CHECK_4 = '[0-9a-fA-F]{4}\\.'
    MAC_ADDRESS_CHECK_5 = '[0-9a-fA-F]{4})$'
