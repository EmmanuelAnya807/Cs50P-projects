import sys


class Jar:
    def __init__(self, capacity=12):
        # Initialize cookie count to 0 and validate/set capacity
        self._size = 0
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError

    def __str__(self):
        # Return string of cookie emojis equal to current size
        return "🍪" * self._size

    def deposit(self, n):
        # Convert input to integer and ensure non-negative value
        n = int(n)

        if n >= 0:
            # Check if there is enough remaining capacity for the deposit
            jar_space = self._capacity - self._size
            if n <= jar_space:
                self._size += n
            else:
                raise ValueError
        else:
            raise ValueError

    def withdraw(self, n):
        # Convert input to integer and ensure non-negative value
        n = int(n)

        if n >= 0:
            # Check if enough cookies are available to withdraw
            if n <= self._size:
                self._size -= n
            else:
                raise ValueError
        else:
            raise ValueError

    @property
    def capacity(self):
        # Getter for jar capacity
        return self._capacity

    @property
    def size(self):
        # Getter for current cookie count
        return self._size


# Driver code to test Jar functionality
try:
    cookie = Jar()
    print(cookie.capacity)
    print(cookie)
except ValueError:
    sys.exit("Error")
