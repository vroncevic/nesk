# -*- coding: UTF-8 -*-

"""
 Module
     userid.py
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
     Defined class UserID with attribute(s) and method(s).
     Created API for getting or setting user id.
"""

from os import geteuid
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
class UserID:
    """
        Defined class UserID with attribute(s) and method(s).
        Created API for getting or setting user id.
        It defines:

            :attributes:
                | SUDO_USER_ID - root user id in Unix-like systems.
                | __userid - user id object-instance container.
            :methods:
                | user_id - property methods for user id.
                | is_root - check is root user.
    """

    SUDO_USER_ID = 0
    __user_id: int = geteuid()

    @property
    def user_id(self) -> int:
        """
            Property method for getting user id.

            :return: user id for Unix-like systems.
            :rtype: <int>
            :exceptions: None
        """
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """
            Property method for setting user id.

            :param user_id: user id for Unix-like systems.
            :type user_id: <int>
            :return: None
            :exceptions: None
        """
        self.__user_id = user_id

    def is_root(self) -> bool:
        """
            Check is root user.

            :return: boolean status for check is user root.
            :rtype: <bool>
            :exceptions: None
        """
        return bool(self.__user_id == UserID.SUDO_USER_ID)
