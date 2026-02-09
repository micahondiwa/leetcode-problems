def isPalindrome(s):
    """
    :type s: str
     :rtype: bool
     """
    cleaned = [char.lower() for char in s if char.isalnum()]

    low, high = 0, len(cleaned)-1
    while low <= high:
         if cleaned[low] != cleaned[high]:
            return False
         low += 1
         high -= 1
    return True
# Example
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))