import os
import glob

directory = r"c:\Users\Baker\Documents\RAYVOTECH DIGITAL\temp-app"
html_files = glob.glob(os.path.join(directory, "*.html"))

hamburger_markup = """            <!-- Hamburger Menu -->
            <button class="mobile-menu-toggle" aria-label="Toggle Menu" style="display: none;">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </button>"""

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "mobile-menu-toggle" in content:
        continue # Already injected

    # Inject after the Hire Us button
    marker = '<a href="hire.html" class="btn btn-primary">Hire Us</a>'
    if marker in content:
        new_content = content.replace(marker, marker + "\n" + hamburger_markup)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

print(f"Mobile menu markup injected into {len(html_files)} files!")
