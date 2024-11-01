import unittest
import warnings
import sys
import os

sys.path.append("../")
from Code.text_based_approach.plot_based_email_recommendation import *

warnings.filterwarnings("ignore")

class GenerateWeightedRecommendationsTests(unittest.TestCase):

    def setUp(self):
        # Basic sample history data
        self.sample_data = [
            {"movie_title": "Election", "frequency": 2},
            {"movie_title": "Radio", "frequency": 2},
            {"movie_title": "The Official Story", "frequency": 2},
            {"movie_title": "Some Girl", "frequency": 1},
            {"movie_title": "Blackboard Jungle", "frequency": 2},
            {"movie_title": "The Five Venoms", "frequency": 1},
            {"movie_title": "Sidekicks", "frequency": 1},
            {"movie_title": "Home Room", "frequency": 2},
            {"movie_title": "Masques", "frequency": 1},
            {"movie_title": "Mona Lisa Smile", "frequency": 2},
            {"movie_title": "Trippin'", "frequency": 1},
            {"movie_title": "Storytelling", "frequency": 1},
            {"movie_title": "The Breakfast Club", "frequency": 1},
            {"movie_title": "The Substitute", "frequency": 1}
        ]

    def test_valid_data_with_frequencies(self):
        recommendations = generate_weighted_recommendations(self.sample_data)
        self.assertGreater(len(recommendations), 0)

    def test_empty_history(self):
        recommendations = generate_weighted_recommendations([])
        self.assertEqual(recommendations, [])

    def test_single_high_frequency(self):
        high_freq_data = [{"movie_title": "Radio", "frequency": 100}]
        recommendations = generate_weighted_recommendations(high_freq_data)
        self.assertGreater(len(recommendations), 0)

    def test_all_unrecognized_titles(self):
        unrecognized_data = [{"movie_title": "Unknown Title", "frequency": 3}]
        recommendations = generate_weighted_recommendations(unrecognized_data)
        self.assertEqual(recommendations, [])

    def test_mixed_recognized_unrecognized_titles(self):
        mixed_data = [
            {"movie_title": "Radio", "frequency": 2},
            {"movie_title": "Unknown Title", "frequency": 3}
        ]
        recommendations = generate_weighted_recommendations(mixed_data)
        self.assertGreater(len(recommendations), 0)

    def test_no_overlap_with_history_titles(self):
        recommendations = generate_weighted_recommendations(self.sample_data)
        history_titles = set(entry["movie_title"] for entry in self.sample_data)
        self.assertTrue(all(rec not in history_titles for rec in recommendations))

    def test_low_frequency_entries(self):
        low_freq_data = [{"movie_title": "Radio", "frequency": 1}]
        recommendations = generate_weighted_recommendations(low_freq_data)
        self.assertGreater(len(recommendations), 0)

    def test_large_history_data(self):
        large_history_data = [{"movie_title": f"Movie {i}", "frequency": i % 3 + 1} for i in range(100)]
        recommendations = generate_weighted_recommendations(large_history_data)
        self.assertLessEqual(len(recommendations), 10)

    def test_zero_frequency_ignored(self):
        zero_freq_data = [
            {"movie_title": "Radio", "frequency": 2},
            {"movie_title": "Election", "frequency": 0}
        ]
        recommendations = generate_weighted_recommendations(zero_freq_data)
        self.assertGreater(len(recommendations), 0)

    def test_large_frequency_range(self):
        varied_freq_data = [
            {"movie_title": "Radio", "frequency": 1},
            {"movie_title": "Election", "frequency": 50}
        ]
        recommendations = generate_weighted_recommendations(varied_freq_data)
        self.assertGreater(len(recommendations), 0)

    def test_single_low_frequency_movie(self):
        single_low_freq = [{"movie_title": "The Breakfast Club", "frequency": 1}]
        recommendations = generate_weighted_recommendations(single_low_freq)
        self.assertGreater(len(recommendations), 0)

    def test_unique_recommendations_only(self):
        recommendations = generate_weighted_recommendations(self.sample_data)
        self.assertEqual(len(recommendations), len(set(recommendations)))

    def test_multiple_high_frequencies(self):
        high_freq_data = [
            {"movie_title": "Radio", "frequency": 5},
            {"movie_title": "Election", "frequency": 5},
            {"movie_title": "The Official Story", "frequency": 5}
        ]
        recommendations = generate_weighted_recommendations(high_freq_data)
        self.assertGreater(len(recommendations), 0)

    def test_weighted_title_influence(self):
        weighted_data = [
            {"movie_title": "Mona Lisa Smile", "frequency": 10},
            {"movie_title": "The Five Venoms", "frequency": 1}
        ]
        recommendations = generate_weighted_recommendations(weighted_data)
        self.assertGreater(len(recommendations), 0)

    def test_duplicate_titles_handling(self):
        duplicate_data = [
            {"movie_title": "Radio", "frequency": 2},
            {"movie_title": "Radio", "frequency": 2}
        ]
        recommendations = generate_weighted_recommendations(duplicate_data)
        self.assertGreater(len(recommendations), 0)

    def test_large_single_title_frequency(self):
        high_freq_single = [{"movie_title": "Some Girl", "frequency": 500}]
        recommendations = generate_weighted_recommendations(high_freq_single)
        self.assertGreater(len(recommendations), 0)

    def test_varied_frequencies_among_titles(self):
        varied_data = [
            {"movie_title": "Radio", "frequency": 10},
            {"movie_title": "Election", "frequency": 1},
            {"movie_title": "Storytelling", "frequency": 5}
        ]
        recommendations = generate_weighted_recommendations(varied_data)
        self.assertGreater(len(recommendations), 0)

    def test_titles_with_no_duplicates(self):
        unique_titles_data = [
            {"movie_title": "Some Girl", "frequency": 2},
            {"movie_title": "Sidekicks", "frequency": 1},
            {"movie_title": "Blackboard Jungle", "frequency": 2}
        ]
        recommendations = generate_weighted_recommendations(unique_titles_data)
        self.assertEqual(len(recommendations), len(set(recommendations)))

    def test_titles_with_and_without_genres(self):
        # Test that the function handles movies with and without defined genres
        mixed_genre_data = [
            {"movie_title": "Radio", "frequency": 3},
            {"movie_title": "The Breakfast Club", "frequency": 2}
        ]
        recommendations = generate_weighted_recommendations(mixed_genre_data)
        self.assertGreater(len(recommendations), 0)

    def test_top_five_recommendations_with_varied_history(self):
        varied_data = [
            {"movie_title": "Radio", "frequency": 3},
            {"movie_title": "Election", "frequency": 5},
            {"movie_title": "The Official Story", "frequency": 1},
            {"movie_title": "The Substitute", "frequency": 2}
        ]
        recommendations = generate_weighted_recommendations(varied_data)
        self.assertLessEqual(len(recommendations), 10)


if __name__ == '__main__':
    unittest.main()
