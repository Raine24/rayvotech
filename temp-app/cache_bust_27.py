import glob
import re

html_files = glob.glob('*.html')
pattern = re.compile(r'style\.css\?v=\d+')
replacement = 'style.css?v=27'

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = pattern.sub(replacement, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except Exception as e:
        print(f"Failed processing {filepath}: {e}")
