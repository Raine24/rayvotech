import re
with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'\s*<a href="[^"]+" class="btn btn-primary" style="margin-top: 1.5rem; display: inline-block; width: 100%; text-align: center;">View Case Study</a>', '', html)
with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed residual text.")
