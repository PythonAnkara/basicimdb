import sys


def extract(text, start_marker, end_marker):
    start_pos = text.index(start_marker) + len(start_marker)
    end_pos = text.index(end_marker, start_pos + 1)
    value = text[start_pos:end_pos]
    return value


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: %s html_file" % sys.argv[0])
        sys.exit(1)

    html_file_name = sys.argv[1]
    html_file = open(html_file_name)
    html = html_file.read()

    title = extract(html, '<h1 class="header"> <span class="itemprop" itemprop="name">', '<')
    print(title)

    year = extract(html, '<span class="nobr">(<a href="/year/', '/')
    print(year)

    genres_html = extract(html, '<h4 class="inline">Genres:</h4>', '</div>')
    genre_start_marker = '> '
    genre_end_marker = '<'
    last_pos = 0
    genres = []
    while True:
        try:
            genre_start_pos = genres_html.index(genre_start_marker, last_pos) + len(genre_start_marker)
            genre_end_pos = genres_html.index(genre_end_marker, genre_start_pos + 1)
            genre = genres_html[genre_start_pos:genre_end_pos]
            genres.append(genre)
            last_pos = genre_end_pos + 1
        except ValueError:
            break
    print(genres)

    html_file.close()
