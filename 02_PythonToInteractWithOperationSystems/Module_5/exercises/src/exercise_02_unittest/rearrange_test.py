#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

# Clase que contiene los casos de pruebas para la clase rearrange
class TestRearrange(unittest.TestCase):
  
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase), expected)

  def test_double_name(self):
    testcase = "Hopper, Grace M."
    expected = "Grace M. Hopper"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_one_name(self):
    testcase = "Voltaire"
    expected = "Voltaire"
    self.assertEqual(rearrange_name(testcase), expected)

# Para lanzar las pruebas con unittest el archivo Python debe tener la siguiente declaracion: unittest.main()
unittest.main()