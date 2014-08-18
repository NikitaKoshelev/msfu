from BeautifulSoup import BeautifulSoup

doc = open('base.html', 'r').readlines()

soup = BeautifulSoup(''.join(doc))
parse = open('parse.html', 'w')
parse.write(u'{0}'.format(soup.prettify()))
print(soup.prettify())
parse.close()