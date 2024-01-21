#!/usr/bin/env python3

# Arrange
import pytest
from fruit import Fruit
from fruit_salad import FruitSalad


@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]

def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)
    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
    
# Para lanzar las pruebas con pytest, se debe ingresar el comando por consola: pytest
# Una ventaja de pytest es que este puede descubrir y ejecturar automaticamente pruebas