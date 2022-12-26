import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

from .errors import MovieNotFound, PosterNotFound
from .headers import HEADERS


def _create_request_with_headers(url):
    return urllib.request.Request(url, headers=HEADERS)


def get_imdb_search_url(title):
    return "https://imdb.com/find/?s=tt&q=" + urllib.parse.quote_plus(title)


def get_imdb_link_from_relative(link):
    return "https://imdb.com" + link


def get_imdb_link_from_id(id):
    return get_imdb_link_from_relative(get_imdb_relative_link_from_id(id))


def get_imdb_relative_link_from_id(id):
    if isinstance(id, str):
        return f"/title/{id}/"
    elif isinstance(id, int):
        return f"/title/tt{id:07}/"
    raise ValueError("id must be int or str")


def get_link_to_title_from_findSection(findSection):
    try:
        relative_link = findSection.table.tr.a["href"]  # /title/ttXXXXXXX
    except AttributeError:
        raise MovieNotFound
    else:
        return get_imdb_link_from_relative(relative_link)


def is_titles_section(section):
    try:
        return section.h3.a["name"] == "tt"
    except AttributeError:
        raise MovieNotFound


def _is_relative_link_to_title(link):
    return link.startswith("/title")


def get_imdb_link_from_response(response):
    soup = BeautifulSoup(response.read(), features="lxml")
    a_tag = soup.find("a", href=_is_relative_link_to_title)
    if not a_tag:
        raise MovieNotFound
    return get_imdb_link_from_relative(a_tag["href"])


def get_imdb_link_from_title(title):
    searchurl = get_imdb_search_url(title)
    with urllib.request.urlopen(_create_request_with_headers(searchurl)) as response:
        try:
            return get_imdb_link_from_response(response)
        except MovieNotFound:
            raise MovieNotFound(f"{title!r} not found on IMDb")


def get_src_of_poster_div(div):
    try:
        return _get_best_src_of_img(div.img)
    except AttributeError:
        raise PosterNotFound


def _get_best_src_of_img(img):
    try:
        srcset = img["srcset"].split(", ")
    except KeyError:
        return img["src"]  # fallback

    best_quality = srcset[-1]
    return best_quality.split(" ")[0]


def get_poster_link_from_response(response):
    soup = BeautifulSoup(response.read(), features="lxml")
    poster_div = soup.find("div", class_="ipc-media")
    return get_src_of_poster_div(poster_div)


def get_poster_from_imdb_link(link):
    try:
        with urllib.request.urlopen(_create_request_with_headers(link)) as response:
            return get_poster_link_from_response(response)
    except urllib.error.HTTPError:
        raise MovieNotFound


def get_poster(title=None, id=None):
    if title is not None:
        imdb_link = get_imdb_link_from_title(title)
    elif id is not None:
        imdb_link = get_imdb_link_from_id(id)
    else:
        raise ValueError("one of [title, id] must be specified")
    try:
        return get_poster_from_imdb_link(imdb_link)
    except PosterNotFound:
        raise PosterNotFound(
            f"{title if title is not None else id!r} doesn't " "have a poster on IMDb"
        )
    except MovieNotFound:
        raise MovieNotFound(
            f"{title if title is not None else id!r} not found" " on IMDb"
        )
