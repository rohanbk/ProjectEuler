# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import unittest


# Determine smallest_positive_multiple
def smallest_positive_multiple(lower, upper):

    answer = 1

    while True:
        checker = 1
        for i in range(lower,upper):
            if answer%i == 0:
                checker += 1
        if checker == upper:
            break
        else:
            answer += 1
    return answer

# Here's our "unit tests".
class smallest_positive_multiple_tests(unittest.TestCase):

    def testOne(self):
        self.assertEquals(2520, smallest_positive_multiple(1, 10))


def main():
    print('Running script...')
    #unittest.main()

    print(smallest_positive_multiple(1,20))

if __name__ == '__main__':
    main()
