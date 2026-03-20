import os
import re

links = {
    "portfolio-body-fit.html": "https://www.bodyfittraining.au",
    "portfolio-proper-health.html": "https://properhealth.com",
    "portfolio-moment-photography.html": "https://www.ampstudio.photos",
    "portfolio-kc-creative.html": "https://www.kccreativedesign.com",
    "portfolio-call-greens.html": "https://www.callgreens.com",
    "portfolio-firebirds.html": "https://firebirdsrestaurants.com",
    "portfolio-jamie-graham.html": "https://www.jamiegrahamlaw.com",
    "portfolio-lueder.html": "https://www.lueder.com",
    "portfolio-tibico-health.html": "https://www.tibicohealth.com",
    "portfolio-womens-foundation.html": "https://thewomensfoundation.org",
    "portfolio-stapende-auto.html": "https://stampedeauto.com",
    "portfolio-absolute-collagen.html": "https://www.absolutecollagen.com"
}

for filename, url in links.items():
    if not os.path.exists(filename):
        print(f"Skipping {filename}, not found.")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # We want to inject the button right after the tech-icons div in the hero section.
    # The tech-icons div looks like:
    # <div class="tech-icons reveal-text delay-2" style="justify-content: center;">
    #    <span class="tech-badge">...</span>
    #    <span class="tech-badge">...</span>
    # </div>
    
    # We'll use regex to find it and append the link div.
    pattern = r'(<div class="tech-icons reveal-text delay-2" style="justify-content: center;">[\s\S]*?</div>)'
    
    button_html = f"""\\1
            <div style="margin-top: 2rem;" class="reveal-text delay-2">
                <a href="{url}" target="_blank" rel="nofollow" class="btn btn-outline" style="border-color: rgba(255,255,255,0.2); color: var(--text-secondary);">Visit Live Website <i class="ph ph-arrow-square-out"></i></a>
            </div>"""
            
    # Also optionally add meta robots noindex to be extra safe about google not indexing these specific project pages' links
    # But he said "Include a no index tag because i dont want google to index those links" -> rel="nofollow" is the direct answer.
    
    new_html = re.sub(pattern, button_html, html, count=1)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_html)
        
print("Successfully injected client URLs with nofollow attributes.")
