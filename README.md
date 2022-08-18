## movieposters

A simple Python package to get the link a movie's poster given its title.

## Installation

Installation has been made easy with PyPI. Depending on your system, you should either run

```pip install movieposters```

or

```pip3 install movieposters```

to install **movieposters**.

## How to use
See the example below:
```python
import movieposters as mp
link = mp.get_poster(title='breakfast club')
assert link == mp.get_poster(id='tt0088847')  # can also be found using movie's id
assert link == mp.get_poster(id=88847)
assert link == 'https://m.media-amazon.com/images/M/MV5BOTM5N2ZmZTMtNjlmOS00YzlkLTk3YjEtNTU1ZmQ5OTdhODZhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg'
```

#### Movies not on IMDb
If **movieposters** is *unable* to find the title on IMDb an `mp.errors.MovieNotFound` exception will be raised.

#### Movies without posters
If **movieposters** is *able* to find the title on IMDb but can't find its poster an `mp.errors.PosterNotFound` exception will be raised.
