"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.val = start - 1
        self.start = start - 1

    def generate(self):
        if self.val:
            self.val += 1
        return self.val

    def reset(self):
        self.val = self.start


serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())
