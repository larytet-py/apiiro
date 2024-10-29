# PYTHONPATH=. pytest
import pytest
from koogle import Koogle, get_top_scores, SubstringIterator

@pytest.fixture
def koogle_instance():
    return Koogle()

def test_get_top_scores():
    scores = {"a": 2, "b": 3, "c": 1}
    top_scores = get_top_scores(scores, 2)
    assert top_scores == [("b", 3), ("a", 2)]  # "b" should be the top score

def test_suggest(koogle_instance):
    iterator = SubstringIterator("apple")
    for prefix in iterator:
        koogle_instance.suggest(prefix)

    assert koogle_instance.score == {"a": 1, "ap": 1, "app": 1, "appl": 1, "apple": 1}
    assert koogle_instance.lookup == {
        "a": {"a", "ap", "app", "appl", "apple"},
        "ap": {"ap", "app", "appl", "apple"},
        "app": {"app", "appl", "apple"},
        "appl": {"appl", "apple"},
        "apple": {"apple"}
    }

def test_search(koogle_instance):
    iterator = SubstringIterator("apple")
    for prefix in iterator:
        koogle_instance.suggest(prefix)

    iterator = SubstringIterator("app")
    for prefix in iterator:
        koogle_instance.suggest(prefix)

    res = koogle_instance.search("app", 1)
    assert res == [('app', 2)]
