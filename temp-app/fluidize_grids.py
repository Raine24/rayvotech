import glob
import re

html_files = glob.glob('*.html')
# Finds minmax(450px... and ignores minmax(min...
pattern = re.compile(r'minmax\(\s*(?!min)(\d+px)')

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub(r'minmax(min(100%, \1)', content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fluidized grids in {filepath}")
    except Exception as e:
        print(f"Failed processing {filepath}: {e}")
