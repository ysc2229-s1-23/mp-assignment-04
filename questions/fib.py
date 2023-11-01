"""
Problem: Fibonacci Sequence with O(n)

Description:
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1. Your task is to find the nth Fibonacci number. However, the challenge is to find this in O(n) time complexity.

Function Signature:
def fibonacci(n: int) -> int:

Inputs:
    - n (int): An integer n where 0 <= n <= 10^5, representing the position in the Fibonacci sequence.

Returns:
    - int: The nth Fibonacci number.

Examples:
1. Input: 0
   Output: 0
   Explanation: 
   The Fibonacci sequence starts with 0.

2. Input: 1
   Output: 1
   Explanation: 
   The second number in the Fibonacci sequence is 1.

3. Input: 10
   Output: 55
   Explanation:
   The sequence starts as: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. Thus, the 10th Fibonacci number is 55.

4. Input: 7
   Output: 13
   Explanation:
   The sequence starts as: 0, 1, 1, 2, 3, 5, 8, 13. Thus, the 7th Fibonacci number is 13.

Notes:
    - While the Fibonacci sequence can be solved using various methods such as matrix exponentiation or using Binet's formula, the objective of this problem is to implement it using a simple iterative approach to achieve O(n) time complexity.
    - Start by initializing two variables representing the two preceding numbers and use them to compute the next number in the sequence iteratively.

Tags:
    - Dynamic Programming
    - Iteration
"""

def fibonacci(n: int) -> int:
  return 0