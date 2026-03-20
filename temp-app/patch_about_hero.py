import os

html_path = r"c:\Users\Baker\Documents\RAYVOTECH DIGITAL\temp-app\about.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

old_h1 = """<h1 class="hero-title reveal-text delay-1" style="font-size: 6rem; line-height: 1.05; letter-spacing: -2px; margin-bottom: 2rem;">
                Built for <br> <span class="text-gradient liquid-text" style="background: linear-gradient(to right, #ffffff, #888888); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Excellence.</span>
            </h1>"""

new_h1 = """<h1 class="hero-title reveal-text delay-1" style="font-size: clamp(3rem, 10vw, 6rem); line-height: 1.05; letter-spacing: -2px; margin-bottom: 2rem;">
                Built for <br> <span class="text-gradient liquid-text" style="background: linear-gradient(to right, #ffffff, #888888); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Excellence.</span>
            </h1>"""

old_p = """<p class="hero-subtitle reveal-text delay-2" style="max-width: 800px; margin: 0 auto; font-size: 1.35rem; color: var(--text-secondary); line-height: 1.6;">
                We are a collective of engineers, designers, and strategists. We don't just build websites; we architect the digital infrastructure for tomorrow's leading brands.
            </p>"""

new_p = """<p class="hero-subtitle reveal-text delay-2" style="max-width: 800px; margin: 0 auto; font-size: clamp(1rem, 3vw, 1.35rem); color: var(--text-secondary); line-height: 1.6; padding: 0 1rem; text-wrap: balance;">
                We are a collective of engineers, designers, and strategists. <br class="desktop-only">We don't just build websites; we architect the digital infrastructure for tomorrow's leading brands.
            </p>
            <style>
              @media (max-width: 768px) { .desktop-only { display: none; } }
            </style>"""

html = html.replace(old_h1, new_h1)
html = html.replace(old_p, new_p)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated About Us hero typography and alignment!")
