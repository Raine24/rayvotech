import os

css_path = r"c:\Users\Baker\Documents\RAYVOTECH DIGITAL\temp-app\style.css"

with open(css_path, "a", encoding="utf-8") as f:
    f.write("""
/* ------------------------------------------- */
/* HERO OPTIMIZATION FOR 2 LINES & NO SCROLL  */
/* ------------------------------------------- */

/* Shared space reduction to bring CTA up */
.hero-text-col > h1 { margin-bottom: 1rem !important; line-height: 1.1 !important; }
.hero-text-col > p { margin-bottom: 1.5rem !important; line-height: 1.4 !important; }
.y2k-badge { margin-bottom: 0.5rem !important; }

/* Desktop */
@media(min-width: 900px) {
  .hero-title { font-size: clamp(3rem, 4.5vw, 4.5rem) !important; white-space: nowrap; }
  .hero-subtitle { max-width: 95% !important; font-size: clamp(1rem, 1.5vw, 1.2rem) !important; white-space: nowrap; }
}

/* Mobile */
@media(max-width: 899px) {
  /* Shrink text specifically so it doesn't wrap to a third line */
  .hero-title { font-size: clamp(1.8rem, 8vw, 2.5rem) !important; }
  .hero-subtitle { font-size: clamp(0.85rem, 4vw, 1rem) !important; max-width: 100% !important; }
  .hero-actions .btn { padding: 0.5rem 1rem !important; font-size: 0.9rem !important; }
  .hero-top-split { gap: 1rem !important; }
  .hero { padding-top: 60px !important; margin-bottom: 1rem !important; }
}
""")

print("Appended responsive overrides to style.css!")
