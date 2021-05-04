class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # print(ord('Z'))
        # print(ord('Z')-ord('A'))

        # we need to track the length of the letters that are max only 2 different
        # the maximum length to be returned

        # so whenever we meet other letter we will decrease the LIMITATION K
        # if the letter is different than the right pointer we reset the leftpointer value
        # and update with new
        # if only 2 letters exists in the Subarray we can take into consideration the length of the subarray

        # 1) Make a list of chars

        char_list = [0] * 26
        # we need count of MAX letter so we keep track of the max operation per letter, to not exceed > K

        count_letters = 0
        max_length = 0

        left = 0

        # s = "AABABBA", k = 1

        for right in range(0, len(s), 1):

            letterR = ord(s[right]) - ord('A')
            # print("letterR", s[right], " ", letterR)
            char_list[letterR] += 1

            # keep track of max_count letter, to comapre with K, highest repeting
            count_letters = max(count_letters, char_list[letterR])

            # sliding window - MAX REPETEAD character, must be < k,
            # as sliding window - max repeated = number of possible changes
            # ABBBC, k = 2, count = 3, k = 2

            while right - left - count_letters + 1 > k:
                # print("count_letters", count_letters)
                letterL = ord(s[left]) - ord('A')
                char_list[letterL] -= 1
                left += 1

            # print("right", right, "left", left)
            length = right - left + 1
            max_length = max(max_length, length)

        return max_length

        """
        char_list = [0] * 26        
        count_letters = 0
        max_length = 0
        left = 0

        for right in range(0, len(s), 1):

            letterR = ord(s[right]) - ord('A')
            char_list[letterR] += 1

            #keep track of max_count letter, to comapre with K, highest repeting 
            count_letters = max(count_letters, char_list[letterR])

            # sliding window - MAX REPETEAD character, must be < k, 
            # as sliding window - max repeated = number of possible changes 

            while right - left - count_letters + 1 > k:

                letterL = ord(s[left]) - ord('A')
                char_list[letterL] -= 1
                left += 1

            length = right - left + 1
            max_length = max(max_length, length)

        return max_length 


        """