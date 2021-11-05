# -*- coding: utf-8 -*-
from enum import Enum


class EXIT_CODE(Enum):
    COMPONENT_WITH_SYMBOL_EXISTS = 345
    MESHPROJECT_FILE_NOT_FOUND = 346
    MESHPROJECT_INVALID_FIELD_VALUE = 347
    MESHPROJECT_FILE_INVALID_YAML_SYNTAX = 348
    FILE_EXISTS = 349
