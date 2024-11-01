import unittest
import warnings
import sys

sys.path.append("../")
from Code.prediction_scripts.item_based import recommendForNewUser

warnings.filterwarnings("ignore")


class Tests(unittest.TestCase):
    def test_toy_story_recommendation(self):
        movie_list = [{"title": "Toy Story (1995)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Toy Story 3 (2010)", recommendations)

    def test_toy_story_negative_case(self):
        movie_list = [{"title": "Toy Story (1995)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertNotIn("Inception", recommendations)

    def test_kung_fu_panda_recommendation(self):
        movie_list = [{"title": "Kung Fu Panda (2008)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Toy Story (1995)", recommendations)

    def test_kung_fu_panda_negative_case(self):
        movie_list = [{"title": "Kung Fu Panda (2008)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertNotIn("Batman (2001)", recommendations)

    def test_horror_genre_with_cartoon_exclusion(self):
        movie_list = [{"title": "Strangers, The (2008)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertFalse("Toy Story (1995)" in recommendations)

    def test_iron_man_recommendation(self):
        movie_list = [{"title": "Iron Man (2008)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Avengers: Infinity War - Part I (2018)", recommendations)

    def test_robo_cop_recommendation(self):
        movie_list = [{"title": "RoboCop (1987)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("RoboCop 2 (1990)", recommendations)

    def test_nolan_movie_recommendation(self):
        movie_list = [{"title": "Inception (2010)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Dark Knight, The (2008)", recommendations)

    def test_dc_universe_recommendation(self):
        movie_list = [{"title": "Man of Steel (2013)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Batman v Superman: Dawn of Justice (2016)", recommendations)

    def test_armageddon_recommendation(self):
        movie_list = [{"title": "Armageddon (1998)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("2012 (2009)", recommendations)

    def test_lethal_weapon_recommendation(self):
        movie_list = [{"title": "Lethal Weapon (1987)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Lethal Weapon 3 (1992)", recommendations)

    def test_dark_action_movie_recommendation(self):
        movie_list = [{"title": "Batman: The Killing Joke (2016)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Punisher: War Zone (2008)", recommendations)

    def test_dark_movie_recommendation(self):
        movie_list = [{"title": "Puppet Master (1989)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Black Mirror: White Christmas (2014)", recommendations)

    def test_horror_comedy_recommendation(self):
        movie_list = [{"title": "Scary Movie (2000)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("I Sell the Dead (2008)", recommendations)

    def test_superhero_recommendation(self):
        movie_list = [{"title": "Spider-Man (2002)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Iron Man 2 (2010)", recommendations)

    def test_cartoon_movie_recommendation(self):
        movie_list = [{"title": "Moana (2016)", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Monsters, Inc. (2001)", recommendations)

    def test_multiple_movie_recommendation(self):
        movie_list = [
            {"title": "Harry Potter and the Goblet of Fire (2005)", "rating": 5.0},
            {"title": "Twilight Saga: New Moon, The (2009)", "rating": 5.0},
        ]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("Twilight (2008)", recommendations)

    def test_empty_input_handling(self):
        movie_list = []
        recommendations = recommendForNewUser(movie_list)
        self.assertEqual(recommendations, [], "Empty input should yield no recommendations")

    def test_invalid_rating_handling(self):
        movie_list = [{"title": "Toy Story (1995)", "rating": 6.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertEqual(recommendations, [], "Invalid rating should yield no recommendations")

    def test_long_title_handling(self):
        movie_list = [{"title": "T" * 1000, "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertEqual(recommendations, [], "Overly long movie titles should yield no recommendations")

    def test_invalid_title_handling(self):
        movie_list = [{"title": "Invalid Movie", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertEqual(recommendations, [], "Invalid title should yield no recommendations")

    def test_gibberish_title_handling(self):
        movie_list = [{"title": "@#$%^", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertEqual(recommendations, [], "Gibberish titles should yield no recommendations")

    def test_negative_rating_handling(self):
        movie_list = [{"title": "Toy Story (1995)", "rating": -2.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertEqual(recommendations, [], "Negative ratings should yield no recommendations")

    def test_mixed_valid_invalid_ratings(self):
        movie_list = [
            {"title": "Toy Story (1995)", "rating": 5.0},
            {"title": "Inception (2010)", "rating": 6.0},
        ]
        recommendations = recommendForNewUser(movie_list)
        self.assertEqual(recommendations, [], "Mixed valid and invalid ratings should yield no recommendations")

    def test_title_with_whitespace(self):
        movie_list = [{"title": "  Batman (1989) ", "rating": 5.0}]
        recommendations = recommendForNewUser(movie_list)
        self.assertIn("RoboCop (1987)", recommendations)

    def test_none_rating_value(self):
        movie_list = [{"title": "Inception (2010)", "rating": None}]
        recommendations = recommendForNewUser(movie_list)
        self.assertEqual(recommendations, [], "None rating should yield no recommendations")


if __name__ == "__main__":
    unittest.main()
