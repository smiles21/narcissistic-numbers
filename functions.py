import math

def sum_of_factorials(numbers):
  """
  Sums the factorial of each digit in digits

  Ex: sum_of_factorials([2, 3, 4]) = 2! + 3! + 4! = 32
  """
  return sum(math.factorial(number) for number in numbers)


def sum_of_self_exponential(numbers):
  """
  Sums each digit raised to the power of itself

  Ex: sum_of_self_exponential([2, 3, 4]) = 2^2 + 3^3 + 4^4 = 287
  """
  return sum(pow(number, number) for number in numbers)


def sum_of_powers(numbers, power):
  """
  Sums each number raised to power

  Ex: sum_of_powers([2, 3, 4], 2) = 2^2 + 3^2 + 4^2 = 29
  """ 
  return sum(pow(number, power) for number in numbers)


def sum_of_exponents(numbers, powers):
  """
  Sums each number raised to the power in the same index powers

  Ex: sum_of_exponents([2, 3, 4], [1, 2, 3]) = 2^1 + 3^2 + 4^3 = 75
  """
  return sum(pow(number, power) for (number, power) in zip(numbers, powers))


if __name__ == '__main__':
  print('Running functions tests')

  assert(sum_of_factorials([1]) == 1)
  assert(sum_of_factorials([1, 2, 3]) == 9)
  assert(sum_of_factorials([5, 6, 7]) == 5880)

  assert(sum_of_self_exponential([1]) == 1)
  assert(sum_of_self_exponential([1, 2, 3]) == 32)
  assert(sum_of_self_exponential([5, 6, 7]) == 873324)

  assert(sum_of_powers([1], 2) == 1)
  assert(sum_of_powers([1, 2, 3], 2) == 14)
  assert(sum_of_powers([5, 6, 7], 3) == 684)

  assert(sum_of_exponents([1], [1]) == 1)
  assert(sum_of_exponents([2, 3, 4], [1, 2, 3]) == 75)
  assert(sum_of_exponents([5, 6, 7], [6, 7, 8]) == 6060362)

  print('All functions tests passed')
