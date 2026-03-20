import glob

html_files = ['terms.html', 'privacy.html', 'cookies.html', 'disclaimer.html']

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Just forcibly add 'visible' to any instance of 'fade-up'
        if 'fade-up visible' not in content:
            new_content = content.replace('fade-up', 'fade-up visible')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Forced .visible on {filepath}")
        else:
            print(f"{filepath} already forced visible.")
    except Exception as e:
        print(f"Failed processing {filepath}: {e}")
