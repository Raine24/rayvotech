import glob

for f in glob.glob('*.html'):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = content.replace('style.css?v=3', 'style.css?v=4')
        content = content.replace('style.css', 'style.css?v=4') # fallback
        content = content.replace('style.css?v=4?v=4', 'style.css?v=4')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Safe cache bust applied to {f}")
    except Exception as e:
        print(f"Error on {f}: {e}")
