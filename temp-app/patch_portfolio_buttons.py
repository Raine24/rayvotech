import os
import re

projects = [
    {"title": "Body Fit Training", "slug": "portfolio-body-fit.html"},
    {"title": "Proper Health", "slug": "portfolio-proper-health.html"},
    {"title": "A Moment Photography", "slug": "portfolio-moment-photography.html"},
    {"title": "KC Creative Photography", "slug": "portfolio-kc-creative.html"},
    {"title": "Call Greens", "slug": "portfolio-call-greens.html"},
    {"title": "Firebirds Restaurant", "slug": "portfolio-firebirds.html"},
    {"title": "Jamie Graham Law", "slug": "portfolio-jamie-graham.html"},
    {"title": "Lueder", "slug": "portfolio-lueder.html"},
    {"title": "Tibico Health", "slug": "portfolio-tibico-health.html"},
    {"title": "Women's Foundation", "slug": "portfolio-womens-foundation.html"},
    {"title": "Stapende Auto", "slug": "portfolio-stapende-auto.html"},
    {"title": "Absolute Collagen", "slug": "portfolio-absolute-collagen.html"}
]

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

for p in projects:
    # We want to inject a beautiful button at the bottom of the card content.
    # The structure ends with:
    # <div class="tech-icons" style="margin-bottom:0; justify-content:flex-start;">
    #     <span class="tech-badge">...</span>
    #     <span class="tech-badge">...</span>
    # </div>
    # </div> <!-- Ends the padding: 2.5rem; div -->
    # </div> <!-- Ends the testimonial-card div -->
    
    # We will find the tech-icons div corresponding to the title and replace it
    pattern = rf"(<h3[^>]*>{p['title']}</h3>[\s\S]*?<div class=\"tech-icons\"[^>]*>[\s\S]*?</div>)"
    
    button_html = f"""\\1
                        <div style="margin-top: 2rem; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 1.5rem;">
                            <a href="{p['slug']}" class="btn" style="width: 100%; text-align: center; background: rgba(0, 230, 240, 0.1); color: var(--color-accent); border: 1px solid rgba(0, 230, 240, 0.3); border-radius: 8px; padding: 0.8rem; font-weight: 600; display: block; transition: all 0.3s;">
                                View Full Case Study <i class="ph ph-arrow-right" style="vertical-align: middle; margin-left: 5px;"></i>
                            </a>
                        </div>"""
    html = re.sub(pattern, button_html, html)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
# Let's also verify and fix index.html so its buttons look beautiful and point to the right place.
# The user said the button looked ugly and not well placed. 
# On index.html, it's currently inside the project-overlay.
print("Patched portfolio.html.")
