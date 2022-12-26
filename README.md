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
assert link == 'https://m.media-amazon.com/images/M/MV5BOTM5N2ZmZTMtNjlmOS00YzlkLTk3YjEtNTU1ZmQ5OTdhODZhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL75_UX380_CR0,16,380,562_.jpg'
```

### Errors

| Name                       | Meaning                                      |
|----------------------------|----------------------------------------------|
| `mp.errors.MovieNotFound`  | Movie _**is not**_ on IMDb                   |
| `mp.errors.PosterNotFound` | Movie _**is**_ on IMDb, but its poster isn't |