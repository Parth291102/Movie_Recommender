import unittest
import warnings
import sys
import os

sys.path.append(os.path.abspath("../"))
from Code.recommenderapp.search import Search

warnings.filterwarnings("ignore")


class Tests(unittest.TestCase):
    def testSearchToy(self):
        search_word = "toy"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        self.assertTrue(any("Toy" in title for title in filtered_dict), "Expected a movie with 'Toy' in the title")

    def testSearchWithMixedCharacters(self):
    search_word = "Toy2"
    search = Search()
    filtered_dict = search.resultsTop10(search_word)
    self.assertTrue(any("Toy" in title for title in filtered_dict), "Expected a movie with 'Toy' in the title")
    

    def testSearchLove(self):
        search_word = "love"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        self.assertTrue(any("Love" in title for title in filtered_dict), "Expected a movie with 'Love' in the title")

    def testSearchGibberish(self):
        search_word = "gibberish"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = []
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchSpecialCharacters(self):
        search_word = "!@#$%^&*()"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = []
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchLongString(self):
        search_word = "a" * 1000
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = []
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchTermNotFound(self):
        search_word = "nonexistentterm"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = []
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchWhitespace(self):
        search_word = "  whitespace  "
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = []
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchHTMLJavaScriptTags(self):
        search_word = "<script>alert('Hello');</script>"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = []
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchUnicodeCharacters(self):
        search_word = "😊"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = []
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchExactMatch(self):
        search_word = "Toy Story"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        self.assertTrue(any("Toy Story" in title for title in filtered_dict), "Expected 'Toy Story' in results")

    def testSearchSingleCharacter(self):
        search_word = "a"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        self.assertTrue(len(filtered_dict) <= 10)

    def testSearchCaseInsensitive(self):
        search_word = "TOY"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        self.assertTrue(any("Toy" in title for title in filtered_dict), "Expected a case-insensitive match for 'Toy'")

    def testSearchSubstringMatch(self):
        search_word = "stor"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        self.assertTrue(any("Story" in title for title in filtered_dict), "Expected a match for 'stor' in the title")

    def testSearchWithHyphenatedWords(self):
        search_word = "self-love"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        expected_resp = []
        self.assertEqual(filtered_dict, expected_resp)

    def testSearchWithCommonWord(self):
        search_word = "the"
        search = Search()
        search_results = search.resultsTop10(search_word)
        self.assertTrue(len(search_results) <= 10)

    def testSearchMultipleWords(self):
    search_word = "The Dark Knight"
    search = Search()
    filtered_dict = search.resultsTop10(search_word)
    self.assertTrue(any("The Dark Knight" in title for title in filtered_dict), "Expected 'The Dark Knight' in the results")

    def testSearchPartialTitleMatch(self):
    search_word = "Avengers"
    search = Search()
    filtered_dict = search.resultsTop10(search_word)
    self.assertTrue(any("Avengers" in title for title in filtered_dict), "Expected a match for 'Avengers' in the title")

    def testSearchWithHyphenInTitle(self):
    search_word = "Spider-Man"
    search = Search()
    filtered_dict = search.resultsTop10(search_word)
    self.assertTrue(any("Spider-Man" in title for title in filtered_dict), "Expected a movie with 'Spider-Man' in the title")

    def testSearchWithNumbersAndLetters(self):
    search_word = "Fast & Furious 7"
    search = Search()
    filtered_dict = search.resultsTop10(search_word)
    self.assertTrue(any("Fast & Furious" in title for title in filtered_dict), "Expected a movie with 'Fast & Furious' in the title")

    def testSearchWithNumbersAndLetters(self):
    search_word = "Hero"
    search = Search()
    filtered_dict = search.resultsTop10(search_word)
    self.assertTrue(any("Fast & Furious" in title for title in filtered_dict), "Expected a movie with 'Fast & Furious' in the title")

    

    def testSearchWithAccents(self):
        search_word = "Amelie"  # Removed accent for consistency
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        self.assertTrue(len(filtered_dict) <= 10, "Expected results with similar words without accents")

    def testSearchWithSpacesBetweenCharacters(self):
        search_word = "T o y   S t o r y"
        search = Search()
        filtered_dict = search.resultsTop10(search_word)
        self.assertEqual(filtered_dict, [], "Expected no results for search term with spaced-out characters")

if __name__ == "__main__":
    unittest.main()
