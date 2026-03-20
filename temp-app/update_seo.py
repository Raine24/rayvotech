import os
import re

TARGET_DIR = r"c:\Users\Baker\Documents\RAYVOTECH DIGITAL\temp-app"
TAGLINE = "Built to Elevate. Designed to Convert."
DESC = "We design, build, and grow digital experiences that attract the right audience and turn them into paying customers."

def update_seo():
    count = 0
    for filename in os.listdir(TARGET_DIR):
        if not filename.endswith('.html'):
            continue
            
        filepath = os.path.join(TARGET_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Temporarily clean up old meta titles to avoid duplicates if they exist
        content = re.sub(r'<meta property="og:title" content=".*?">\n?', '', content)
        content = re.sub(r'<meta property="twitter:title" content=".*?">\n?', '', content)
        
        # We will extract title later for OG
        final_title = "Rayvotech | " + TAGLINE
        m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if m:
            old_title = m.group(1).strip()
            prefix = old_title.split('|')[0].strip() if '|' in old_title else old_title
            if prefix.lower() == 'rayvotech' or 'rayvotech' in prefix.lower():
                final_title = f"Rayvotech | {TAGLINE}"
            else:
                final_title = f"{prefix} | Rayvotech - {TAGLINE}"
            content = re.sub(r'<title>.*?</title>', f'<title>{final_title}</title>', content, flags=re.IGNORECASE)
        else:
            content = content.replace('<head>', f'<head>\n    <title>{final_title}</title>')
        
        # 2. Description Replacement
        if '<meta name="description"' in content:
            content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{DESC}">', content, flags=re.IGNORECASE)
        else:
            content = content.replace('<title>', f'<meta name="description" content="{DESC}">\n    <title>')
            
        # 3. Clean up existing OG / Twitter / Schema if script was run multiple times
        content = re.sub(r'\s*<!-- SEO_INJECT_START -->.*?<!-- SEO_INJECT_END -->\n?', '', content, flags=re.DOTALL)
        
        SEO_BLOCK = f"""
    <!-- SEO_INJECT_START -->
    <!-- Open Graph / Social Media -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://rayvotech.com/">
    <meta property="og:title" content="{final_title}">
    <meta property="og:description" content="{DESC}">
    <meta property="og:image" content="https://i.imgur.com/thPnAch.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://rayvotech.com/">
    <meta property="twitter:title" content="{final_title}">
    <meta property="twitter:description" content="{DESC}">
    <meta property="twitter:image" content="https://i.imgur.com/thPnAch.png">

    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "Rayvotech Digital",
      "url": "https://rayvotech.com",
      "logo": "https://i.imgur.com/thPnAch.png",
      "image": "https://i.imgur.com/thPnAch.png",
      "description": "{DESC}",
      "address": {{
        "@type": "PostalAddress",
        "addressCountry": "US"
      }},
      "sameAs": [
        "https://www.facebook.com/rayvotechdigital",
        "https://www.instagram.com/rayvotech_digital/"
      ]
    }}
    </script>
    <!-- SEO_INJECT_END -->"""

        if '<!-- Google Fonts -->' in content:
            content = content.replace('<!-- Google Fonts -->', f'{SEO_BLOCK}\n    <!-- Google Fonts -->')
        else:
            content = content.replace('</head>', f'{SEO_BLOCK}\n</head>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
            
    print(f"SEO updates applied successfully to {count} HTML files.")

if __name__ == '__main__':
    update_seo()
