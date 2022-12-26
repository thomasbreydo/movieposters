import movieposters as mp


def test_get_poster_friends():
    link = mp.get_poster(title="friends")
    print(link)


def test_get_poster_breakfast_club():
    link = mp.get_poster(title="breakfast club")
    assert link == mp.get_poster(id="tt0088847")
    assert link == mp.get_poster(id=88847)
    print(link)
