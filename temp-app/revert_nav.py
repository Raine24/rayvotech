import os
import re

nav_replacement = """<div class="nav-links">
                <a style="--i: 0;" href="index.html">Home</a>
                <a style="--i: 1;" href="about.html">About Us</a>
                <a style="--i: 2;" href="services.html">Services</a>
                <a style="--i: 3;" href="portfolio.html">Portfolio</a>
                <a style="--i: 4;" href="pricing.html">Pricing</a>
                <a style="--i: 5;" href="faqs.html">FAQs</a>
                <a style="--i: 6;" href="contact.html">Contact</a>
                <a style="--i: 7;" href="hire.html" class="menu-hire-btn">HIRE US</a>
            </div>
            <a href="hire.html" class="btn btn-primary">Hire Us</a>
            <!-- Hamburger Menu -->
            <button class="mobile-menu-toggle" aria-label="Toggle Menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </button>
        </div>
    </nav>"""

pattern = re.compile(r'<div class="nav-links">.*?</nav>', re.DOTALL)

updated = 0
for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if pattern.search(content):
            new_content = pattern.sub(nav_replacement, content)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            updated += 1

print(f"Reverted {updated} HTML files to simple desktop-safe nav.")
