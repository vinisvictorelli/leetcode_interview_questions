def longestCommonPrefix(strs):
        prefix = ""
        for i in range(1,len(strs)):
            if strs[i][i-1] == strs[i-1][i-1] and strs[i-1][i-1] not in prefix:
                prefix += strs[i][i-1]
            else:
                 break
        print(prefix)
longestCommonPrefix(["dog","racecar","car"])
longestCommonPrefix(["flower","flow","flight"])