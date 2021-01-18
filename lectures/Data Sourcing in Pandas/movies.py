import re
import requests
from bs4 import BeautifulSoup

def fetch_all_pages():
    pass

def fetch_page(page):
    """
    Fetch a result page from the TOP 250 from IMDB
    """
    response = requests.get(
        "https://www.imdb.com/search/title/",
        params={"groups":"top_250", "sort":"user_rating","start": (1 + page * 50)},
        headers={"Accept-Language":"en-US"})
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def parse_movies(soup):
    """
    Parse movie information
    """
    movies = []
    for movie in soup.find_all("div", class_="lister-item-content"):
        title = movie.find("h3").find("a").string
        duration = int(movie.find(class_="runtime").string.strip(' min'))
        year = int(re.search(r"\d{4}", movie.find(class_="lister-item-year").string).group(0))
        movies.append({'title': title, 'duration': duration, 'year': year})
    return movies