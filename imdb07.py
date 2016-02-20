import sys
import urllib.request


START_MARKERS = {
    'title': '<h1 class="header"> <span class="itemprop" itemprop="name">',
    'year': '<span class="nobr">(<a href="/year/',
    'genres': '<h4 class="inline">Genres:</h4>',
    'genre': '> '
}


def extract(text, start_marker, end_marker, multiple=False):
    if not multiple:
        start_pos = text.index(start_marker) + len(start_marker)
        end_pos = text.index(end_marker, start_pos + 1)
        value = text[start_pos:end_pos]
    else:
        value = []
        for item in text.split(start_marker)[1:]:
            value.append(item.split(end_marker)[0])
    return value


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: %s imdb_id" % sys.argv[0])
        sys.exit(1)

    imdb_id = sys.argv[1]
    imdb_url = 'http://www.imdb.com/title/tt' + imdb_id
    with urllib.request.urlopen(imdb_url) as html_file:
        html = html_file.read().decode('utf-8')

    title = extract(html, START_MARKERS['title'], end_marker='<')
    print(title)

    year = extract(html, START_MARKERS['year'], end_marker='/')
    print(year)

    genres_html = extract(html, START_MARKERS['genres'], end_marker='</div>')
    genres = extract(genres_html, START_MARKERS['genre'], end_marker='<', multiple=True)
    print(genres)
