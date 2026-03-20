import re

html_file = 'service-ui-ux-design.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

nav_end_idx = content.find('</nav>') + len('</nav>')
footer_start_idx = content.find('<!-- Footer -->')

if nav_end_idx > 6 and footer_start_idx != -1:
    new_body = """
    <!-- Page Header -->
    <section class="hero" id="hero" style="min-height: auto; padding-top: 10rem; padding-bottom: 3rem;">
        <div class="container hero-content text-center">
            <div class="y2k-badge reveal-text">UI/UX DESIGN</div>
            <h1 class="hero-title reveal-text delay-1" style="font-size: 5rem; line-height: 1.1;">UI/UX Design <br> <span class="text-gradient liquid-text">Services.</span></h1>
            <p class="hero-subtitle reveal-text delay-2" style="max-width: 800px; margin: 0 auto; font-size: 1.25rem;">
                At Rayvotech, we believe great design is never an accident. It's the result of deep thinking, careful research, and obsessive attention to detail. Our UI/UX design service exists at the intersection of human psychology and digital craft &mdash; creating interfaces that don't just look world-class but feel effortless to use.
            </p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 2rem 0 6rem 0;">
        <div class="container" style="max-width: 1200px;">
            
            <div class="fade-up" style="max-width: 800px; margin: 0 auto 5rem auto; text-align: center;">
                <p style="font-size: 1.25rem; line-height: 1.8; color: var(--text-secondary);">
                    Whether you're building a brand new product from scratch or untangling a frustrating user experience, we bring clarity, structure, and visual excellence to everything we touch.
                </p>
            </div>

            <!-- Image Section -->
            <div class="fade-up delay-1" style="width: 100%; height: 500px; border-radius: 24px; overflow: hidden; margin-bottom: 6rem; box-shadow: 0 30px 60px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.05); position: relative;">
                <img src="https://i.imgur.com/l5BnUoy.jpg" alt="UI/UX Visual Design" style="width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>

            <!-- Expertise Grid -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2rem; margin-bottom: 8rem;" class="fade-up delay-2">
                
                <!-- Research -->
                <div class="glass-card" style="padding: 3rem; border-radius: 20px;">
                    <h3 style="font-size: 1.75rem; color: var(--color-accent); margin-bottom: 1rem;">User Research</h3>
                    <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
                        Every great design decision starts with understanding people. Before we sketch a single wireframe or choose a single color, we dig deep into who your users are, what they need, and where they're getting stuck. Through interviews, surveys, behavioral analysis, and competitive audits, we build a clear picture of your audience &mdash; so every design choice we make is grounded in reality, not assumption.
                    </p>
                    <p style="color: var(--text-primary); font-weight: 600; margin: 0;">We don't design for trends. We design for your users.</p>
                </div>

                <!-- Wireframing -->
                <div class="glass-card" style="padding: 3rem; border-radius: 20px;">
                    <h3 style="font-size: 1.75rem; color: var(--color-accent); margin-bottom: 1rem;">Wireframing</h3>
                    <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
                        Think of wireframes as the blueprint before the build. We map out every screen, every flow, and every interaction before a single line of code is written. This stage saves time, reduces costly revisions, and ensures everyone &mdash; you, your team, and our developers &mdash; is aligned on exactly what's being built and why.
                    </p>
                    <p style="color: var(--text-primary); font-weight: 600; margin: 0;">Clean. Logical. Intentional.</p>
                </div>

                <!-- Prototyping -->
                <div class="glass-card" style="padding: 3rem; border-radius: 20px;">
                    <h3 style="font-size: 1.75rem; color: var(--color-accent); margin-bottom: 1rem;">Prototyping</h3>
                    <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
                        Seeing is believing. We bring your product to life with interactive prototypes that look and feel like the real thing &mdash; long before development begins. This means you can test the experience, gather feedback, and make confident decisions early, when changes are still easy and affordable to make.
                    </p>
                    <p style="color: var(--text-primary); font-weight: 600; margin: 0;">Click through it. Feel it. Approve it. Then we build it.</p>
                </div>

                <!-- Design Systems -->
                <div class="glass-card" style="padding: 3rem; border-radius: 20px;">
                    <h3 style="font-size: 1.75rem; color: var(--color-accent); margin-bottom: 1rem;">Design Systems</h3>
                    <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
                        Consistency is the hallmark of a professional brand. We build comprehensive design systems &mdash; reusable components, typography scales, color libraries, spacing rules, and interaction patterns &mdash; that keep your product looking sharp and cohesive at every touchpoint, no matter how much it grows.
                    </p>
                    <p style="color: var(--text-primary); font-weight: 600; margin: 0;">A design system isn't just a deliverable. It's an investment in your brand's future.</p>
                </div>

                <!-- Usability -->
                <div class="glass-card" style="padding: 3rem; border-radius: 20px;">
                    <h3 style="font-size: 1.75rem; color: var(--color-accent); margin-bottom: 1rem;">Usability Testing</h3>
                    <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
                        We don't guess &mdash; we test. Once a prototype or live product is in place, we put it in front of real users and watch how they interact with it. What confuses them? Where do they drop off? What delights them? The insights we gather feed directly back into the design, resulting in a product that gets sharper with every iteration.
                    </p>
                    <p style="color: var(--text-primary); font-weight: 600; margin: 0;">Good design is never finished. It's always improving.</p>
                </div>

                <!-- Mobile App -->
                <div class="glass-card" style="padding: 3rem; border-radius: 20px;">
                    <h3 style="font-size: 1.75rem; color: var(--color-accent); margin-bottom: 1rem;">Mobile App Design</h3>
                    <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
                        Mobile is no longer secondary &mdash; it's often the primary experience. Our mobile app design service covers both iOS and Android, with deep attention to platform-specific design guidelines, touch interaction patterns, and performance considerations. The result is a native-feeling app experience that users love opening every single day.
                    </p>
                    <p style="color: var(--text-primary); font-weight: 600; margin: 0;">Thumb-friendly. Pixel-perfect. Built for the way people actually use their phones.</p>
                </div>

            </div>

            <!-- Process -->
            <div class="fade-up" style="margin-bottom: 8rem; text-align: center;">
                <div class="y2k-badge" style="margin-bottom: 1.5rem;">OUR PROCESS</div>
                <div class="glass-card" style="display: inline-block; padding: 4rem; text-align: left; border-radius: 24px;">
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 2rem;">
                        <li style="font-size: 1.25rem;"><strong style="color: var(--color-accent); margin-right: 1rem;">1. Discover &mdash;</strong> <span style="color: var(--text-secondary);">We learn your business, your users, and your goals inside out.</span></li>
                        <li style="font-size: 1.25rem;"><strong style="color: var(--color-accent); margin-right: 1rem;">2. Define &mdash;</strong> <span style="color: var(--text-secondary);">We map user flows, information architecture, and product requirements.</span></li>
                        <li style="font-size: 1.25rem;"><strong style="color: var(--color-accent); margin-right: 1rem;">3. Design &mdash;</strong> <span style="color: var(--text-secondary);">We craft wireframes, visual designs, and interactive prototypes.</span></li>
                        <li style="font-size: 1.25rem;"><strong style="color: var(--color-accent); margin-right: 1rem;">4. Test &mdash;</strong> <span style="color: var(--text-secondary);">We validate with real users and refine based on findings.</span></li>
                        <li style="font-size: 1.25rem;"><strong style="color: var(--color-accent); margin-right: 1rem;">5. Deliver &mdash;</strong> <span style="color: var(--text-secondary);">We hand off production-ready designs with full documentation.</span></li>
                    </ul>
                </div>
            </div>

            <!-- Why Us / CTA -->
            <div class="glass-card fade-up" style="padding: 5rem; text-align: center; background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(0, 230, 240, 0.1)); border-radius: 24px;">
                <h2 style="font-size: 3rem; margin-bottom: 2rem;">Why Rayvotech</h2>
                <p style="font-size: 1.25rem; line-height: 1.8; color: var(--text-secondary); max-width: 900px; margin: 0 auto 2rem auto;">
                    We're not a design factory churning out templates. Every project at Rayvotech is a bespoke experience &mdash; designed from scratch, tailored to your brand, and built around your users. Our team brings together creative vision and strategic thinking to produce work that is as effective as it is beautiful.
                </p>
                <p style="font-size: 1.35rem; color: var(--text-primary); font-weight: 600; margin-bottom: 4rem;">
                    When you choose Rayvotech for UI/UX, you're choosing a partner who cares about your product as much as you do.
                </p>
                
                <h3 style="font-size: 2.25rem; margin-bottom: 0.5rem;">Ready to elevate your user experience?</h3>
                <p style="color: var(--color-accent); font-size: 1.25rem; margin-bottom: 3rem;">Let's design something your users will never forget.</p>
                
                <a href="hire.html" class="btn btn-primary btn-lg">Start Your Project &rarr;</a>
            </div>

        </div>
    </section>
    """

    final_content = content[:nav_end_idx] + "\n" + new_body + "\n    " + content[footer_start_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("UI/UX layout successfully updated with new copy.")
else:
    print("Could not find boundaries.")
