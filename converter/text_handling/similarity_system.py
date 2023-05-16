#from ..models import Word
import numpy as np
from eimegem.converter import models



class Similarity(): 
    """
    This script uses the Levenshtein distance algorithm to compute 
    the minimum number of edits (insertions, deletions, or substitutions)
    required to transform one string into another. The similarity score 
    is then calculated as 1 minus the normalized distance divided by the maximum
    length of the input strings.
    """

    def levenshtein_distance(self, w1, w2):
        m, n = len(w1), len(w2)
        dp = np.zeros((m + 1, n + 1))

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if w1[i - 1] == w2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

        return dp[m][n]

    def meansure_similarity(self, w1, w2):
        distance = Similarity().levenshtein_distance(w1, w2)
        similarity = 1 - (distance / max(len(w1), len(w2)))
        return similarity



class Database:
    all_elements_object = models.Word.objects.all()



class text_handling():
    def __init__(self, text: str):
        self.original_text = text
        self.processed_text = []
        self.all_words = Database.all_elements_object

    def split_text(self):
        self.processed_text = self.original_text.split(' ')

    def is_valid_word(self, word: str):
        word_score = Similarity().meansure_similarity(w1=word)

        # In production...
    
    




    