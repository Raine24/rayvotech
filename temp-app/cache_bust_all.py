import glob
import re

html_files = glob.glob('*.html')
pattern = re.compile(r'href="style\.css\?v=\d+"')
replacement = 'href="style.css?v=23"'

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub(replacement, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cache busted {filepath}")
    except Exception as e:
        print(f"Failed processing {filepath}: {e}")
