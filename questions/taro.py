"""
Problem: Taro's Festival Activities

Description:
Taro has N days of festival. For each of the N days, he can choose to do one of three activities:
A. Swim in the sea and gain a[i] points of happiness.
B. Catch bugs in the mountains and gain b[i] points of happiness.
C. Do crafts at the stalls and gain c[i] points of happiness.

However, Taro gets bored easily and cannot do the same activity for two or more consecutive days. Your task is to determine the maximum possible total points of happiness Taro can gain over the N days while ensuring he doesn't engage in the same activity on consecutive days.

Function Signature:
def taro_festival_happiness(n: int, activities: List[Tuple[int, int, int]]) -> int:

Inputs:
    - n (int): An integer representing the number of festival days. 1 ≤ n ≤ 10^5.
    - activities (List[Tuple[int, int, int]]): A list of tuples, where each tuple contains three integers representing the happiness points Taro gains for swimming, bug-catching, and doing crafts respectively for each day. 1 ≤ a[i], b[i], c[i] ≤ 10^4 for all i.

Returns:
    - int: The maximum possible total points of happiness Taro can gain.

Examples:
1. Input: n = 3, activities = [(6, 7, 8), (8, 8, 3), (2, 5, 7)]
   Output: 23
   Explanation: 
   On day 1, Taro chooses activity C (crafts) and gains 8 points. 
   On day 2, Taro chooses activity A (swimming) and gains 8 points.
   On day 3, Taro chooses activity B (bug-catching) and gains 7 points.
   Total happiness points = 8 + 8 + 7 = 23.

2. Input: n = 2, activities = [(10, 10, 10), (10, 10, 10)]
   Output: 20
   Explanation: 
   Taro can choose any two distinct activities over the two days since all activities offer the same happiness points.

Notes:
    - This problem can be approached using dynamic programming. At each day, based on the activity chosen on the previous day, determine the maximum happiness Taro can gain if he chooses each of the three activities. Update the maximum happiness values for each activity accordingly.

Tags:
    - Dynamic Programming
    - Decision Making
"""

from typing import List, Tuple

def taro_festival_happiness(n: int, activities: List[Tuple[int, int, int]]) -> int:
  return 0
