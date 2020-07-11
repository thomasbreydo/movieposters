# movieposters

A simple Python package to get the link a movie's poster given its title.

# Installation

Installation has been made easy with PyPI. Depending on your system, you should either run

```pip install movieposters```

or

```pip3 install movieposters```

to install **movieposters**.

# How to use
See the example below:
```python
>>> import movieposters as mp
>>> link = mp.get_link_to_poster('breakfast club')  # it's a long link
>>> pprint.pprint((link[:50], 
...                link[50:100],
...                link[100:]))
('https://m.media-amazon.com/images/M/MV5BOTM5N2ZmZT',
 'MtNjlmOS00YzlkLTk3YjEtNTU1ZmQ5OTdhODZhXkEyXkFqcGde',
 'QXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg')
```

## Movies not on IMDb
If **movieposters** is *unable* to find the title on IMDb a `MovieNotFound` exception will be raised.

## Movies without posters
If **movieposters** is *able* to find the title on IMDb but can't find its poster a `PosterNotFound` exception will be raised.