class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        """
        1) aaa - each letter is one permutation
        2) palindrome - the same word at the back to front - and front to back
        3) we can see that if we have SAME letters, we have additional permutation
        3) what if we count letters in substrings and check while adding if we have the eqivalent ?
        4) "aaa": so this one is a palindrome, since "a" is a palindrome, than "aa" is palindrome
        because its letter is the same a the [0] letter, than "aaa" is palindrome because 
        [-1] is the same like [0]
        so not only we got extra 3size palindrome, but also, since the other conditions are valid we 
        increment them +1 as well
        
        1) letter itself is palindorme
        2) the [-1] = [0]
        3) every time we get new letter we check conditions, 
        4) when we find FALSE value/condition. very virst letter we stop the current count
        
        'aabbaabbcc'
        a is pal - 1
        aa is pal - 1 + (previous) = 2
        b[-1] != a[0] - pal 1
        
         
         left_pointer
         right_pointer
         
         
        
        """
        """
        We perform a "center expansion" among all possible centers of the palindrome.

        Let N = len(S). There are 2N-1 possible centers for the palindrome: we could have a center at S[0], between S[0] and S[1], at S[1], between S[1] and S[2], at S[2], etc.

        To iterate over each of the 2N-1 centers, we will move the left pointer every 2 times, and the right pointer every 2 times starting with the second (index 1). Hence, left = center / 2, right = center / 2 + center % 2.

        From here, finding every palindrome starting with that center is straightforward: while the ends are valid and have equal characters, record the answer and expand.
        """
        
        """
        ans = 0
        for i in range(len(s)):
            for j in range(2):
                left = i
                right = left + j

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    ans += 1
                    left -= 1
                    right += 1
        return ans
        """
        
        """
        Algorithm

        We choose all possible centers for potential palindromes:

        Every single character in the string is a center for possible odd-length palindromes
        Every pair of consecutive characters in the string is a center for possible even-length palindromes.
        For every center, we can expand around it as long as we get palindromes (i.e. the first and last characters should match).
        """
        N = len(s)
        count = 0
        for i in range(N):
            for j in [i, i + 1]:
                i, j = start_left, start_right
                while left >= 0 and right < N and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
        
        return count