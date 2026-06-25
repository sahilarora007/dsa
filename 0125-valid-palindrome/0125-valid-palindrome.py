class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        reverse = clean_text[::-1]
        if clean_text == reverse:
            return True
        else:
            return False