import glob

logo_target = '<a href="index.html" class="logo">Rayvo<span>tech</span></a>'
logo_replacement = '<a href="index.html" class="logo" style="display: flex; align-items: center;"><img src="https://i.imgur.com/thPnAch.png" alt="Rayvotech" style="height: 35px; width: auto;" /></a>'

social_target = """                    <div style="display: flex; gap: 1rem;">
                        <a href="#" class="social-circle"><i class="ph ph-twitter-logo"></i></a>
                        <a href="#" class="social-circle"><i class="ph ph-linkedin-logo"></i></a>
                        <a href="#" class="social-circle"><i class="ph ph-instagram-logo"></i></a>
                        <a href="#" class="social-circle"><i class="ph ph-dribbble-logo"></i></a>
                    </div>"""

social_replacement = """                    <div style="display: flex; gap: 1rem;">
                        <a href="https://www.facebook.com/rayvotechdigital" target="_blank" rel="noopener noreferrer" class="social-circle"><i class="ph ph-facebook-logo"></i></a>
                        <a href="https://www.instagram.com/rayvotech_digital/" target="_blank" rel="noopener noreferrer" class="social-circle"><i class="ph ph-instagram-logo"></i></a>
                        <a href="#" class="social-circle"><i class="ph ph-twitter-logo"></i></a>
                        <a href="#" class="social-circle"><i class="ph ph-linkedin-logo"></i></a>
                    </div>"""

updated_files = 0

for filepath in glob.glob('*.html'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content.replace(logo_target, logo_replacement)
        new_content = new_content.replace(social_target, social_replacement)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files += 1
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

print(f"\nDone! Successfully updated {updated_files} files.")
