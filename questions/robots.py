"""
Problem: Robot Jump

Description:
There are N platforms, each with a specific height. A robot starts at the first platform and aims to reach the Nth platform. The robot can jump from the ith platform to either the (i+1)th platform or the (i+2)th platform. The cost of jumping from the ith platform to the jth platform is the absolute difference in their heights, |heights[i] - heights[j]|. Your task is to find the minimum possible total cost for the robot to reach the Nth platform.

Function Signature:
def robot_jump(n: int, heights: List[int]) -> int:

Inputs:
    - n (int): An integer representing the number of platforms. 2 ≤ n ≤ 10^5.
    - heights (List[int]): A list of integers representing the heights of the platforms. 1 ≤ heights[i] ≤ 10^4 for all i.

Returns:
    - int: The minimum possible total cost incurred for the robot to reach the Nth platform.

Examples:
1. Input: n = 2, heights = [10, 30]
   Output: 20
   Explanation: 
   The robot will jump from the 1st platform to the 2nd platform directly, incurring a cost of |10-30| = 20.

2. Input: n = 4, heights = [10, 30, 40, 20]
   Output: 30
   Explanation: 
   The robot jumps from the 1st platform to the 2nd platform with a cost of 20. Then, it jumps to the 4th platform with a cost of 10, totaling a cost of 30.

3. Input: n = 5, heights = [10, 30, 10, 20, 20]
   Output: 20
   Explanation:
   The robot jumps from the 1st platform to the 3rd platform with a cost of 20. Then, it jumps to the 5th platform with no additional cost.

Notes:
    - This problem can be approached using dynamic programming. The idea is to maintain an array of costs where the ith entry represents the minimum cost to reach the ith platform.
    - For each platform, consider the cost of jumping from the previous platform and the one before that, and take the minimum of the two.

Tags:
    - Dynamic Programming
    - Greedy
"""

from typing import List

def robot_jump(n: int, heights: List[int]) -> int:
  return 0
