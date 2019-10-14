# #!/usr/bin/env python3
# encoding: utf-8
# mspac (c) 2019 MIT License <baltasarq@gmail.com>


import unittest

from mspac import mspac_tool


class TestMspac(unittest.TestCase):
    def test_autoremove(self):
        self.assertEqual(0, mspac_tool.autoremove())
        
    def test_upgrade(self):
        self.assertEqual(0, mspac_tool.upgrade(True))
        self.assertEqual(0, mspac_tool.upgrade(False))
        
    def test_install(self):
        self.assertEqual(0, mspac_tool.install(["pacman"], True))
        self.assertEqual(0, mspac_tool.install(["pacman"], False))
        
    def test_show(self):
        self.assertEqual(0, mspac_tool.show(["pacman"]))
                         
    def test_list(self):
        self.assertEqual(0, mspac_tool.lists(["pacman"]))


if __name__ == "__main__":
    unittest.main()
