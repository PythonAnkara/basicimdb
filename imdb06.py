import sys
import urllib.request


START_MARKERS = {
    'title': '<h1 class="header"> <span class="itemprop" itemprop="name">',
    'year': '<span class="nobr">(<a href="/year/',
    'genres': '<h4 class="inline">Genres:</h4>',
    'genre': '> '
}


def extract(text, start_marker, end_marker, last_pos=0):
    start_pos = text.index(start_marker, last_pos) + len(start_marker)
    end_pos = text.index(end_marker, start_pos + 1)
    value = text[start_pos:end_pos]
    return value, end_pos + 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        # print("Usage: %s html_file" % sys.argv[0])
        print("Usage: %s imdb_id" % sys.argv[0])
        sys.exit(1)

    # html_file_name = sys.argv[1]
    # with open(html_file_name) as html_file:
    #     html = html_file.read()

    imdb_id = sys.argv[1]
    imdb_url = 'http://www.imdb.com/title/tt' + imdb_id
    with urllib.request.urlopen(imdb_url) as html_file:
        html = html_file.read().decode('utf-8')

    title, _ = extract(html, START_MARKERS['title'], end_marker='<')
    print(title)

    year, _ = extract(html, START_MARKERS['year'], end_marker='/')
    print(year)

    genres_html, _ = extract(html, START_MARKERS['genres'], end_marker='</div>')
    genres = []
    last_pos = 0
    while True:
        try:
            genre, last_pos = extract(genres_html, START_MARKERS['genre'],
                                      end_marker='<', last_pos=last_pos)
            genres.append(genre)
        except ValueError:
            break
    print(genres)

    html_file.close()
