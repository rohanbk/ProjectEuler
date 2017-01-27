import unittest


def phoneCall(min1, min2_10, min11, money):
    time = 0

    if money - min1 >= 0:
        time += 1
        money -= min1

    while money - min2_10 >= 0 and time < 10:
        time += 1
        money -= min2_10

    while money - min11 >= 0 and time >= 10:
        time += 1
        money -= min11

    return time

class phoneCallTests(unittest.TestCase):

    def testOne(self):
        self.assertEquals(14,phoneCall(3,1,2,20))

    def testTwo(self):
        self.assertEquals(1, phoneCall(2, 2, 1, 2))

    def testThree(self):
        self.assertEquals(11, phoneCall(10,1,2,22))

    def testFour(self):
        self.assertEquals(14, phoneCall(2,2,1,24))

    def testFive(self):
        self.assertEquals(3, phoneCall(1, 2, 1, 6))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
