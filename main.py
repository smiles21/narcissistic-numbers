from digit_functions import get_adjacent_digits, get_digits
from functions import sum_of_factorials, sum_of_self_exponential, sum_of_powers

if __name__ == '__main__':
  for adjacent in range(2, 5):
    for exponent in range(2, 10):
      for i in range(2, 1000000):
        numbers = get_adjacent_digits(i, adjacent)
        if sum_of_powers(numbers, exponent) == i:
          print(i, 'exponent:', exponent, 'adjacenct:', adjacent)
