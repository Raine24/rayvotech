import os
import glob

directory = r"c:\Users\Baker\Documents\RAYVOTECH DIGITAL\temp-app"
html_files = glob.glob(os.path.join(directory, "*.html"))

favicon_tag = '    <!-- Favicon -->\n    <link rel="icon" type="image/png" href="https://i.imgur.com/PYTMauh.png">\n'

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "rel=\"icon\"" in content or "PYTMauh.png" in content:
        # Avoid duplicating if already present
        continue

    # Insert just before </head>
    if "</head>" in content:
        content = content.replace("</head>", favicon_tag + "</head>")
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
print(f"Branded Favicon Successfully added to {len(html_files)} HTML pages!")
