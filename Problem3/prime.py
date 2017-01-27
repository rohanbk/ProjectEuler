# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import unittest

# Determine largest prime factor
def prime_factors(input):

    """Returns all the prime factors of a positive integer"""
    factors = []
    factor = 2
    while input > 1:
        while input % factor == 0:
            factors.append(factor)
            input /= factor
        factor += 1
        if factor*factor > input:
            if input > 1: factors.append(input)
            break
    return factors[-1]


# Here's our "unit tests".
class largestPrimeFactorTests(unittest.TestCase):

    def testOne(self):
        self.assertEquals(29, prime_factors(13195))

    def testTwo(self):
        self.assertEquals(3, prime_factors(18))


def main():
    #unittest.main()
    n = 18
    print 'The largest prime factor of ', n, ' is ', prime_factors(n)
    n = 100
    print 'The largest prime factor of ', n, ' is ', prime_factors(n)


if __name__ == '__main__':
    main()
