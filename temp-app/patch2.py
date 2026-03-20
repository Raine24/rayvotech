import os, glob
files = glob.glob('*.html')
for f in files:
    if f == 'faqs.html': continue
    with open(f, 'r', encoding='utf-8') as file: content = file.read()
    content = content.replace('<a href="pricing.html">Pricing</a>', '<a href="pricing.html">Pricing</a>\n                        <a href="faqs.html">FAQs</a>')
    with open(f, 'w', encoding='utf-8') as file: file.write(content)
print('Patched FAQs link into footer.')
