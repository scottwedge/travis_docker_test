#!/usr/bin/env python3

import unittest
import script

class TestScript(unittest.TestCase):
  def test_hello(self):
    self.assertEqual(script.say_hello("Vadim"), "Hello, Vadim")
    
if __name__ == '__main__':
  unittest.main()
