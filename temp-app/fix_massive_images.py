import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Target only the massive showcase images which use height: 600px
        # We replace it with clamp to ensure it's squared on mobile but full 600px on desktop
        new_content = content.replace('height: 600px;', 'height: clamp(300px, 50vw, 600px);')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed massive image heights in {filepath}")
    except Exception as e:
        print(f"Failed processing {filepath}: {e}")
