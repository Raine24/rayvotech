import os
import re

projects = [
    {
        "id": 1,
        "title": "Body Fit Training",
        "slug": "portfolio-body-fit.html",
        "image": "https://i.imgur.com/yHr7Ova.jpg",
        "type": "Fitness Platform",
        "challenge": "A high-performance fitness franchise required a dynamic, energetic digital platform to handle class scheduling, member onboarding, and location-based discovery. The previous system was experiencing severe latency during peak booking hours.",
        "solution": "We architected a bespoke frontend experience utilizing lightweight UI/UX principles, coupled with a highly scalable database structure to ensure zero downtime. We engineered seamless integration with their existing member management APIs.",
        "results": ["+140% Mobile Conversions", "-70% Server Latency during Peak", "12,000+ Active Weekly Users"],
        "tags": ["UI/UX Design", "Web Dev"]
    },
    {
        "id": 2,
        "title": "Proper Health",
        "slug": "portfolio-proper-health.html",
        "image": "https://i.imgur.com/8l9EImC.jpg",
        "type": "Healthcare Portal",
        "challenge": "A localized healthcare provider needed a trustworthy, highly accessible online portal. The primary goal was to simplify patient education and drastically improve the appointment booking conversion rate without overwhelming older demographics.",
        "solution": "We deployed a clean, high-contrast UI focused on accessibility (WCAG compliant). We streamlined the booking flow into a frictionless multi-step form and implemented robust local SEO to capture immediate patient intent.",
        "results": ["+85% Form Submissions", "100/100 Accessibility Score", "Top 3 Local Search Ranking"],
        "tags": ["Web Dev", "SEO"]
    },
    {
        "id": 3,
        "title": "A Moment Photography",
        "slug": "portfolio-moment-photography.html",
        "image": "https://i.imgur.com/M020ECS.jpg",
        "type": "Creative Portfolio",
        "challenge": "A premium photography studio required a digital presence that matched their high-end aesthetic. They needed to serve massive, uncompressed image galleries without suffering from slow loading times that hurt SEO and user experience.",
        "solution": "We utilized advanced lazy-loading techniques, next-gen image formatting, and a bespoke brutalist-inspired UI. Micro-animations were added to make the browsing experience feel tactile and high-fashion.",
        "results": ["0.8s Initial Page Load", "0 Layout Shifts (CLS)", "+220% Session Duration"],
        "tags": ["Branding", "UI/UX Design"]
    },
    {
        "id": 4,
        "title": "KC Creative Photography",
        "slug": "portfolio-kc-creative.html",
        "image": "https://i.imgur.com/6rjCekC.jpg",
        "type": "Creative Studio",
        "challenge": "A fast-growing creative agency needed a web presence that did more than just look pretty—it needed to actively capture enterprise leads while showcasing vast reserves of past campaign media.",
        "solution": "We built a structurally brilliant lead-generation engine disguised as a seamless creative portfolio. We implemented intelligent caching and global CDNs to ensure global clients experienced zero lag.",
        "results": ["3x Increase in Lead Quality", "99.9% Uptime", "Page speed increased by 40%"],
        "tags": ["Web Dev", "Optimization"]
    },
    {
        "id": 5,
        "title": "Call Greens",
        "slug": "portfolio-call-greens.html",
        "image": "https://i.imgur.com/3X9popV.jpg",
        "type": "E-Commerce",
        "challenge": "A disruptive nutritional supplement brand was experiencing high cart abandonment rates on their legacy platform. They needed a custom flow that communicated trust while seamlessly nudging users toward recurring subscriptions.",
        "solution": "We overhauled the entire checkout flow utilizing psychological UX principles. We reduced friction, introduced trust badges strategically, and engineered a custom 'Build Your Bundle' subscription flow.",
        "results": ["-45% Cart Abandonment", "+60% Subscription Opt-ins", "2.4x ROI within 3 months"],
        "tags": ["E-Commerce", "CRO"]
    },
    {
        "id": 6,
        "title": "Firebirds Restaurant",
        "slug": "portfolio-firebirds.html",
        "image": "https://i.imgur.com/HQGBLer.jpg",
        "type": "Hospitality",
        "challenge": "A premium dining franchise needed to consolidate their multi-location web presence into one cohesive, high-performing site that handled live menu updates and advanced reservation routing.",
        "solution": "We designed an interactive hospitality experience. We integrated a headless CMS so management could alter menus instantly across specific locations, and optimized the entire site architecture for massive local SEO dominance.",
        "results": ["+200% Organic Local Traffic", "Fully Automated Menu Sync", "+30% Direct Reservations"],
        "tags": ["UI/UX Design", "Local SEO"]
    },
    {
        "id": 7,
        "title": "Jamie Graham Law",
        "slug": "portfolio-jamie-graham.html",
        "image": "https://i.imgur.com/T7gm2EM.jpg",
        "type": "Legal Services",
        "challenge": "A highly competitive legal firm was losing high-intent traffic to competitors with stronger SEO. Their existing site was outdated and failed to communicate their authority and track record effectively.",
        "solution": "We rebuilt the platform from the ground up focusing on authoritative design and aggressive technical SEO. We restructured their content silos to target specific high-value case types.",
        "results": ["Page 1 Ranking for 15+ Keywords", "+180% Qualified Leads", "Premium Brand Positioning"],
        "tags": ["SEO", "Web Dev"]
    },
    {
        "id": 8,
        "title": "Lueder",
        "slug": "portfolio-lueder.html",
        "image": "https://i.imgur.com/MHznsaV.jpg",
        "type": "Enterprise Portal",
        "challenge": "A large-scale corporate enterprise possessed fragmented data and multiple outdated web portals that confused stakeholders. They demanded a unified architectural overhaul capable of handling massive secure traffic.",
        "solution": "We deployed a Next.js framework coupled with an advanced headless CMS. We rebuilt the information architecture to be instantly intuitive and secured the endpoints with enterprise-grade protection.",
        "results": ["Consolidated 5 Portals to 1", "Sub-second Load Times", "Zero Security Breaches"],
        "tags": ["CMS", "Next.js"]
    },
    {
        "id": 9,
        "title": "Tibico Health",
        "slug": "portfolio-tibico-health.html",
        "image": "https://i.imgur.com/D4ciMv4.jpg",
        "type": "Health Tech",
        "challenge": "A modern health and wellness brand needed an engaging platform to deliver complex nutritional guides and subscription models without overwhelming the user UX.",
        "solution": "We developed a deeply immersive, educational UI that guides the user step-by-step through their health journey, pairing crisp design with custom scalable backend integrations.",
        "results": ["+50% User Retention", "Seamless Content Delivery", "High Customer Satisfaction"],
        "tags": ["Health Tech", "UI/UX Design"]
    },
    {
        "id": 10,
        "title": "Women's Foundation",
        "slug": "portfolio-womens-foundation.html",
        "image": "https://i.imgur.com/958DvKQ.jpg",
        "type": "Non-Profit",
        "challenge": "A major non-profit needed a commanding digital presence to display their community impact, streamline their outreach programs, and aggressively drive donation metrics.",
        "solution": "We formulated a profound, story-driven UX layout explicitly optimized to generate emotional investment and frictionless donation flows across all devices.",
        "results": ["+110% YoY Donations", "Streamlined Campaign Management", "Global Reach Expanded"],
        "tags": ["Non-Profit", "SEO"]
    },
    {
        "id": 11,
        "title": "Stapende Auto",
        "slug": "portfolio-stapende-auto.html",
        "image": "https://i.imgur.com/JrvsgXo.jpg",
        "type": "Automotive Showcase",
        "challenge": "A high-end automotive dealer faced abysmal lead generation via their online portal due to poor inventory search tools and low-resolution image constraints.",
        "solution": "We engineered a cutting-edge automotive showroom experience, featuring lightning-fast inventory filtering and immersive full-screen galleries that capture buyer intent instantly.",
        "results": ["+300% Inventory Searches", "40% Lead Generation Spike", "Premium Visual Delivery"],
        "tags": ["Auto", "Optimization"]
    },
    {
        "id": 12,
        "title": "Absolute Collagen",
        "slug": "portfolio-absolute-collagen.html",
        "image": "https://i.imgur.com/lxfKiWw.jpg",
        "type": "E-Commerce",
        "challenge": "An explosive beauty brand scaling rapidly needed to maximize their direct-to-consumer recurring revenue through simplified, high-converting subscription UX flows.",
        "solution": "We completely revamped their D2C architecture using data-backed conversion rate optimization techniques, ensuring users naturally gravitated toward long-term subscription loyalty.",
        "results": ["+80% Subscription LTV", "Reduced Churn by 25%", "Record-Breaking Monthly Sales"],
        "tags": ["E-Commerce", "CRO"]
    }
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rayvotech | {title} Case Study</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
    <!-- Phosphor Icons -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body class="theme-aurora">
    
    <div class="cursor-dot" data-cursor-dot></div>
    <div class="cursor-outline" data-cursor-outline></div>

    <nav class="navbar glass-effect">
        <div class="nav-container container">
            <a href="index.html" class="logo">Rayvo<span>tech</span></a>
            <div class="nav-links">
                <a href="about.html">About Us</a>
                <a href="services.html">Services</a>
                <a href="portfolio.html">Portfolio</a>
                <a href="pricing.html">Pricing</a>
                <a href="faqs.html">FAQs</a>
                <a href="contact.html">Contact</a>
            </div>
            <a href="hire.html" class="btn btn-primary">Hire Us</a>
        </div>
    </nav>

    <!-- Project Hero -->
    <section class="hero" style="min-height: 70svh; padding-top: 12rem; padding-bottom: 5rem; position: relative;">
        <!-- Immersed Background Image -->
        <div style="position: absolute; inset: 0; background: url('{image}') top center/cover no-repeat; opacity: 0.15; z-index: -1;"></div>
        <div style="position: absolute; inset: 0; background: linear-gradient(to bottom, transparent, var(--color-bg)); z-index: -1;"></div>

        <div class="container hero-content text-center">
            <div class="y2k-badge reveal-text">{type}</div>
            <h1 class="hero-title reveal-text delay-1" style="font-size: 5rem; margin-bottom: 2rem;">{title}</h1>
            <div class="tech-icons reveal-text delay-2" style="justify-content: center;">
                <span class="tech-badge"><i class="ph ph-check-circle"></i> {tag1}</span>
                <span class="tech-badge"><i class="ph ph-check-circle"></i> {tag2}</span>
            </div>
        </div>
    </section>

    <!-- Case Study Details -->
    <section class="section-padding" style="padding-top: 2rem;">
        <div class="container">
            <!-- Full width Image showcase -->
            <div class="fade-up glass-card" style="height: 600px; border-radius: 20px; background: url('{image}') top center/cover no-repeat; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 6rem; box-shadow: 0 30px 60px rgba(0,0,0,0.5);"></div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; margin-bottom: 6rem;">
                <div class="fade-up">
                    <h2 style="font-size: 2.5rem; color: var(--color-accent); margin-bottom: 1.5rem; display: flex; align-items: center; gap: 1rem;"><i class="ph ph-warning-circle"></i> The Challenge</h2>
                    <p style="font-size: 1.15rem; color: var(--text-secondary); line-height: 1.8;">{challenge}</p>
                </div>
                <div class="fade-up delay-1">
                    <h2 style="font-size: 2.5rem; color: #a855f7; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 1rem;"><i class="ph ph-lightbulb"></i> The Solution</h2>
                    <p style="font-size: 1.15rem; color: var(--text-secondary); line-height: 1.8;">{solution}</p>
                </div>
            </div>

            <!-- The Results -->
            <div class="fade-up delay-2 glass-box text-center" style="padding: 5rem 3rem;">
                <h2 style="font-size: 3rem; margin-bottom: 4rem;">The Results</h2>
                <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 2rem;">
                    <div>
                        <span class="neon-text">{res1}</span>
                    </div>
                    <div>
                        <span class="neon-text" style="color: #00E6F0;">{res2}</span>
                    </div>
                    <div>
                        <span class="neon-text" style="color: #a855f7;">{res3}</span>
                    </div>
                </div>
            </div>

            <div class="text-center" style="margin-top: 6rem;">
                <a href="{next_slug}" class="btn btn-outline btn-lg">View Next Project <i class="ph ph-arrow-right"></i></a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer" id="contact">
        <div class="container">
            <div class="massive-cta fade-up">
                <div class="cta-content">
                    <h2 style="color: var(--text-inverse); font-size: 4rem;">Ready for your own <br> success story?</h2>
                </div>
                <div class="cta-action" style="margin-top: 3rem;">
                    <a href="hire.html" class="btn btn-outline btn-lg" style="border-color: var(--color-dominant); color: var(--color-dominant);">Start the Conversation <i class="ph ph-arrow-right"></i></a>
                </div>
            </div>
            
            <div class="footer-bottom">
                <div class="footer-brand">
                    <a href="index.html" class="logo">Rayvo<span>tech</span></a>
                    <p>Delivering clarity, creativity, and conversion.</p>
                </div>
                <div class="footer-links">
                    <div class="link-group">
                        <h4>Company</h4>
                        <a href="about.html">About Us</a>
                        <a href="services.html">Services</a>
                        <a href="portfolio.html">Our Work</a>
                        <a href="pricing.html">Pricing</a>
                        <a href="faqs.html">FAQs</a>
                        <a href="contact.html">Contact</a>
                    </div>
                </div>
            </div>
            <div class="footer-legal">
                <p>&copy; 2026 Rayvotech Digital. Built with passion.</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>"""

# 1. GENERATE THE 12 HTML FILES
for i, p in enumerate(projects):
    next_index = (i + 1) % len(projects)
    next_slug = projects[next_index]['slug']
    
    html_content = template.format(
        title=p['title'],
        type=p['type'],
        image=p['image'],
        challenge=p['challenge'],
        solution=p['solution'],
        tag1=p['tags'][0],
        tag2=p['tags'][1],
        res1=p['results'][0],
        res2=p['results'][1],
        res3=p['results'][2],
        next_slug=next_slug
    )
    
    with open(p['slug'], 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Generated 12 case study pages successfully.")

# 2. PATCH PORTFOLIO.HTML TO ADD LINKS TO THE NEW PAGES
with open('portfolio.html', 'r', encoding='utf-8') as f:
    port_html = f.read()

# For each project, we want to inject a 'View Case Study' button at the bottom of the testimonial-card's padding wrapper
for p in projects:
    # A bit dangerous, but we know each project has an <h3> containing the title.
    # The structure: 
    # <div style="padding: 2.5rem;">
    #   <h3 ...>Title</h3>
    #   ...
    #   <div class="tech-icons" ...> ... </div>
    # </div>
    # We can inject the button right after the tech-icons div for that specific project.
    
    # We'll use regex to find the block for the specific title
    pattern = rf"(<h3[^>]*>{p['title']}</h3>[\s\S]*?<div class=\"tech-icons\"[^>]*>[\s\S]*?</div>)"
    replacement = rf"\1\n                        <a href=\"{p['slug']}\" class=\"btn btn-primary\" style=\"margin-top: 1.5rem; display: inline-block; width: 100%; text-align: center;\">View Case Study</a>"
    port_html = re.sub(pattern, replacement, port_html)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(port_html)

print("Patched portfolio.html with links to case studies.")

# 3. PATCH INDEX.HTML
# Index has 4 specifically featured projects
with open('index.html', 'r', encoding='utf-8') as f:
    idx_html = f.read()

# We need to replace `href="portfolio.html"` with the specific slug for those 4 projects in the gallery.
# However, `index.html` structure:
# <div class="project-overlay glass-effect">
#     <a href="portfolio.html" class="view-btn btn-primary">View Details</a>
# </div>
# <div style="margin-top: 1.5rem; padding-left: 0.5rem;">
#     <h3 style="...">Body Fit Training</h3>

for p in projects:
    # Look for the block containing `href="portfolio.html"` followed somewhat shortly by the Title.
    pattern2 = rf"(<a href=\")portfolio\.html(\"[^>]*>View Details</a>[\s\S]*?<h3[^>]*>{p['title']}</h3>)"
    idx_html = re.sub(pattern2, rf"\1{p['slug']}\2", idx_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_html)

print("Patched index.html homepage gallery links.")
