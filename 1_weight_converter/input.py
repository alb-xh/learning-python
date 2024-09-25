class Invalid(Exception):

    def __init__(self, input_name):
      super().__init__(self, 'Invalid input')
      self.input_name = input_name

class Input:

  def __init__ (self, name, validate = None):
    self.name = name
    self.validate = validate

  def get (self, message):
    input_str = input(message)

    if self.validate is not None and self.validate(input_str) is False:
      raise Invalid(self.name)

    return input_str
