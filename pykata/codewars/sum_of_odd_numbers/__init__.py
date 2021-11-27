"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
"""

# First number in each row is the sum of n-1 even numbers plus 1
# 2 + 4 + ... + 2(n-1) + 1 = (n-1)n + 1
first_number = lambda n: n*(n-1) + 1

def row_sum_odd_numbers(n):
    """
    
    Math:
    ========
    First number in each row is:

    x := first_number = sum of (n-1) even numbers plus 1 =
       = 2 + 4 + ... + 2(n-1) + 1 = 2(1 + 2 + ... + (n-1) ) + 1 =
       = 2(n-1)n/2 + 1 = (n-1)n + 1

    Sum of numbers on row n is sum of n odd numbers starting with x:
    s := sum_row_n = x + (x + 2) + (x + 4) + ... (x + 2(n-1)) = 
       = nx + 2(1 + 2 + ... + (n-1)) =
       = nx + 2(n-1)n/2 = nx + (n-1)n

    Substitute first number in row x:
    s = n(n-1)n + n + n*n - n = n*n*n

    >>> row_sum_odd_numbers(1)
    1
    
    >>> row_sum_odd_numbers(2)
    8

    >>> row_sum_odd_numbers(13)
    2197
    
    >>> row_sum_odd_numbers(19)
    6859
    
    >>> row_sum_odd_numbers(41)
    68921
    """
    x = first_number(n)
    # Sum on row n is sum of n odd numbers, starting with the first number on the row
    # s = x + (x+2) + (x+2*2) + ... (x+2(n-1)) = nx + 2(1 + 2 + ... + (n-1)) =
    #   = nx + (n-1)n
    return n*x + n*(n-1)

if __name__ == "__main__": # pragma: no cover
    import doctest
    doctest.testmod()
