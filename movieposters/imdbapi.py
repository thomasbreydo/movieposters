import urllib
from bs4 import BeautifulSoup


class MovieNotFound(Exception):
    pass


class PosterNotFound(Exception):
    pass


def construct_imdb_search_url(title):
    return 'https://imdb.com/find?q=' + urllib.parse.quote_plus(title)


def get_link_to_title_from_findSection(findSection):
    try:
        relative_link = findSection.table.tr.a['href']  # /title/ttXXXXXXX
    except AttributeError:
        raise MovieNotFound
    else:
        return 'https://imdb.com' + relative_link


def is_titles_section(section):
    try:
        return section.h3.a['name'] == 'tt'
    except AttributeError:
        raise MovieNotFound


def get_imdb_link_from_response(response):
    soup = BeautifulSoup(response.read(), features='lxml')
    for section in soup.find_all('div', class_='findSection'):
        if is_titles_section(section):
            return get_link_to_title_from_findSection(section)
    raise MovieNotFound


def get_imdb_link_of_title(title):
    searchurl = construct_imdb_search_url(title)
    with urllib.request.urlopen(searchurl) as response:
        try:
            return get_imdb_link_from_response(response)
        except MovieNotFound:
            raise MovieNotFound(f'{title!r} not found on IMDb')


def get_src_of_poster_div(div):
    try:
        return div.a.img['src']
    except AttributeError:
        raise PosterNotFound


def get_poster_link_from_response(response):
    soup = BeautifulSoup(response.read(), features='lxml')
    poster_div = soup.find('div', class_='poster')
    return get_src_of_poster_div(poster_div)


def get_poster_of_imdb_link(link):
    with urllib.request.urlopen(link) as response:
        return get_poster_link_from_response(response)


def get_link_to_poster(title):
    imdb_link = get_imdb_link_of_title(title)
    try:
        return get_poster_of_imdb_link(imdb_link)
    except PosterNotFound:
        raise PosterNotFound(f"{title!r} doesn't have a poster on IMDb")
