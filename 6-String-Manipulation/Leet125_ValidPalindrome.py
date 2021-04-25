'''

    2021.04.25, Lee Sun Hong

    Python LeetCode Problem 125.
    (https://leetcode.com/problems/valid-palindrome/)
    
    -
    -       Valid Palindrome
    -
    
'''

# list로 변환 후 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 주어진 문자열을 담을 list를 선언.
        str = []
        for char in s:
            # isalnum 함수는 주어진 문자열이 알파벳으로 이루어져있는지 판별할 수 있다.
            if char.isalnum():
                str.append(char.lower())
        
        # list의 앞 뒤 요소를 꺼내 비교한다.
        while len(str) > 1:
            if str.pop(0) != str.pop():
                return False
        
        return True
