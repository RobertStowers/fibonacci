import time

"""
Sum Fibonacci Numbers

Fibonacci Sequence = 1, 1, 2, 3, 5, 8, 13, ...
Fibonacci Sequence = f0, f1, f2, f3, ...
F(n) represents the nth Fibonacci Number
Sum First n Fibonacci Numbers, S(n) = f0 + f1 + ... + fn
"""


# Recursion: Original approach, but > 1.0 sec when num_to_sum >= 32
def sum_fibs_recursion(num_to_sum):
    if num_to_sum == 1 or num_to_sum == 0:
        return 1
    else:
        return sum_fibs_recursion(num_to_sum - 1) + sum_fibs_recursion(num_to_sum - 2)


GOLDEN_RATIO = (1 + 5 ** 0.5) / 2


# Direct Solution
def sum_fibs(num_to_sum):
    """
    Direct Solution: S(n) = F(n+2) - 1
    e.g. S(4) = 1 + 1 + 2 + 3 = 7 = F(4+2) - 1 = F(6) - 1 = 8 - 1 = 7
    F(n) = ROUND( 1/(5**0.5) * GOLDEN_RATIO ** (n + 1) )

    :param num_to_sum: number Fibonacci Numbers to sum
    :return: sum of the first "num_to_sum" Fibonacci Numbers
    """
    return round((GOLDEN_RATIO ** (num_to_sum + 2 + 1)) / (5 ** 0.5)) - 1


start_time = time.time()
fibs_to_sum = 10  # Work for 100, 1000, 10000, and 100000
print("Fibonacci numbers to sum: %i" % fibs_to_sum)
fib_total = sum_fibs(fibs_to_sum)
print("Time: %f" % (time.time() - start_time))
print("Sum = %i" % fib_total)
