import pytest
import movieposters as mp


def test_get_poster():
    link = mp.get_poster(title="breakfast club")
    assert link == mp.get_poster(id="tt0088847")
    assert link == mp.get_poster(id=88847)
    print(link)
