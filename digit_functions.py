def get_adjacent_digits(n, tuple_length):
  """
  Returns a list of numbers where each numbre is the tuple_length
  group of adjacent digits

  Ex: get_adjacent_digits(2345, 2) => [23, 34, 45] 
  Ex: get_adjacent_digits(2345, 1) => [1, 2, 3, 4]
  """
  result = []
  limit = (10 ** (tuple_length - 1)) - 1
  divisor = int(10 ** tuple_length)
  while n > limit:
    remainder = n % divisor
    result.insert(0, remainder)
    n //= 10
  return result

def get_digits(n):
  """
  Returns a list of containing the digits of n
  """
  return get_adjacent_digits(n, 1)


if __name__ == '__main__':
  print('Running digit_functions tests')

  assert(get_digits(1) == [1])
  assert(get_digits(1234) == [1, 2, 3, 4])
  assert(get_digits(1010101) == [1, 0, 1, 0, 1, 0, 1])

  assert(get_adjacent_digits(1, 1) == [1])
  assert(get_adjacent_digits(2345, 2) == [23, 34, 45])
  assert(get_adjacent_digits(1, 2) == [])
  assert(get_adjacent_digits(100, 2) == [10, 0])
  assert(get_adjacent_digits(1001, 3) == [100, 1])
  assert(get_adjacent_digits(23456, 3) == [234, 345, 456])

  print('All digit_functions tests passed')

