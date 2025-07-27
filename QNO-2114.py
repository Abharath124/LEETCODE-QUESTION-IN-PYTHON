class Solution(object):
    def mostWordsFound(self, sentences):
        return max(len(i.split()) for i in sentences)