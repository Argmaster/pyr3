# -*- coding: utf-8 -*-
from __future__ import annotations
from email.policy import default
from numbers import Number
from PyR3.factory.fields.FieldABC import Field


class Integer(Field):
    def __init__(self, *, default: int = None, value_range: range = None) -> None:
        self.default = default
        self.value_range = value_range

    def digest(self, value: str | Number = None) -> None:
        if value is None:
            return self._get_default()
        else:
            parsed_int = int(value)
            self.check_if_in_range(parsed_int)
            return parsed_int

    def check_if_in_range(self, parsed_int):
        if self.value_range is not None:
            if parsed_int not in self.value_range:
                raise ValueError("Value out of desired value range.")


class Float(Field):
    def __init__(
        self, *, default: float = None, min: float = None, max: float = None
    ) -> None:
        self.default = default
        self.min = min
        self.max = max

    def digest(self, value: str | Number = None) -> None:
        if value is None:
            return self._get_default()
        else:
            parsed_float = float(value)
            self.check_if_in_range(parsed_float)
            return parsed_float

    def check_if_in_range(self, parsed_float):
        if self.min is not None:
            if not (self.min <= parsed_float):
                raise ValueError(f"Value {parsed_float} below expected range. (min: {self.min})")
        if self.max is not None:
            if not (parsed_float <= self.max):
                raise ValueError(f"Value {parsed_float} above expected range. (max: {self.max})")
