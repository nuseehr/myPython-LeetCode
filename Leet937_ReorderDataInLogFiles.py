'''

    2021.04.25, Lee Sun Hong

    Python LeetCode Problem 937.
    (https://leetcode.com/problems/reorder-data-in-log-files/)
    
    -
    -       Reorder Data in Log Files
    -
    
'''

# Lambda와 split함수를 이용한다.
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        
        # 식별자 뒤에 숫자 인지 문자인지 구분해준다.
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # 문자일때는 문제 속 조건을 따라야 하므로 람다식의 key값으로 정렬해준다.
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
        
