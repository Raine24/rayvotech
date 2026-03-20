import os

css_path = r"c:\Users\Baker\Documents\RAYVOTECH DIGITAL\temp-app\style.css"

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n\n/* Override Hero Section Padding & Floating Element Box */\n")
    f.write(".hero { padding-top: 120px !important; min-height: auto !important; margin-bottom: 2rem !important; }\n")
    f.write("@media(max-width: 900px) { .hero { padding-top: 100px !important; } }\n")
    
    # Move code-window towards the center gap on desktop
    f.write("@media(min-width: 900px) {\n")
    f.write("  .hero-objects .code-window { right: 45% !important; bottom: 25% !important; top: auto !important; transform: translateX(50%) !important; z-index: 10 !important; }\n")
    f.write("  .hero-objects .ui-widget { left: 45% !important; top: 25% !important; transform: translateX(-50%) !important; z-index: 10 !important; }\n")
    f.write("}\n")
    
    # Make sure they still look good on mobile
    f.write("@media(max-width: 899px) {\n")
    f.write("  .hero-objects .code-window { top: 10% !important; right: 10% !important; }\n")
    f.write("}\n")

print("Added CSS overrides for padding and floating objects.")
