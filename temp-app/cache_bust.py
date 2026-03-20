import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Cache bust the CSS link
        if 'href="style.css"' in content:
            new_content = content.replace('href="style.css"', 'href="style.css?v=3"')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Cache busted {filepath}")
    except Exception as e:
        print(f"Failed processing {filepath}: {e}")
