html_file = open('matrix.html')
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

html_file.close()
