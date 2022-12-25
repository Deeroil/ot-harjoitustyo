import unittest
from repository.highscore_repository import highscore_repository

class TestHighscoreRepository(unittest.TestCase):
    def setUp(self):
        highscore_repository.delete_all()
        self.user1 = "Alph"
        self.user2 = "Betty"

    def test_create_score(self):
        highscore_repository.add(self.user1, 10)
        scores = highscore_repository.find_all()

        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0][1], 10)
        self.assertEqual(scores[0][0], "Alph")

    def test_find_all_right_order_with_two(self):
        highscore_repository.add(self.user1, 1)
        highscore_repository.add(self.user2, 10)
        scores = highscore_repository.find_all()

        self.assertEqual(len(scores), 2)
        self.assertEqual(scores[0][0], "Betty")
        self.assertEqual(scores[0][1], 10)

    def test_find_top_3_right_order_with_two(self):
        highscore_repository.add(self.user1, 1)
        highscore_repository.add(self.user2, 10)
        scores = highscore_repository.find_top_3()

        self.assertEqual(len(scores), 2)
        self.assertEqual(scores[0][0], "Betty")
        self.assertEqual(scores[0][1], 10)
