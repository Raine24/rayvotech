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
      left: 36% !important; /* Center-left as requested */
      bottom: auto !important; 
      top: 18% !important; /* Pushed down to clear the header */
      transform: translate(-50%, 0) scale(1.3) !important; /* Increased size */
      z-index: 10 !important; 
  }
}
@media(max-width: 899px) {
  .hero-objects .ui-widget { display: none !important; }
  .hero-objects .code-window { top: 12% !important; left: 50% !important; transform: translateX(-50%) scale(1.1) !important; right: auto !important; }
}
"""

if "/* Override Hero Section Padding" in content:
    content = re.sub(r'/\* Override Hero Section Padding & Floating Element Box \*/.*', new_css.strip(), content, flags=re.DOTALL)
else:
    content += "\n\n" + new_css.strip()

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied CSS placement and resize tweaks for code window!")
