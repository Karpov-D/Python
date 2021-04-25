from itertools import count
from itertools import cycle

my_count = count(7)

for _ in range(10):
    print((next(my_count)))

my_cycle = cycle("abc")

for _ in range(10):
    print((next(my_cycle)))