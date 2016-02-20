import sys

if len(sys.argv) < 2:
    print("Usage: %s html_file" % sys.argv[0])
    sys.exit(1)

html_file_name = sys.argv[1]
html_file = open(html_file_name)
html = html_file.read()

title_start_marker = '<h1 class="header"> <span class="itemprop" itemprop="name">'
title_end_marker = '<'
title_start_pos = html.index(title_start_marker) + len(title_start_marker)
title_end_pos = html.index(title_end_marker, title_start_pos + 1)
title = html[title_start_pos:title_end_pos]
print(title)

year_start_marker = '<span class="nobr">(<a href="/year/'
year_end_marker = '/'
year_start_pos = html.index(year_start_marker) + len(year_start_marker)
year_end_pos = html.index(year_end_marker, year_start_pos + 1)
year = html[year_start_pos:year_end_pos]
print(year)

genres_start_marker = '<h4 class="inline">Genres:</h4>'
genres_end_marker = '</div>'
genres_start_pos = html.index(genres_start_marker) + len(genres_start_marker)
genres_end_pos = html.index(genres_end_marker, genres_start_pos + 1)
genres_html = html[genres_start_pos:genres_end_pos]
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
