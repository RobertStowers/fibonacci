# fibonacci
Working with the Fibonacci Sequence
F(n) = 1, 1, 2, 3, 5, 8, 13, ...<br>
Where, F(n) = F(n-1) + F(n-2)

Goal: create a script, fib_sum.py, to sum a given number of terms in the Fibonacci Sequence.
Sum of Fibonacci Numbers, S(n) = 1 + 1 + 2 + 3 + ... + F(n)

Inputs<br>
    num_to_sum: number of Fibonacci Numbers to sum
    
Outputs<br>
    returns the sum of the first "num_to_sum" numbers in the Fibonacci Sequence

Function<br>
    Makes use of direct solution: S(n) = F(n+2) - 1<br>
    example: S(4) = 1 + 1 + 2 + 3 = 7 = F(4+2) - 1 = F(6) - 1 = 8 - 1 = 7
