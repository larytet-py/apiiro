import pytest


@pytest.fixture
def koogle_instance():
    return koogle.Koogle()

def test_get_top_scores():
    scores = {"a": 2, "b": 3, "c": 1}
    top_scores = koogle.get_top_scores(scores, 2)
    assert top_scores == [("b", 3), ("a", 2)]  # "b" should be the top score

def test_update_new_prefix(koogle_instance):
    koogle_instance.update("apple")
    assert koogle_instance.score == {"a": 1, "ap": 1, "app": 1, "appl": 1, "apple": 1}
    assert koogle_instance.lookup == {
        "a": ["a"],
        "ap": ["ap"],
        "app": ["app"],
        "appl": ["appl"],
        "apple": ["apple"]
    }

def test_update_existing_prefix(koogle_instance):
    koogle_instance.update("apple")
    koogle_instance.update("apricot")
    assert koogle_instance.score["a"] == 2
    assert koogle_instance.lookup["a"] == ["a", "a"]  # Should have "a" from both words

def test_suggest_empty_lookup(koogle_instance):
    suggestions = koogle_instance.suggest("a", 3)
    assert suggestions == []

def test_suggest_with_one_prefix(koogle_instance):
    koogle_instance.update("banana")
    koogle_instance.update("bandana")
    suggestions = koogle_instance.suggest("ba", 2)
    assert suggestions == [("ba", 2)]  # "ba" has 2 occurrences

def test_suggest_multiple_matches(koogle_instance):
    koogle_instance.update("cherry")
    koogle_instance.update("cherry")
    koogle_instance.update("chocolate")
    suggestions = koogle_instance.suggest("ch", 2)
    assert suggestions == [("ch", 3)]  # "ch" should have 3 occurrences
