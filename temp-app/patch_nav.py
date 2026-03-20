import os
import glob

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace `<div class="nav-links"> \n <a href="about.html">` 
    # with `<div class="nav-links">\n<a href="index.html">Home</a>\n<a href="about.html">`
    # Let's just look for '<div class="nav-links">'
    # and if '<a href="index.html">Home</a>' is not immediately following it, inject it.

    if '<a href="index.html">Home</a>' not in content:
        # We can just replace '<div class="nav-links">' with '<div class="nav-links">\n                <a href="index.html">Home</a>'
        # Wait, let's be safe. Replace '<div class="nav-links">\\n                <a href="about.html">'
        content = content.replace(
            '<div class="nav-links">\n                <a href="about.html">',
            '<div class="nav-links">\n                <a href="index.html">Home</a>\n                <a href="about.html">'
        )
        
        # In case the whitespace is slightly different:
        import re
        content = re.sub(
            r'(<div class="nav-links">\s*)<a href="about.html">',
            r'\1<a href="index.html">Home</a>\n                <a href="about.html">',
            content
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Patched navigation in {len(html_files)} HTML files.")
