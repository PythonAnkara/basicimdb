import sys
import urllib.request


MARKERS = {
    'title': ('<h1 class="header"> <span class="itemprop" itemprop="name">', '<'),
    'year': ('<span class="nobr">(<a href="/year/', '/'),
    'genres': ('<h4 class="inline">Genres:</h4>', '</div>'),
    'genre': ('> ', '<'),
    'languages': ('<h4 class="inline">Language:</h4>', '</div>'),
    'language': ("itemprop='url'>", '<'),
    'actors': ('<h2>Cast</h2>', '</table>'),
    'actor': (' itemprop="name">', '<')
}

KEYS = {'title', 'year', 'genres', 'languages', 'actors'}

SECONDARY_KEYS = {
    'genres': 'genre',
    'languages': 'language',
    'actors': 'actor'
}


def extract(text, start_marker, end_marker):
    return [item.split(end_marker)[0]
            for item in text.split(start_marker)[1:]]


def get_property(text, first, second=None):
    value = extract(text, *MARKERS[first])[0]
    if second is not None:
        value = extract(value, *MARKERS[second])
    return value


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: %s imdb_id" % sys.argv[0])
        sys.exit(1)

    imdb_id = sys.argv[1]
    imdb_url = 'http://www.imdb.com/title/tt' + imdb_id
    with urllib.request.urlopen(imdb_url) as html_file:
        html = html_file.read().decode('utf-8')

    data = {k: get_property(html, k, SECONDARY_KEYS.get(k)) for k in KEYS}
    print(data)
