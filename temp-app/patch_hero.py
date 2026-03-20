import os

css_path = r"c:\Users\Baker\Documents\RAYVOTECH DIGITAL\temp-app\style.css"

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n\n/* Override Hero Title Size */\n.hero-title { font-size: clamp(2.5rem, 5vw, 4rem) !important; }\n")

print("Patched style.css successfully.")
