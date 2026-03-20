import re

def main():
    with open('services.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the container section
    section_match = re.search(r'(<!-- Services Detailed -->.*?)<div class="container".*?>', html, re.DOTALL)
    if not section_match:
        print("Could not find section.")
        return

    # We want to replace the container start and the services inside
    # First, let's extract all 4 services
    services_pattern = r'(<!-- Service \d{1}: .*? -->)\s*<div class="flat-card.*?>\s*<div style="display: grid;.*?>\s*<!-- Left Side: Pitch -->\s*<div style="padding: clamp\(2rem, 5vw, 4rem\); position: relative;">(.*?)</div>\s*<!-- Right Side: Deliverables -->\s*<div style="background: rgba.*?">(.*?)</div>\s*</div>\s*</div>'
    
    services = list(re.finditer(services_pattern, html, re.DOTALL))
    if len(services) != 4:
        print(f"Found {len(services)} services, expected 4. Script might need adjustment.")
        return

    new_services_html = '\n                '.join([
        f"""{s.group(1)}
                <div class="flat-card beam-card fade-up glass-card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; gap: 0; border-radius: 24px; height: 100%;">
                    <div style="padding: clamp(1.5rem, 3vw, 2.5rem); display: flex; flex-direction: column; height: 100%; position: relative;">
                        {s.group(2).strip()}
                        
                        <div style="flex-grow: 1;"></div> <!-- pushes deliverables to bottom -->
                        
                        <div style="margin-top: 2.5rem; padding-top: 2.5rem; border-top: 1px solid rgba(255,255,255,0.1); background: transparent;">
                            {s.group(3).strip()}
                        </div>
                    </div>
                </div>"""
        for s in services
    ])

    new_section = f"""    <!-- Services Detailed -->
    <section class="section-padding" id="services">
        <div class="container" style="max-width: 1400px;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 500px), 1fr)); gap: 2.5rem;">
                {new_services_html}
            </div>
        </div>
    </section>"""

    # Replace everything from <!-- Services Detailed --> to the end of the section
    start_idx = html.find('<!-- Services Detailed -->')
    end_idx = html.find('</section>', start_idx) + 10
    
    final_html = html[:start_idx] + new_section + html[end_idx:]

    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully restructered services.html")

if __name__ == '__main__':
    main()
