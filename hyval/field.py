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

try:
    from django.db import models
    from django.conf import settings
except ImportError:
    raise ImportError(
        "you need to install django or use this in django projects.")

from .utils import encrypt_keys, decrypt_keys
from django.core.exceptions import ValidationError


class HideMyValue(models.CharField):
    description = "A field to save dollars as pennies (int) in db, but act like a float"

    def __init__(self, *args, **kwargs):
        super(HideMyValue, self).__init__(*args, **kwargs)

        self.key = settings.HIDE_MY_VALUE['key']
        self.length = settings.HIDE_MY_VALUE['length']
        self.salt = settings.HIDE_MY_VALUE['salt']

    def get_db_prep_value(self, value, *args, **kwargs):
        if value is None:
            return None
        return encrypt_keys(salt=self.salt, key=self.key, value=value)

    def to_python(self, value):
        if value is None or isinstance(value, str):
            return decrypt_keys(salt=self.salt, key=self.key, value=value)
        try:
            return decrypt_keys(salt=self.salt, key=self.key, value=value)
        except (TypeError, ValueError):
            raise ValidationError(
                "This value must be an integer or a string represents an integer.")

    def from_db_value(self, value, expression, connection, context=None):
        return self.to_python(value)

    def formfield(self, **kwargs):
        from django.forms import CharField
        defaults = {'form_class': CharField}
        defaults.update(kwargs)
        return super(HideMyValue, self).formfield(**defaults)
