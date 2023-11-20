class Solution(object):
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = strs[0]
        for st in strs:
            for ind, ch in enumerate(res):
                try:
                    if ch != st[ind]:
                        res = st[:ind]
                        break
                except IndexError:
                    res = st
                    break
        return res


print(Solution.longestCommonPrefix(["dogovorische","dog","dogvor"]))
