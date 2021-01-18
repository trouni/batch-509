import requests

def fetch_lyrics(artist, track):
    url = f"https://orion.apiseeds.com/api/music/lyric/{artist}/{track}/"
    api_key = 'Um9e4VJFhfKvFdch8iQwENVi4F2n4nylFgKfhjiTMa08XCiO9SVywXGFyEEUd6xb'
    response = requests.get(url, params={'apikey': api_key})
    if response.status_code != 200:
        return ''
    return response.json()['result']['track']['text']

if __name__ == '__main__':
    print(fetch_lyrics('Dshinghis Khan', 'Moskau'))