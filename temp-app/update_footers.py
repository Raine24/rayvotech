import os
import glob
import re

new_footer_html = """
            <style>
                .footer-grid {
                    display: grid;
                    grid-template-columns: 2fr 1fr 1fr 1fr;
                    gap: 4rem;
                    padding: 4rem 0;
                    border-top: 1px solid rgba(255,255,255,0.1);
                    margin-top: 5rem;
                }
                .footer-grid h4 {
                    font-size: 1.25rem;
                    color: #fff;
                    margin-bottom: 1.5rem;
                    position: relative;
                    padding-bottom: 0.5rem;
                }
                .footer-grid h4::after {
                    content: '';
                    position: absolute;
                    left: 0;
                    bottom: 0;
                    width: 30px;
                    height: 2px;
                    background: var(--color-accent);
                }
                .footer-links-col {
                    display: flex;
                    flex-direction: column;
                    gap: 1rem;
                }
                .footer-links-col a {
                    color: var(--text-secondary);
                    text-decoration: none;
                    transition: all 0.3s ease;
                    font-size: 1.05rem;
                    display: inline-block;
                }
                .footer-links-col a:hover {
                    color: var(--color-accent);
                    transform: translateX(5px);
                }
                .social-circle {
                    width: 45px;
                    height: 45px;
                    border-radius: 50%;
                    background: rgba(255,255,255,0.05);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: var(--text-primary);
                    font-size: 1.25rem;
                    transition: all 0.3s ease;
                }
                .social-circle:hover {
                    background: var(--color-accent);
                    color: #000;
                    transform: translateY(-5px);
                }
                @media (max-width: 900px) {
                    .footer-grid {
                        grid-template-columns: 1fr 1fr;
                        gap: 2rem;
                    }
                }
                @media (max-width: 600px) {
                    .footer-grid {
                        grid-template-columns: 1fr;
                        gap: 3rem;
                    }
                }
            </style>
            
            <div class="footer-grid">
                <!-- Brand Col -->
                <div class="footer-brand" style="margin: 0;">
                    <a href="index.html" class="logo" style="font-size: 2.25rem; margin-bottom: 1.5rem; display: block;">Rayvo<span style="color: var(--color-accent);">tech</span></a>
                    <p style="color: var(--text-secondary); line-height: 1.8; max-width: 300px; margin-bottom: 2.5rem; font-size: 1.1rem;">We craft digital experiences that command attention, build trust, and drive action for ambitious brands across the US.</p>
                    <div style="display: flex; gap: 1rem;">
                        <a href="#" class="social-circle"><i class="ph ph-twitter-logo"></i></a>
                        <a href="#" class="social-circle"><i class="ph ph-linkedin-logo"></i></a>
                        <a href="#" class="social-circle"><i class="ph ph-instagram-logo"></i></a>
                        <a href="#" class="social-circle"><i class="ph ph-dribbble-logo"></i></a>
                    </div>
                </div>

                <!-- Company -->
                <div class="footer-links-col">
                    <h4>Company</h4>
                    <a href="about.html">About Us</a>
                    <a href="portfolio.html">Our Work</a>
                    <a href="pricing.html">Pricing Structure</a>
                    <a href="faqs.html">FAQs & Support</a>
                    <a href="contact.html">Contact Us</a>
                </div>

                <!-- Services -->
                <div class="footer-links-col">
                    <h4>Services</h4>
                    <a href="service-website-design.html">Website Design</a>
                    <a href="service-ui-ux-design.html">UI/UX Layouts</a>
                    <a href="service-web-development.html">Web Development</a>
                    <a href="service-seo-growth.html">SEO & Growth</a>
                </div>

                <!-- Legal -->
                <div class="footer-links-col">
                    <h4>Legal</h4>
                    <a href="terms.html">Terms & Conditions</a>
                    <a href="privacy.html">Privacy Policy</a>
                    <a href="cookies.html">Cookies Policy</a>
                    <a href="disclaimer.html">Disclaimer</a>
                </div>
            </div>

            <div class="footer-legal" style="padding: 2.5rem 0; border-top: 1px solid rgba(255,255,255,0.05); color: var(--text-secondary); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.5rem; margin-top: 2rem;">
                <p style="margin: 0; font-size: 1rem;">&copy; 2026 Rayvotech Digital. Built with precision.</p>
                <div style="display: flex; gap: 1.5rem; font-size: 0.95rem;">
                    <span style="display: flex; align-items: center; gap: 0.5rem;"><i class="ph-fill ph-check-circle" style="color: var(--color-accent);"></i> Secure & Operational</span>
                </div>
            </div>
"""

# Pattern to strictly replace the footer links section across all HTML files.
# It matches from `<div class="footer-bottom">` all the way to `</div>\n    </footer>`
pattern = r'<div class="footer-bottom">.*?(</script>|</body>|</html>)'

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create the regex to find where footer-bottom starts and replace it up to the footer close.
    # A safe approach is finding ' <div class="footer-bottom">' and '</footer>'
    start_idx = content.find('<div class="footer-bottom">')
    end_idx = content.find('</footer>', start_idx)

    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + new_footer_html + "        </div>\n    " + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {filepath}")

# Now, generate the 4 legal pages using base structure from a short template
template_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Rayvotech</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
</head>
<body class="theme-aurora">
    
    <!-- Navbar -->
    <nav class="navbar glass-effect">
        <div class="container navbar-container">
            <a href="index.html" class="logo">Rayvo<span>tech</span></a>
            <button class="mobile-menu-btn"><i class="ph ph-list"></i></button>
            <div class="nav-links">
                <a href="about.html">About</a>
                <a href="services.html">Services</a>
                <a href="portfolio.html">Portfolio</a>
                <a href="pricing.html">Pricing</a>
                <a href="hire.html" class="btn btn-primary" style="padding: 0.5rem 1.25rem;">Hire Us</a>
            </div>
        </div>
    </nav>

    <!-- Header -->
    <section class="hero" style="min-height: auto; padding-top: 10rem; padding-bottom: 3rem;">
        <div class="container text-center fade-up">
            <h1 class="hero-title" style="font-size: 4rem;">{title}</h1>
            <p class="hero-subtitle" style="font-size: 1.25rem;">Last Updated: October 2026</p>
        </div>
    </section>

    <!-- Content -->
    <section class="section-padding" style="padding-top: 2rem;">
        <div class="container" style="max-width: 800px;">
            <div class="glass-card fade-up" style="padding: 4rem; border-radius: 24px;">
                <h2 style="font-size: 2rem; margin-bottom: 1.5rem;">Placeholder for {title}</h2>
                <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2rem;">
                    This is a legally binding document generated for demonstration purposes. In a live production environment, this text will be replaced with officially vetted legal terminology tailored to your company's jurisdiction and operational requirements.
                </p>
                <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2rem;">
                    If you have any questions or concerns, please contact our support team at legal@rayvotech.test.
                </p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer" id="contact" style="padding-top: 5rem;">
        <div class="container">
{footer}
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>
"""

pages = [
    ("terms.html", "Terms & Conditions"),
    ("privacy.html", "Privacy Policy"),
    ("cookies.html", "Cookie Policy"),
    ("disclaimer.html", "Disclaimer")
]

for filename, title in pages:
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(template_html.format(title=title, footer=new_footer_html))
        print(f"Created {filename}")

print("All footer and legal page tasks successfully resolved.")
