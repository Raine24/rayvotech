import os, glob
files = glob.glob('*.html')
for f in files:
    if f == 'pricing.html': continue
    with open(f, 'r', encoding='utf-8') as file: content = file.read()
    content = content.replace('<a href="portfolio.html">Portfolio</a>\n                <a href="contact.html">Contact</a>', '<a href="portfolio.html">Portfolio</a>\n                <a href="pricing.html">Pricing</a>\n                <a href="contact.html">Contact</a>')
    content = content.replace('<a href="portfolio.html">Our Work</a>\n                        <a href="contact.html">Contact</a>', '<a href="portfolio.html">Our Work</a>\n                        <a href="pricing.html">Pricing</a>\n                        <a href="contact.html">Contact</a>')
    with open(f, 'w', encoding='utf-8') as file: file.write(content)
print('Updated navigation globally.')
