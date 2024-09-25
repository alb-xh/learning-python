from input import Input, Invalid as InvalidInput
from validators import String as StringValidator
from mass import Converter as MassConverter, Unit as MassUnit, InvalidUnit as InvalidMassUnit

def main():
  weight_input = Input('weight', StringValidator.is_int)
  weight_unit_input = Input(
    'weight_unit_input',
    lambda string : StringValidator.isOneOf(string.upper(), [ MassUnit.KILOGRAM.value, MassUnit.POUND.value ])
  )

  try:
    weight_str = weight_input.get('Weight: ')
    weight_unit_str = weight_unit_input.get('(K)g or (L)bs: ')

    weight = int(weight_str)
    from_weight_unit = MassUnit.get(weight_unit_str.upper())
    to_weight_unit = MassUnit.KILOGRAM if from_weight_unit == MassUnit.POUND else MassUnit.POUND
    converted_weight = MassConverter.convert(weight, from_weight_unit, to_weight_unit)

    print(converted_weight, to_weight_unit.value)

  except InvalidInput as err:
    print('Invalid input:', err.input_name)

  except InvalidMassUnit as err:
    print('Invalid mass unit:', err.unit)

main()
