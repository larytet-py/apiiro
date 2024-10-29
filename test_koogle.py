import unittest
from . import koogle

class TestKoogle(unittest.TestCase):
    def setUp(self):
        self.koogle = koogle.Koogle()

    def test_update_new_prefix(self):
        self.koogle.update("apple")
        self.assertEqual(self.koogle.score, {"a": 1, "ap": 1, "app": 1, "appl": 1, "apple": 1})
        self.assertEqual(self.koogle.lookup, {
            "a": ["a"],
            "ap": ["ap"],
            "app": ["app"],
            "appl": ["appl"],
            "apple": ["apple"]
        })

    def test_update_existing_prefix(self):
        self.koogle.update("apple")
        self.koogle.update("apricot")
        self.assertEqual(self.koogle.score["a"], 2)
        self.assertEqual(self.koogle.lookup["a"], ["a", "a"])  # Should have "a" from both words

    def test_suggest_empty_lookup(self):
        suggestions = self.koogle.suggest("a", 3)
        self.assertEqual(suggestions, [])

    def test_suggest_with_one_prefix(self):
        self.koogle.update("banana")
        self.koogle.update("bandana")
        suggestions = self.koogle.suggest("ba", 2)
        self.assertEqual(suggestions, [("ba", 2)])  # "ba" has 2 occurrences

    def test_get_top_scores(self):
        scores = {"a": 2, "b": 3, "c": 1}
        top_scores = koogle.get_top_scores(scores, 2)
        self.assertEqual(top_scores, [("b", 3), ("a", 2)])  # "b" should be the top score

    def test_suggest_multiple_matches(self):
        self.koogle.update("cherry")
        self.koogle.update("cherry")
        self.koogle.update("chocolate")
        suggestions = self.koogle.suggest("ch", 2)
        self.assertEqual(suggestions, [("ch", 3)])  # "ch" should have 3 occurrences

if __name__ == "__main__":
    unittest.main()