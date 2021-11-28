# -*- coding: utf-8 -*-
from __future__ import annotations

import importlib
from pathlib import Path

import yaml

from PyR3.factory.MeshFactory import MeshFactory
from PyR3.shortcut.context import wipeScenes
from PyR3.shortcut.io import export_to


def import_factory(class_: str):
    """Imports factory class from module.

    :param class_: python import name in form <python_module_import_path>.class
    :type class_: str
    :raises TypeError: Raised if requested class is not descendant of MeshFactory.
    """
    module_name, class_name = class_.rsplit(".", 1)
    module = importlib.import_module(module_name)
    class_object = getattr(module, class_name)
    if not issubclass(class_object, MeshFactory):
        raise TypeError(
            f"Requested class '{class_name}' is not a MeshFactory."
        )
    return class_object


def build_from_file(src_file: Path, save_path: Path):
    """Build mesh using configuration from file. Later mesh is saved to
    save_path.

    :param src_file: source configuration file.
    :type src_file: Path
    :param save_path: destination save path.
    :type save_path: Path
    """
    with src_file.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    build_and_save(
        data.get("type", "python").lower(),
        data["class"],
        data["params"],
        save_path,
    )


def build_and_save(
    generator_type: str,
    class_: str | MeshFactory,
    params: dict,
    save_path: Path,
):
    if generator_type == "python":
        build_python(class_, params)
    else:
        raise RuntimeError(
            f"Unknown generator type '{generator_type}' selected."
        )
    export_to(filepath=save_path)


def build_python(class_: str | MeshFactory, params: dict):
    wipeScenes()
    if isinstance(class_, str):
        class_ = import_factory(class_)
    class_(params).render()
