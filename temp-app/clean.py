import os
import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the double/ugly View Case Study buttons
ugly_btn_pattern = r'\n\s*<a href="[^"]+" class="btn btn-primary" style="margin-top: 1.5rem; display: inline-block; width: 100%; text-align: center;">View Case Study</a>'
html = re.sub(ugly_btn_pattern, '', html)

# 2. Remove Tibico Health
parts = re.split(r'(<!-- Project \d+ -->)', html)

new_parts = []
skip_next = False
for i in range(len(parts)):
    if skip_next:
        skip_next = False
        continue
        
    # If this is the project marker AND the next part contains Tibico Health, we skip both
    if parts[i].startswith('<!-- Project') and i + 1 < len(parts) and 'Tibico Health' in parts[i+1]:
        skip_next = True
        continue
        
    new_parts.append(parts[i])

html = "".join(new_parts)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Delete the file
if os.path.exists('portfolio-tibico-health.html'):
    os.remove('portfolio-tibico-health.html')
    print("Deleted portfolio-tibico-health.html")

print("Cleaned portfolio.html")
