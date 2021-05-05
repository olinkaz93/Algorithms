# https://www.youtube.com/watch?v=K1ps6d7YCy4
    def longestCommonPrefix(self, strs):

        if (len(strs)) == 0:
            return ""
        if (len(strs)) == 1:
            return (strs[0])

        ### HORIZONTAL SCAN

        prefix = strs[0]
        # the idea is to cut the string as the other word does not begin with it
        for i in range(1, len(strs), 1):
            while strs[i].startswith(prefix) == False:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""


        return prefix

        ### VERTICAL SCAN (TOP DOWN)
    def longestCommonPrefix(self, strs):

        if (len(strs)) == 0:
            return ""
        if (len(strs)) == 1:
            return (strs[0])

        prefix = strs[0]

        # the idea is to scan index by index, of the letters
        # check the first index of every single word, and third

        for i in range (0, len(prefix), 1):
            # we scan to the very end of index, but we still cut the prefixes
            char = prefix[i]
            for j in range (1, len(strs), 1): #word in strs
                #we scan every index from the PREFIX through the letters
                #once we find the MISMATCH character , or we reach the end of the word
                #we return the cutted word, until this moment of mismatch
                if (i == len(strs[j]) or char != strs[j][i]):#" o != l "
                    return strs[j][:i]

        return prefix


"""