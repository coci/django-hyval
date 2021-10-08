# -*- coding: utf-8 -*-
#
# Copyright (C) 2021- Soroush Safari <mr.safarii1992@gmail.com>
#
# This file is part of Hyval.
#
# Hyval is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hyval is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with grest.  If not, see <http://www.gnu.org/licenses/>.
#
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt_keys(salt, key, value):
    """
            encrypt user credential
    """
    secret_key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=bytes(salt, 'utf-8'), iterations=1000,
                            backend=default_backend()).derive(bytes(key, 'utf-8'))
    fernet_obj = Fernet(base64.urlsafe_b64encode(secret_key))
    return fernet_obj.encrypt(bytes(value, 'utf-8')).decode("utf-8")


def decrypt_keys(salt, key, value):
    """
            decrypt user credential
    """

    secret_key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=bytes(salt, 'utf-8'), iterations=1000,
                            backend=default_backend()).derive(bytes(key, 'utf-8'))
    fernet_obj = Fernet(base64.urlsafe_b64encode(secret_key))
    return fernet_obj.decrypt(bytes(value, 'utf-8')).decode("utf-8")
