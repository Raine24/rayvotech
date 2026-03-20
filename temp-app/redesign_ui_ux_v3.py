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
            <h1 class="hero-title reveal-text delay-1" style="font-size: 5rem; line-height: 1.1;">Human <br> <span class="text-gradient liquid-text">Centered.</span></h1>
            <p class="hero-subtitle reveal-text delay-2" style="max-width: 800px; margin: 0 auto; font-size: 1.25rem;">
                At Rayvotech, we believe great design is never an accident. It's the result of deep thinking, careful research, and obsessive attention to detail. Our UI/UX design service exists at the intersection of human psychology and digital craft &mdash; creating interfaces that don't just look world-class but feel effortless to use.
            </p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 2rem 0 6rem 0;">
        <div class="container" style="max-width: 1200px;">
            
            <div class="fade-up" style="max-width: 900px; margin: 0 auto 6rem auto; text-align: center;">
                <p style="font-size: 1.35rem; line-height: 1.8; color: var(--text-secondary);">
                    Whether you're building a brand new product from scratch or untangling a frustrating user experience, we bring clarity, structure, and visual excellence to everything we touch.
                </p>
            </div>

            <!-- Massive Image Showcase -->
            <div class="fade-up delay-1" style="width: 100%; height: 600px; border-radius: 32px; overflow: hidden; margin-bottom: 8rem; box-shadow: 0 40px 80px rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.05); position: relative;">
                <img src="https://i.imgur.com/l5BnUoy.jpg" alt="UI/UX Visual Architecture" style="width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 50%; background: linear-gradient(to top, rgba(10,10,14,0.9), transparent); pointer-events: none;"></div>
            </div>

            <!-- Our Expertise (Bento Grid) -->
            <div style="text-align: center; margin-bottom: 4rem;">
                <h2 style="font-size: 3rem;">Digital Craftsmanship</h2>
            </div>
            
            <div class="bento-grid fade-up delay-1" style="margin-bottom: 8rem;">
                
                <!-- Card 1: User Research -->
                <div class="bento-item glass-card beam-card" style="grid-column: span 2; padding: 4rem; display: flex; flex-direction: column; justify-content: center; position: relative; overflow: hidden;">
                    <div style="position: absolute; top: -100px; right: -100px; width: 300px; height: 300px; background: rgba(168, 85, 247, 0.15); filter: blur(100px); border-radius: 50%;"></div>
                    <div class="card-icon chrome-icon" style="margin-bottom: 2rem; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem;"><i class="ph ph-users"></i></div>
                    <h3 style="font-size: 2.5rem; margin-bottom: 1.5rem;">User Research</h3>
                    <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2rem;">
                        Every great design decision starts with understanding people. Before we sketch a single wireframe or choose a single color, we dig deep into who your users are, what they need, and where they're getting stuck.
                    </p>
                    <p style="font-size: 1.15rem; color: var(--text-primary); font-weight: 500; margin: 0; padding-left: 1rem; border-left: 3px solid var(--color-accent);">
                        We don't design for trends. We design for your users.
                    </p>
                </div>

                <!-- Card 2: Wireframing -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #3b82f6, #06b6d4); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-blueprint"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Wireframing</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin-bottom: 1.5rem;">
                        Think of wireframes as the blueprint before the build. We map out every screen, every flow, and every interaction before a single line of code is written.
                    </p>
                    <p style="font-size: 1rem; color: var(--text-primary); font-weight: 600; margin: 0;">Clean. Logical. Intentional.</p>
                </div>

                <!-- Card 3: Prototyping -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #f43f5e, #fb923c); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-cursor-click"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Prototyping</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin-bottom: 1.5rem;">
                        Seeing is believing. We bring your product to life with interactive prototypes that look and feel like the real thing &mdash; long before development begins.
                    </p>
                    <p style="font-size: 1rem; color: var(--text-primary); font-weight: 600; margin: 0;">Click through it. Feel it. Approve it.</p>
                </div>

                <!-- Card 4: Design Systems -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #10b981, #3b82f6); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-stack"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Design Systems</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin-bottom: 1.5rem;">
                        We build comprehensive design systems &mdash; reusable components and scalable libraries that keep your product visually cohesive at every touchpoint.
                    </p>
                    <p style="font-size: 1rem; color: var(--text-primary); font-weight: 600; margin: 0;">An investment in your brand's future.</p>
                </div>

                <!-- Card 5: Mobile App Design -->
                <div class="bento-item glass-card beam-card" style="grid-column: span 2; padding: 4rem; display: flex; flex-direction: column; justify-content: center; position: relative; overflow: hidden; border-color: rgba(0, 230, 240, 0.3);">
                    <div style="position: absolute; bottom: -100px; left: -100px; width: 300px; height: 300px; background: rgba(0, 230, 240, 0.15); filter: blur(100px); border-radius: 50%;"></div>
                    <div class="card-icon chrome-icon" style="margin-bottom: 2rem; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem;"><i class="ph ph-device-mobile"></i></div>
                    <h3 style="font-size: 2.5rem; margin-bottom: 1.5rem;">Mobile App Design</h3>
                    <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2rem;">
                        Mobile is no longer secondary &mdash; it's often the primary experience. Our mobile app design service covers both iOS and Android, with deep attention to platform-specific design guidelines, touch interaction patterns, and performance considerations. The result is a native-feeling app experience that users love opening every single day.
                    </p>
                    <p style="font-size: 1.15rem; color: var(--color-accent); font-weight: 500; margin: 0;">
                        Thumb-friendly. Pixel-perfect. Built for the way people actually use their phones.
                    </p>
                </div>

                <!-- Card 6: Usability Testing -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem; background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(0, 230, 240, 0.05));">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #8b5cf6, #d946ef); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-flask"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Usability Testing</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin-bottom: 1.5rem;">
                        We don't guess &mdash; we test. Once a prototype or live product is in place, we put it in front of real users and watch how they interact with it. What confuses them? Where do they drop off? What delights them?
                    </p>
                    <p style="font-size: 1rem; color: var(--text-primary); font-weight: 600; margin: 0;">Good design is never finished.</p>
                </div>
            </div>

            <!-- Two Column: Process & Value -->
            <div class="fade-up" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(450px, 1fr)); gap: 4rem; margin-bottom: 8rem;">
                
                <!-- Our Process -->
                <div>
                    <h2 style="font-size: 2.5rem; margin-bottom: 3rem;">Our Process</h2>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 2rem;">
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start; padding-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.05);">
                            <div style="width: 45px; height: 45px; border-radius: 12px; background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(0, 230, 240, 0.2)); color: var(--text-primary); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; font-weight: bold; flex-shrink: 0;">1</div>
                            <div>
                                <strong style="display: block; font-size: 1.25rem; font-family: 'Space Grotesk', sans-serif; letter-spacing: 1px; text-transform: uppercase; color: var(--color-accent); margin-bottom: 0.5rem;">Discover</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6; font-size: 1.1rem;">We learn your business, your users, and your goals inside out.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start; padding-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.05);">
                            <div style="width: 45px; height: 45px; border-radius: 12px; background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(0, 230, 240, 0.2)); color: var(--text-primary); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; font-weight: bold; flex-shrink: 0;">2</div>
                            <div>
                                <strong style="display: block; font-size: 1.25rem; font-family: 'Space Grotesk', sans-serif; letter-spacing: 1px; text-transform: uppercase; color: var(--color-accent); margin-bottom: 0.5rem;">Define</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6; font-size: 1.1rem;">We map user flows, information architecture, and product requirements.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start; padding-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.05);">
                            <div style="width: 45px; height: 45px; border-radius: 12px; background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(0, 230, 240, 0.2)); color: var(--text-primary); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; font-weight: bold; flex-shrink: 0;">3</div>
                            <div>
                                <strong style="display: block; font-size: 1.25rem; font-family: 'Space Grotesk', sans-serif; letter-spacing: 1px; text-transform: uppercase; color: var(--color-accent); margin-bottom: 0.5rem;">Design</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6; font-size: 1.1rem;">We craft wireframes, visual designs, and interactive prototypes.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start; padding-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.05);">
                            <div style="width: 45px; height: 45px; border-radius: 12px; background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(0, 230, 240, 0.2)); color: var(--text-primary); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; font-weight: bold; flex-shrink: 0;">4</div>
                            <div>
                                <strong style="display: block; font-size: 1.25rem; font-family: 'Space Grotesk', sans-serif; letter-spacing: 1px; text-transform: uppercase; color: var(--color-accent); margin-bottom: 0.5rem;">Test</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6; font-size: 1.1rem;">We validate with real users and refine based on findings.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 45px; height: 45px; border-radius: 12px; background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(0, 230, 240, 0.2)); color: var(--text-primary); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; font-weight: bold; flex-shrink: 0;">5</div>
                            <div>
                                <strong style="display: block; font-size: 1.25rem; font-family: 'Space Grotesk', sans-serif; letter-spacing: 1px; text-transform: uppercase; color: var(--color-accent); margin-bottom: 0.5rem;">Deliver</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6; font-size: 1.1rem;">We hand off production-ready designs with full documentation.</span>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- Immersion Block -->
                <div style="display: flex; align-items: center;">
                    <div class="glass-card beam-card" style="padding: 4rem; background: rgba(10,10,14,0.6); position: relative; overflow: hidden; border-radius: 32px;">
                        <i class="ph ph-magic-wand" style="font-size: 3rem; color: var(--color-accent); margin-bottom: 1.5rem; display: block;"></i>
                        <h3 style="font-size: 2.25rem; margin-bottom: 1.5rem; line-height: 1.3;">Designing at the intersection of psychology &amp; craft.</h3>
                        <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2rem;">
                            Intuitive experiences never happen by chance. We leverage modern psychological principles, usability metrics, and behavioral analysis to eliminate friction from every corner of your platform.
                        </p>
                        <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary);">
                            We don't just build interfaces; we architect environments that people genuinely love being in. Let’s make something beautiful.
                        </p>
                    </div>
                </div>

            </div>

            <!-- Why Us / CTA -->
            <div class="glass-card fade-up" style="padding: 6rem; text-align: center; background: linear-gradient(135deg, rgba(0, 230, 240, 0.08), rgba(168, 85, 247, 0.08)); border-radius: 32px; border: 1px solid rgba(255,255,255,0.05); position: relative; overflow: hidden;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, var(--color-accent), transparent);"></div>
                <h2 style="font-size: 3.5rem; margin-bottom: 2rem;">Why Rayvotech</h2>
                <p style="font-size: 1.35rem; line-height: 1.8; color: var(--text-secondary); max-width: 900px; margin: 0 auto 3rem auto;">
                    We're not a design factory churning out templates. Every project at Rayvotech is a bespoke experience &mdash; designed from scratch, tailored to your brand, and built around your users. Our team brings together creative vision and strategic thinking to produce work that is as effective as it is beautiful.
                </p>
                <p style="font-size: 1.5rem; color: var(--text-primary); font-weight: 500; margin-bottom: 4rem;">
                    When you choose Rayvotech for UI/UX, you're choosing a partner who cares about your product as much as you do.
                </p>
                
                <h3 style="font-size: 2.5rem; margin-bottom: 1rem; color: var(--color-accent);">Ready to elevate your user experience?</h3>
                <p style="color: var(--text-secondary); font-size: 1.35rem; margin-bottom: 3.5rem;">Let's design something your users will never forget.</p>
                
                <a href="hire.html" class="btn btn-primary btn-lg" style="padding: 1.25rem 3rem; font-size: 1.25rem; border-radius: 50px;">Start Your Project &rarr;</a>
            </div>

        </div>
    </section>
    """

    final_content = content[:nav_end_idx] + "\n" + new_body + "\n    " + content[footer_start_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("UI/UX page fundamentally rebuilt to Awwwards standards.")
else:
    print("Could not find boundaries for overhaul.")
