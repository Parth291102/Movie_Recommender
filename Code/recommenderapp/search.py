import pandas as pd
import os
import sys
sys.path.append("../../")

class Search:

    # Update the path to movies_metadata.csv and use 'original_title' column
    app_dir = os.path.dirname(os.path.abspath(__file__))
    code_dir = os.path.dirname(app_dir)
    project_dir = os.path.dirname(code_dir)

    # Load the updated dataset and specify 'original_title' as the column to use
    df = pd.read_csv(project_dir + "/Code/text_based_approach/movies_metadata.csv", low_memory=False)

    def __init__(self):
        pass

    def startsWith(self, word):
        n = len(word)
        res = []
        word = word.lower()
        # Use 'original_title' instead of 'title'
        for x in self.df["original_title"]:
            curr = str(x).lower()  # Convert to string to avoid issues with missing values
            if curr[:n] == word:
                res.append(x)
        return res

    def anywhere(self, word, visitedWords):
        res = []
        word = word.lower()
        # Use 'original_title' instead of 'title'
        for x in self.df["original_title"]:
            if x not in visitedWords:
                curr = str(x).lower()  # Convert to string to avoid issues with missing values
                if word in curr:
                    res.append(x)
        return res

    def results(self, word):
        startsWith = self.startsWith(word)
        visitedWords = set()
        for x in startsWith:
            visitedWords.add(x)
        anywhere = self.anywhere(word, visitedWords)
        startsWith.extend(anywhere)
        return startsWith

    def resultsTop10(self, word):
        return self.results(word)[:10]
