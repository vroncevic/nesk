# -*- coding: UTF-8 -*-

"""
 Module
     process.py
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
     Defined class Process with attribute(s) and method(s).
     Created API for getting MAC address by using ARP.
"""

import sys
from subprocess import Popen
from re import search, compile
from dataclasses import dataclass

try:
    from nesk.address.ip_address import IPAddress
    from nesk.address.mac_address import MACAddress
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
class Process:
    """
        Defined class Process with attribute(s) and method(s).
        Created API for getting MAC address by using ARP.
        It defines:

            :attributes:
                | ARP_CLI - arp command line interface.
                | __l3 - IP address object-instance container.
                | __l2 - MAC address object-instance container.
            :methods:
                | get_mac - getting MAC address for IP address by ARP.
    """

    ARP_CLI = 'arp'
    __l3: IPAddress
    __l2: MACAddress

    def get_mac(self, ip_address: str) -> str:
        """
            Getting MAC address for IP address by ARP.

            :param ip_address: IPv4 address.
            :type ip_address: <str>
            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        """
        self.__l3.ip_address = ip_address
        if self.__l3.is_ipv4():
            self.__l2.mac_address = 'TODO'
        else:
            print('Not supported address: {0}'.format(ip_address))
        return '{0}'.format(self.__l2.mac_address)
