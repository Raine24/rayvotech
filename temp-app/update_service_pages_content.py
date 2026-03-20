import re
import os

WRITEUPS = {
    "service-website-design.html": """Your website is the most powerful sales tool your business owns. Before a potential client picks up the phone, sends an email, or walks through your door, they have already visited your website and made a judgment about who you are, what you offer, and whether you are worth their time and money. That judgment happens in less than three seconds. Three seconds to earn trust, communicate value, and create a desire to learn more. That is the weight your website carries every single day — and it is why getting it right is not optional.

At Rayvotech, we design custom, visually stunning websites that do exactly that. We don't just build pages that look good on a screen. We craft digital experiences that capture attention, communicate your brand's unique value, and guide visitors naturally toward becoming paying customers. Every project we take on starts with a deep understanding of your business — who you are, who your audience is, what makes you different, and what you want your website to ultimately achieve. That clarity drives every creative decision we make.

We do not do templates. We never have and we never will. Templates are built for everyone, which means they are built for no one in particular. Your brand is not generic and your website should not be either. Every website we design is built from scratch, conceived and crafted specifically for your brand identity, your target audience, and your business goals. The result is a website that feels entirely and unmistakably yours — one that stands apart from every competitor in your space.

Our design process is rooted in three things: strategy, creativity, and an obsession with detail. We begin by asking the right questions. Who is your ideal customer and what do they care about most? What action do you want visitors to take when they land on your site? What emotions should your website evoke? What does success actually look like for your business online? These are not surface-level questions. They shape the entire architecture of your website before we ever open a design tool.

From there, our creative team gets to work. We develop a visual language that is uniquely yours — a combination of typography, color, imagery, layout, and motion that communicates your brand personality with precision and confidence. We consider every element on every page with the same level of care, because in design, the details are not the details — the details are the design.

Every website we build is fully responsive across all devices. Your audience is browsing on phones, tablets, laptops, and desktops, often switching between them multiple times in a single day. Your website needs to look and function perfectly on every single one of those screens, without compromise. We design mobile-first, ensuring that the smallest screen experience is just as polished and intentional as the largest one.

Performance is as important to us as aesthetics. A beautiful website that loads slowly is a website that loses customers. Studies consistently show that a one-second delay in page load time can reduce conversions by up to seven percent. We optimize every website we build for speed — compressing assets, streamlining code, and leveraging modern performance techniques to ensure your site loads fast and keeps visitors engaged from the first moment.

We also build with accessibility in mind, ensuring your website meets WCAG compliance standards so that every visitor, regardless of ability, can navigate and engage with your content comfortably. Accessibility is not just the right thing to do — it expands your audience and signals to search engines that your site is built with quality and care.

Whether you need a single high-converting landing page, a multi-page corporate website, a portfolio, or a full e-commerce experience, Rayvotech delivers design that works as hard as you do. We bring your brand to life online in a way that is bold, intentional, and impossible to ignore.""",

    "service-ui-ux-design.html": """There is a version of your digital product that your users love so much they tell other people about it. A version where everything is exactly where they expect it to be. Where every interaction feels smooth and satisfying. Where the path from landing on your page to completing a purchase, booking a call, or signing up for your service feels so natural that they barely notice they are being guided at all. That version exists. Getting there is what our UI/UX design service is built to do.

At Rayvotech, we believe that design is not decoration — it is problem solving. Our UI/UX service goes far beyond making things look good. We architect the entire experience your users have when they interact with your digital product, from the very first moment they arrive to the moment they complete the action you most want them to take. Every element of that journey is studied, considered, tested, and refined until it works exactly as it should.

UI stands for User Interface — the visual layer that users interact with directly. Buttons, menus, forms, cards, icons, typography, color, spacing. Every visual component that makes up the surface of your product. UX stands for User Experience — the logic, structure, and flow beneath that surface. How information is organized. How users move from one section to another. How friction is identified and eliminated. How the product makes people feel at every stage of their interaction with it. We design both, together, because they cannot be separated. A beautiful interface built on a confusing structure will still frustrate your users. A logical structure wrapped in a poor visual design will still lose their trust.

Our process begins with research. We do not make assumptions about what your users want or need. We study them. We develop detailed user personas that represent your real audience — their goals, their frustrations, their behaviors, and their expectations. We map out every journey a user might take through your product, identifying where they are likely to get confused, where they are likely to drop off, and where the greatest opportunities to delight them exist.

From that research, we build information architecture — a clear and logical blueprint of how your content and features should be organized to serve your users most effectively. This is the skeleton of your product, and getting it right at this stage saves enormous time and cost later in the process.

With the architecture established, we move into wireframing. Wireframes are simplified, structural representations of each screen in your product. They show layout and flow without the distraction of color or visual detail, allowing us to focus entirely on how things work before we decide how they look. This is where we solve the hard problems — where we test different approaches, eliminate confusion, and ensure that every screen serves a clear purpose in the user's journey.

Once wireframes are approved, we build interactive prototypes that simulate the real experience of using your product. These prototypes are tested with real users, generating feedback that is incorporated into the design before development begins. This testing phase is one of the most valuable parts of our process, because it catches problems early when they are cheap to fix rather than late when they are expensive.

The final UI design layer brings everything to life visually — applying your brand's color system, typography, imagery, and motion to create an interface that is not only functional but genuinely beautiful. We build design systems that ensure consistency across every screen and every interaction, and we document everything so your development team can build with confidence and your brand can scale without losing coherence.

Investing in UI/UX design is one of the highest-return decisions a business can make. Companies that prioritize user experience consistently outperform those that do not — with higher conversion rates, lower customer acquisition costs, stronger brand loyalty, and better word-of-mouth. In a digital landscape where your competitors are just one click away, the experience you deliver is your most powerful differentiator.""",

    "service-web-development.html": """An idea is only as powerful as its execution. You can have the most compelling brand, the most beautiful design, and the most strategic content in your industry — but if the product underneath it is slow, buggy, or built on a fragile foundation, none of that other work will save you. Development is where vision becomes reality, and at Rayvotech, we take that responsibility seriously.

Our development team builds fast, scalable, and rock-solid digital products — websites, web applications, and mobile apps — that are engineered to perform under pressure and grow alongside your business. We work with modern, industry-leading technologies and frameworks, writing clean, well-structured code that is easy to maintain, easy to scale, and built to last. We do not take shortcuts. We do not accumulate technical debt. We build things right the first time because we know that the cost of doing it wrong compounds over time.

We are a full-stack development team, which means we handle every layer of your product. On the front end, we build the interfaces your users see and interact with — pixel-perfect implementations of your approved designs, brought to life with smooth animations, responsive layouts, and interactions that feel natural and polished. On the back end, we build the infrastructure that powers everything — databases, servers, APIs, authentication systems, business logic, and integrations with the external tools and platforms your business depends on.

Our core technology stack includes React and Next.js for front-end development, giving us the ability to build everything from simple marketing websites to complex, data-driven web applications with outstanding performance and SEO capabilities. For back-end development, we work with Node.js and a range of databases and cloud infrastructure solutions, selecting the right tools for each project based on its specific requirements rather than defaulting to a one-size-fits-all approach.

E-commerce is a particular area of strength for us. We build online stores that are fast, secure, and optimized for conversion — with seamless checkout experiences, reliable payment gateway integrations, inventory management, and the performance standards that modern shoppers expect. Whether you are launching your first product or managing a catalog of thousands, we build e-commerce solutions that scale.

Every product we deliver is rigorously tested before it goes live. We test across browsers, devices, and screen sizes to ensure a consistent experience for every user regardless of how they access your product. We conduct performance testing to ensure fast load times under real-world conditions. We conduct security testing to identify and address vulnerabilities before they can be exploited. We do not consider a project complete until it meets the highest standards across every one of these dimensions.

We also specialize in integrations — connecting your digital product to the tools and platforms that power your business operations. CRMs, email marketing platforms, payment processors, analytics tools, booking systems, third-party APIs — we have experience integrating a wide range of external services and we approach every integration with the same attention to reliability and performance that we bring to everything else we build.

After delivery, we provide full documentation so your team can understand, manage, and build upon what we have created. We offer ongoing support and maintenance to keep your product running smoothly, address any issues that arise, and help you evolve and expand your product over time. When you work with Rayvotech on development, you are not just getting a product — you are getting a long-term technical partner.""",

    "service-seo-growth.html": """You could have the most beautifully designed, perfectly developed website in your industry — and if nobody can find it, it will not grow your business. Visibility is the foundation of everything. Without it, your website is a billboard in the middle of a forest. Search Engine Optimization is the discipline of making sure your ideal customers can find you exactly when they are looking for what you offer, and at Rayvotech, we approach it with the same strategic depth and technical rigor that we bring to every other service we provide.

SEO is not a quick fix. It is not a set of tricks or hacks. It is not something you do once and forget about. It is a long-term investment in the organic visibility of your business — one that, when done correctly, compounds over time and delivers some of the highest return on investment of any digital marketing activity. The brands that dominate search results in their categories did not get there by accident. They got there through consistent, strategic, technically sound SEO work. That is exactly what we deliver.

Our SEO process begins with a comprehensive audit of your current digital presence. We examine your website's technical health — crawlability, indexability, site speed, mobile performance, structured data, and more. We analyze your existing content and how well it aligns with what your target audience is actually searching for. We assess your backlink profile and your domain authority relative to your competitors. We identify every gap, every opportunity, and every obstacle standing between you and the rankings your business deserves.

From that audit, we build a clear and prioritized SEO strategy — a roadmap that shows exactly what needs to be done, in what order, and why. We do not overwhelm you with jargon or bury the real work in vanity metrics. We focus on the things that actually move rankings and drive qualified traffic to your website.

Keyword research is the cornerstone of our content strategy. We go deep into understanding the exact language your target audience uses when they search for the products, services, or information you provide. We identify high-value keywords with strong commercial intent, assess the competition for each, and build a targeting strategy that gives you the best possible path to ranking for the terms that will actually grow your business. We look beyond the obvious high-volume keywords to find the specific, intent-rich search queries where you can gain traction fastest and build from there.

On-page optimization ensures that every page of your website is structured in a way that search engines can understand and reward. We optimize your meta titles and descriptions, header structure, image alt text, internal linking, URL structure, and content depth. We ensure that every page has a clear purpose, a clear target keyword, and content that genuinely serves the needs of both your users and the search engines indexing your site.

Technical SEO addresses the infrastructure beneath your content. Site speed, Core Web Vitals, mobile responsiveness, crawl efficiency, canonical tags, schema markup, XML sitemaps, and more. These technical factors have a direct impact on how search engines crawl, index, and rank your website, and we leave none of them unaddressed.

Content strategy is where we help you build the authority that sustains long-term rankings. We identify the topics your audience cares about, the questions they are asking, and the content gaps your competitors have left open. We develop a content plan that positions your brand as the most credible and helpful voice in your space — generating traffic, building trust, and earning the backlinks that signal to search engines that your website deserves to rank.

We track everything, report clearly, and communicate what the numbers actually mean for your business. Every month you will know exactly where your rankings stand, how your traffic is growing, where your leads are coming from, and what we are doing next to keep the momentum building."""
}

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f in WRITEUPS]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Locate the <section class="section-padding"> block which contains the old card layout
    # and replace its content with an elegant article layout.
    match = re.search(r'(<!-- Services Detailed -->\s*<section class="section-padding">\s*<div class="container".*?>)(.*?)(</section>)', content, re.DOTALL)
    if match:
        paragraphs = WRITEUPS[f].strip().split('\n\n')
        article_html = '\\n'.join([f'<p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2rem;">{p.strip()}</p>' for p in paragraphs])
        
        replacement = f'''{match.group(1)}
        <div class="article-content fade-up" style="max-width: 900px; margin: 0 auto; background: rgba(255,255,255,0.03); padding: 4rem; border-radius: 24px; border: 1px solid rgba(255,255,255,0.08);">
            {article_html}
            <div style="margin-top: 4rem; text-align: center;">
                <a href="hire.html" class="btn btn-primary btn-lg">Start Your Project <i class="ph ph-arrow-right"></i></a>
            </div>
        </div>
    </div>
{match.group(3)}'''
        
        content = content[:match.start()] + replacement + content[match.end():]
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        print(f"Could not find section to replace in {f}")
