import re

def generate_pages():
    with open('services.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract header up to <!-- Services Detailed -->
    header_match = re.search(r'(.*?)<!-- Services Detailed -->', content, re.DOTALL)
    header = header_match.group(1)

    # We need to change the hero section title and subtitle for each page slightly later.
    # Actually, we can just replace the hero content for each page.
    
    # Extract footer starting from <!-- Footer -->
    footer_match = re.search(r'(<!-- Footer -->.*)', content, re.DOTALL)
    footer = footer_match.group(1)

    # Extract individual services
    services = [
        {
            'id': 'service-website-design.html',
            'title': 'Website Design',
            'regex': r'(<!-- Service 0: Website Design -->.*?)(?=<!-- Service 1: UI/UX Design -->)',
            'bg': '#f43f5e',
            'gradient': 'liquid-text'
        },
        {
            'id': 'service-ui-ux-design.html',
            'title': 'UI/UX Design',
            'regex': r'(<!-- Service 1: UI/UX Design -->.*?)(?=<!-- Service 2: Web Dev -->)',
            'bg': '#FF5F56',
            'gradient': 'liquid-text'
        },
        {
            'id': 'service-web-development.html',
            'title': 'Custom Web Development',
            'regex': r'(<!-- Service 2: Web Dev -->.*?)(?=<!-- Service 3: SEO -->)',
            'bg': '#0284c7',
            'gradient': 'liquid-text'
        },
        {
            'id': 'service-seo-growth.html',
            'title': 'SEO & Growth',
            'regex': r'(<!-- Service 3: SEO -->.*?)(?=</div>\s*</section>\s*<!-- Footer -->)',
            'bg': '#a855f7',
            'gradient': 'liquid-text'
        }
    ]

    for s in services:
        match = re.search(s['regex'], content, re.DOTALL)
        if not match:
            print(f"Could not find match for {s['title']}")
            continue
            
        service_html = match.group(1)
        
        # Remove the "Learn More" button from the individual service page since they are already on it
        service_html = re.sub(r'<a href="service-.*?\.html".*?>Learn More.*?</a>', '', service_html, flags=re.DOTALL)
        
        # Customize hero
        custom_header = re.sub(r'<h1 class="hero-title.*?</h1>', f'<h1 class="hero-title reveal-text delay-1" style="font-size: 4rem;">{s["title"]} <br> <span class="text-gradient {s["gradient"]}">Services.</span></h1>', header)
        custom_header = re.sub(r'<div class="y2k-badge reveal-text">OUR EXPERTISE</div>', f'<div class="y2k-badge reveal-text">{s["title"].upper()}</div>', custom_header)
        custom_header = re.sub(r'<p class="hero-subtitle.*?</p>', f'<p class="hero-subtitle reveal-text delay-2" style="max-width: 600px; margin: 0 auto;">Comprehensive {s["title"].lower()} solutions tailored to elevate your brand and drive results.</p>', custom_header)
        custom_header = re.sub(r'<title>Rayvotech \| Services</title>', f'<title>Rayvotech | {s["title"]}</title>', custom_header)

        # Assemble page
        page_content = custom_header + '\n    <!-- Services Detailed -->\n    <section class="section-padding">\n        <div class="container" style="max-width: 1100px;">\n' + service_html + '\n        </div>\n    </section>\n\n    ' + footer
        
        with open(s['id'], 'w', encoding='utf-8') as f:
            f.write(page_content)
        print(f"Created {s['id']}")

if __name__ == '__main__':
    generate_pages()
