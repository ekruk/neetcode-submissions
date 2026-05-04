class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        for c in s1:
            if dic.get(c) is None:
                dic[c] = 1
            else:
                dic[c] +=1

        compare = {}
        left_window = 0

        for i in range(len(s2)):
            
            if compare.get(s2[i]) is None:
                compare[s2[i]] = 1
            else:
                compare[s2[i]] += 1

            if i >= len(s1) - 1:
                if compare == dic:
                    return True 
                else:
                    if compare[s2[left_window]] > 1:
                        compare[s2[left_window]] -= 1
                    else:
                        del compare[s2[left_window]]
                    left_window += 1
        return False


         