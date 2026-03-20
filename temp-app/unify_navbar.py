import re

html_files = ['terms.html', 'privacy.html', 'cookies.html', 'disclaimer.html']

correct_navbar = """    <!-- Navigation -->
    <nav class="navbar glass-effect">
        <div class="nav-container container">
            <a href="index.html" class="logo">Rayvo<span>tech</span></a>
            <button class="mobile-menu-btn" aria-label="Toggle Navigation"><i class="ph ph-list" style="font-size: 1.5rem; color: var(--text-primary);"></i></button>
            <div class="nav-links">
                <a href="index.html">Home</a>
                <a href="about.html">About Us</a>
                <a href="services.html">Services</a>
                <a href="portfolio.html">Portfolio</a>
                <a href="pricing.html">Pricing</a>
                <a href="faqs.html">FAQs</a>
                <a href="contact.html">Contact</a>
            </div>
            <a href="hire.html" class="btn btn-primary">Hire Us</a>
        </div>
    </nav>"""

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = re.compile(r'<!-- Navbar -->.*?</nav>', re.DOTALL)
        
        if pattern.search(content):
            new_content = pattern.sub(correct_navbar, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Replaced Navbar in {filepath}")
        else:
            print(f"Could not find exact Navbar pattern in {filepath}")
    except Exception as e:
        print(f"Failed processing {filepath}: {e}")
