#!/usr/bin/env python3

import unittest

from validate_user import validate_user

class TestValidateUser(unittest.TestCase):
  
  # Prueba que valida que el usuario enviado cumple con las validaciones
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  # Prueba que valida que el usuario enviado NO cumple con las validaciones
  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)

  # Prueba que valida que el usuario enviado NO cumple con las validaciones
  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)
  
  # Prueba que valida que el usuario enviado y el minlen lanza una excepcion de tipo ValueError
  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user, "user", -1)

  # Prueba que valida que el usuario no es de tipo string y una excepcion de tipo AssertionError
  def test_invalid_username_not_string(self):
    self.assertRaises(AssertionError, validate_user, [3], 1)


# Ejecutar la prueba
unittest.main()
