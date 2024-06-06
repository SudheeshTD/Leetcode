class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = []
        for i in s:
            if(90>=ord(i)>=65 or 122>=ord(i)>=97 or 48<=ord(i)<=57):
                news.append(i)
        r = len(news)
        new2 = []
        new2[:] = news[::-1]
        for i in range(r):
            if news[i].lower() != new2[i].lower():
                return False
        return True

        