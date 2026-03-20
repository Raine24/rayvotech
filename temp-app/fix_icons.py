import os

html_file = 'services.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_style = 'style="margin: 0; width: 44px; height: 44px; font-size: 1.25rem; flex-shrink: 0;"'
new_style = 'style="margin: 0; padding: 0; display: flex; align-items: center; justify-content: center; width: 44px; height: 44px; font-size: 1.25rem; flex-shrink: 0; border-radius: 50%;"'

content = content.replace(old_style, new_style)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Centering applied to {html_file}")
