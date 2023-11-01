"""
Problem: Longest Common Segment

Description:
You are given two strings `s` and `t`. Your task is to find and return the longest segment that is present in both `s` and `t`.

A segment of a string is obtained by removing zero or more characters from the string and concatenating the remaining characters without changing their order.

Function Signature:
def longest_common_segment(s: str, t: str) -> str:

Inputs:
    - s (str): A string consisting of lowercase English letters.
    - t (str): A string consisting of lowercase English letters.

Returns:
    - str: The longest segment that appears in both `s` and `t`.

Examples:
1. Input: s = "abcdef", t = "acef"
   Output: "acef"
   Explanation: 
   The longest common segment is "acef" which appears in its entirety in both strings.

2. Input: s = "abcdef", t = "azc"
   Output: "ac"
   Explanation: 
   The segments "ac", "az", "af", and "cf" are common between the two strings. Among these, "ac" is the longest.

Notes:
    - This problem can be approached using dynamic programming. Let `dp[i][j]` represent the length of the longest common segment of the first `i` characters of `s` and the first `j` characters of `t`. The transition formula is:
        - dp[i][j] = dp[i-1][j-1] + 1, if s[i] == t[j]
        - dp[i][j] = max(dp[i-1][j], dp[i][j-1]), otherwise
    - Once the dp table is built, you can backtrack from `dp[len(s)][len(t)]` to construct the longest common segment.

Tags:
    - Dynamic Programming
"""

def longest_common_segment(s: str, t: str) -> str:
  return "alan was here"
