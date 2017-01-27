# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is 3025 - 385
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import unittest
import math

def difference_between_sum_of_squares_and_square_of_sums(first_n):
    return square_of_sums(first_n) - sum_of_squares(first_n)

def sum_of_squares(first_n):
    sum=0
    for num in range(1,first_n + 1):
        sum += math.pow(num,2)
    return sum

def square_of_sums(first_n):
    sum = 0
    for num in range(1, first_n + 1):
        sum += num
    return math.pow(sum,2)

class difference_between_sum_of_squares_and_square_of_sums_tests(unittest.TestCase):

    def testOne(self):
        self.assertEquals(2640, difference_between_sum_of_squares_and_square_of_sums(10))


def main():
    print('Running script...')
    #unittest.main()
    print(difference_between_sum_of_squares_and_square_of_sums(100))

if __name__ == '__main__':
    print(difference_between_sum_of_squares_and_square_of_sums(100))