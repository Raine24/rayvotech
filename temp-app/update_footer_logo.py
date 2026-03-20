import glob

footer_logo_target = '<a href="index.html" class="logo" style="font-size: 2.25rem; margin-bottom: 1.5rem; display: block;">Rayvo<span style="color: var(--color-accent);">tech</span></a>'
footer_logo_replacement = '<a href="index.html" class="logo" style="margin-bottom: 1.5rem; display: block;"><img src="https://i.imgur.com/thPnAch.png" alt="Rayvotech Logo" style="height: 50px; width: auto;" /></a>'

updated_files = 0

for filepath in glob.glob('*.html'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if footer_logo_target in content:
            new_content = content.replace(footer_logo_target, footer_logo_replacement)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files += 1
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

print(f"\nDone! Successfully updated {updated_files} files.")
