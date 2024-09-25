from enum import Enum

class InvalidUnit(Exception):

  def __init__ (self, unit):
    super().__init__(self, 'Invalid unit')
    self.unit = unit


class Unit(Enum):
  KILOGRAM = 'K'
  POUND = 'L'

  @staticmethod
  def get (unit_str):
    for unit in Unit:
      if unit_str == unit.value:
        return unit

    raise InvalidUnit(unit)


class ConversionRate:

  rates = {
    Unit.KILOGRAM: 1,
    Unit.POUND: 2.20462,
  }

  @staticmethod
  def get (from_unit, to_unit):

    if from_unit not in ConversionRate.rates:
      raise InvalidUnit(from_unit)

    if to_unit not in ConversionRate.rates:
      raise InvalidUnit(to_unit)

    return ConversionRate.rates[to_unit] / ConversionRate.rates[from_unit]

class Converter:

  @staticmethod
  def convert (amount, from_unit, to_unit):
    return amount * ConversionRate.get(from_unit, to_unit)
