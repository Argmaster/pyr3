# -*- coding: utf-8 -*-
from __future__ import annotations

from unittest import TestCase
from unittest import main

from PyR3.shortcut.context import Objects
from PyR3.shortcut.context import wipeScenes
from PyR3.shortcut.edit import Edit
from PyR3.shortcut.io import export_to
from PyR3.shortcut.mesh import addCube
from PyR3.shortcut.mesh import fromPyData
from PyR3.shortcut.mesh import join


class TestMeshModule(TestCase):
    def test_fromPyData(self):
        wipeScenes()
        obj = fromPyData(
            [(0, 0, 0), (0, 1, 1), (0, 3, 0)], [(0, 1), (1, 2), (2, 0)], [(0, 1, 2)]
        )
        with Edit(obj) as edit:
            self.assertEqual(len(edit.vertices()), 3)
            self.assertEqual(len(edit.edges()), 3)
            self.assertEqual(len(edit.faces()), 1)
        export_to(filepath="./tests/.temp/fromPyData.blend")

    def test_join(self):
        wipeScenes()
        o1 = addCube()
        o2 = addCube()
        join(o1, o2)
        self.assertEqual(len(Objects.all()), 1)


if __name__ == "__main__":
    main()
