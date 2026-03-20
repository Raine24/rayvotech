import os
import re

css_path = r"c:\Users\Baker\Documents\RAYVOTECH DIGITAL\temp-app\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

new_css = """
/* Override Hero Section Padding & Floating Element Box */
.hero { padding-top: 100px !important; min-height: auto !important; margin-bottom: 2rem !important; }
@media(max-width: 900px) { .hero { padding-top: 80px !important; } }

@media(min-width: 900px) {
  .hero-objects .ui-widget { display: none !important; }
  .hero-objects .code-window { 
      right: auto !important; 
      left: 32% !important; 
      bottom: auto !important; 
      top: 15% !important; 
      z-index: 10 !important; 
      zoom: 0.8; /* Makes it smaller without overriding transform animations */
  }
}
@media(max-width: 899px) {
  .hero-objects .ui-widget { display: none !important; }
  .hero-objects .code-window { right: auto !important; left: 30% !important; top: 10% !important; zoom: 0.7; }
}
"""

if "/* Override Hero Section Padding" in content:
    content = re.sub(r'/\* Override Hero Section Padding & Floating Element Box \*/.*', new_css.strip(), content, flags=re.DOTALL)
else:
    content += "\n\n" + new_css.strip()

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied CSS placement and resize tweaks for code window without overriding transforms!")
