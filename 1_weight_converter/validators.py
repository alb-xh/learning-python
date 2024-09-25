class String:

  @staticmethod
  def is_int(string):

    try:
      int(string)
      return True

    except ValueError:
      return False

  @staticmethod
  def isOneOf (string, strings):
    return string in strings
