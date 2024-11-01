import unittest
from unittest.mock import patch
import pandas as pd
import sys

sys.path.append("../")
from Code.prediction_scripts.item_based import recommendForNewUser

class RecommendForNewUserTests(unittest.TestCase):
    
    def setUp(self):
        # Mock data for movies and ratings to simulate the environment
        self.mock_movies = pd.DataFrame({
            "movieId": [1, 2, 3],
            "title": ["Toy Story", "Jumanji", "Grumpier Old Men"],
            "genres": ["Animation|Children|Comedy", "Adventure|Children|Fantasy", "Comedy|Romance"]
        })
        self.mock_ratings = pd.DataFrame({
            "userId": [1, 2, 3],
            "movieId": [1, 2, 3],
            "rating": [4.0, 5.0, 4.5]
        })

        # Patch `pd.read_csv` to replace it with our mock data
        patcher = patch("Code.prediction_scripts.item_based.pd.read_csv")
        self.addCleanup(patcher.stop)
        self.mock_read_csv = patcher.start()
        self.mock_read_csv.side_effect = [self.mock_ratings, self.mock_movies]

        # Sample valid input ratings
        self.valid_user_ratings = [
            {"title": "Toy Story", "rating": 4.5},
            {"title": "Jumanji", "rating": 5.0},
            {"title": "Grumpier Old Men", "rating": 4.0}
        ]

    def test_valid_recommendations(self):
        recommendations = recommendForNewUser(self.valid_user_ratings)
        self.assertGreater(len(recommendations), 0, "Expected recommendations for valid inputs")

    def test_empty_input(self):
        recommendations = recommendForNewUser([])
        self.assertEqual(recommendations, [], "Expected empty recommendations for empty input list")

    def test_invalid_ratings(self):
        invalid_ratings = [{"title": "Toy Story", "rating": -1}]
        recommendations = recommendForNewUser(invalid_ratings)
        self.assertEqual(recommendations, [], "Expected empty recommendations for invalid ratings")

    def test_recommendation_titles_are_strings(self):
        recommendations = recommendForNewUser(self.valid_user_ratings)
        self.assertTrue(all(isinstance(title, str) for title in recommendations), "Expected all recommendation titles to be strings")

    def test_too_long_title(self):
        long_title_ratings = [{"title": "A" * 256, "rating": 4.5}]
        recommendations = recommendForNewUser(long_title_ratings)
        self.assertEqual(recommendations, [], "Expected empty recommendations for a title exceeding max length")

    def test_unrecognized_title(self):
        unknown_ratings = [{"title": "Unknown Movie", "rating": 3.0}]
        recommendations = recommendForNewUser(unknown_ratings)
        self.assertEqual(recommendations, [], "Expected empty recommendations for unrecognized title")

    def test_multiple_invalid_titles(self):
        invalid_titles = [{"title": "Unknown1", "rating": 3}, {"title": "Unknown2", "rating": 4}]
        recommendations = recommendForNewUser(invalid_titles)
        self.assertEqual(recommendations, [], "Expected empty recommendations for multiple invalid titles")

    def test_rating_edge_value(self):
        edge_ratings = [{"title": "Toy Story", "rating": 5.0}]
        recommendations = recommendForNewUser(edge_ratings)
        self.assertGreater(len(recommendations), 0, "Expected recommendations for valid edge rating at max limit")

    def test_mixed_valid_invalid_ratings(self):
        mixed_ratings = [{"title": "Toy Story", "rating": 4}, {"title": "Unknown", "rating": 3}]
        recommendations = recommendForNewUser(mixed_ratings)
        self.assertGreater(len(recommendations), 0, "Expected recommendations for input with mixed valid and invalid titles")

    def test_null_rating(self):
        null_rating = [{"title": "Toy Story", "rating": None}]
        recommendations = recommendForNewUser(null_rating)
        self.assertEqual(recommendations, [], "Expected empty recommendations when rating is null")

    def test_nonstandard_genres(self):
        self.mock_movies['genres'] = ["Genre1|@#$%", "Genre2", "Genre3"]
        recommendations = recommendForNewUser(self.valid_user_ratings)
        self.assertGreater(len(recommendations), 0, "Expected recommendations despite nonstandard genres")

    def test_output_is_list(self):
        recommendations = recommendForNewUser(self.valid_user_ratings)
        self.assertIsInstance(recommendations, list, "Expected recommendations output to be a list")

    def test_low_ratings(self):
        low_ratings = [{"title": "Toy Story", "rating": 1.0}]
        recommendations = recommendForNewUser(low_ratings)
        self.assertGreater(len(recommendations), 0, "Expected recommendations for valid low ratings")

    def test_high_ratings_below_max(self):
        high_ratings = [{"title": "Jumanji", "rating": 4.9}]
        recommendations = recommendForNewUser(high_ratings)
        self.assertGreater(len(recommendations), 0, "Expected recommendations for valid high ratings below max")

    def test_empty_genres(self):
        self.mock_movies['genres'] = ["", "", ""]
        recommendations = recommendForNewUser(self.valid_user_ratings)
        self.assertGreater(len(recommendations), 0, "Expected recommendations for movies with empty genres")

    def test_same_rating_all_movies(self):
        same_rating = [{"title": "Toy Story", "rating": 4}, {"title": "Jumanji", "rating": 4}, {"title": "Grumpier Old Men", "rating": 4}]
        recommendations = recommendForNewUser(same_rating)
        self.assertGreater(len(recommendations), 0, "Expected recommendations when all movies have the same rating")

    def test_single_movie_rating(self):
        single_rating = [{"title": "Toy Story", "rating": 4.0}]
        recommendations = recommendForNewUser(single_rating)
        self.assertGreater(len(recommendations), 0, "Expected recommendations with a single valid movie rating")

    def test_special_character_in_title(self):
        special_char_ratings = [{"title": "Toy Story! @#$%^&*()", "rating": 4}]
        recommendations = recommendForNewUser(special_char_ratings)
        self.assertEqual(recommendations, [], "Expected empty recommendations for titles with special characters")

    def test_varied_genres(self):
        varied_genres_ratings = [{"title": "Toy Story", "rating": 4.0}, {"title": "Grumpier Old Men", "rating": 4.0}]
        recommendations = recommendForNewUser(varied_genres_ratings)
        self.assertGreater(len(recommendations), 0, "Expected recommendations for input with varied genres")

if __name__ == '__main__':
    unittest.main()
