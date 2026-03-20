import re

html_file = 'about.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

nav_end_idx = content.find('</nav>') + len('</nav>')
footer_start_idx = content.find('<!-- Legacy CTA & Footer -->')

if nav_end_idx > 6 and footer_start_idx != -1:
    new_body = """
    <!-- Page Header (Who We Are) -->
    <section class="hero" id="hero" style="min-height: auto; padding-top: 12rem; padding-bottom: 5rem;">
        <div class="container hero-content text-center">
            <div class="y2k-badge reveal-text" style="background: rgba(255, 255, 255, 0.05); border-color: rgba(255, 255, 255, 0.1); color: var(--text-secondary);">ABOUT RAYVOTECH</div>
            <h1 class="hero-title reveal-text delay-1" style="font-size: 6rem; line-height: 1.05; letter-spacing: -2px; margin-bottom: 2rem;">
                Built for <br> <span class="text-gradient liquid-text" style="background: linear-gradient(to right, #ffffff, #888888); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Excellence.</span>
            </h1>
            <p class="hero-subtitle reveal-text delay-2" style="max-width: 800px; margin: 0 auto; font-size: 1.35rem; color: var(--text-secondary); line-height: 1.6;">
                We are a collective of engineers, designers, and strategists. We don't just build websites; we architect the digital infrastructure for tomorrow's leading brands.
            </p>
        </div>
    </section>

    <!-- Cinematic Image Section -->
    <section style="padding: 0 0 6rem 0;">
        <div class="container" style="max-width: 1400px;">
            <div class="fade-up delay-3" style="width: 100%; height: 75vh; min-height: 600px; border-radius: 32px; overflow: hidden; position: relative; box-shadow: 0 40px 100px rgba(0,0,0,0.8); border: 1px solid rgba(255,255,255,0.05);">
                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2850&auto=format&fit=crop" alt="The Rayvotech Team" style="width: 100%; height: 100%; object-fit: cover; filter: grayscale(20%) contrast(1.1);">
                <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(10,10,14,0.9), transparent 50%); pointer-events: none;"></div>
            </div>
        </div>
    </section>

    <!-- Our Story (Two Column Editorial) -->
    <section class="section-padding" style="padding-top: 2rem; padding-bottom: 8rem;">
        <div class="container" style="max-width: 1200px;">
            <div class="fade-up" style="display: grid; grid-template-columns: 1fr 1.5fr; gap: 6rem; align-items: start;">
                <div>
                    <h2 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 2rem; position: sticky; top: 120px;">
                        The story <br>behind the <br><span style="color: var(--color-accent);">craft.</span>
                    </h2>
                </div>
                <div>
                    <p style="font-size: 1.5rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 2.5rem; font-weight: 400;">
                        Founded in the heart of Omaha, Nebraska, we set out to bridge the massive gap between cutting-edge technology and compelling design.
                    </p>
                    <p style="font-size: 1.25rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2.5rem;">
                        What started as a small team with a singular, obsessive vision has rapidly grown into a full-service creative technology agency. We are trusted by startups, enterprises, and ambitious founders across the United States who absolutely refuse to settle for ordinary.
                    </p>
                    <p style="font-size: 1.25rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2.5rem;">
                        We didn't build Rayvotech to be just another agency. We built it to be the last one you'd ever need. From day one, our focus has been exactly the same: delivering digital ecosystems that don't just look impressive, but actively convert and grow your business at scale.
                    </p>
                    <div style="padding-left: 2rem; border-left: 2px solid rgba(255,255,255,0.2); margin-top: 4rem;">
                        <p style="font-size: 1.15rem; color: var(--text-primary); margin: 0; font-family: 'Space Grotesk', sans-serif; letter-spacing: 0.5px;">
                            "Omaha may not be Silicon Valley, but that is exactly our advantage. We bring an unrelenting Midwest work ethic paired with a creative and technical edge that competes anywhere in the world."
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Mission & Vision (Bento Grid) -->
    <section style="padding: 4rem 0 8rem 0;">
        <div class="container" style="max-width: 1200px;">
            <div style="text-align: center; margin-bottom: 5rem;" class="fade-up">
                <h2 style="font-size: 3.5rem;">The Standard</h2>
            </div>

            <div class="bento-grid fade-up delay-1">
                <!-- Our Vision (Spans 2 columns) -->
                <div class="bento-item glass-card beam-card" style="grid-column: span 2; padding: 5rem; border-radius: 32px; position: relative; overflow: hidden; background: rgba(5,5,10,0.6); border: 1px solid rgba(255,255,255,0.05);">
                    <div style="position: absolute; top: -150px; right: -50px; width: 400px; height: 400px; background: rgba(2, 132, 199, 0.15); filter: blur(120px); border-radius: 50%;"></div>
                    <i class="ph ph-eye" style="font-size: 3rem; color: #38bdf8; margin-bottom: 2rem; display: block;"></i>
                    <h3 style="font-size: 2.5rem; margin-bottom: 1.5rem;">Our Vision</h3>
                    <p style="font-size: 1.35rem; line-height: 1.7; color: var(--text-secondary); max-width: 600px;">
                        A world where every ambitious brand — from a first-time founder to a seasoned enterprise — has total access to the bespoke design and deep engineering they require to win their market.
                    </p>
                </div>

                <!-- Our Mission -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 4rem; border-radius: 32px; display: flex; flex-direction: column; justify-content: center;">
                    <i class="ph ph-crosshair" style="font-size: 2.5rem; color: #f43f5e; margin-bottom: 2rem; display: block;"></i>
                    <h3 style="font-size: 2rem; margin-bottom: 1.5rem;">Our Mission</h3>
                    <p style="font-size: 1.15rem; line-height: 1.7; color: var(--text-secondary);">
                        To strictly engineer purposeful digital experiences that help brands stand out, scale up, and make a massive, measurable impact online.
                    </p>
                </div>

                <!-- Core Values Row -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem; border-radius: 32px;">
                    <h4 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-primary);"><i class="ph ph-lightning" style="color: #eab308; margin-right: 0.5rem;"></i> Move Fast</h4>
                    <p style="color: var(--text-secondary); line-height: 1.6;">Aggressive execution without ever cutting corners on code or design.</p>
                </div>
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem; border-radius: 32px;">
                    <h4 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-primary);"><i class="ph ph-brain" style="color: #a855f7; margin-right: 0.5rem;"></i> Think Deeply</h4>
                    <p style="color: var(--text-secondary); line-height: 1.6;">Every decision serves an overarching and measurable business goal.</p>
                </div>
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem; border-radius: 32px;">
                    <h4 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text-primary);"><i class="ph ph-handshake" style="color: #10b981; margin-right: 0.5rem;"></i> Genuine Care</h4>
                    <p style="color: var(--text-secondary); line-height: 1.6;">Dedicated partners who are authentically invested in your ultimate success.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- By The Numbers (Apple-style massive typography) -->
    <section style="padding: 8rem 0; background: #000; border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
        <div class="container">
            <div class="fade-up" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 4rem;">
                <!-- Stat 1 -->
                <div style="flex: 1; min-width: 250px; text-align: center;">
                    <div style="font-size: 6rem; font-weight: 700; font-family: 'Space Grotesk', sans-serif; background: linear-gradient(to bottom, #ffffff, #666666); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1;">
                        5<span style="font-size: 3rem;">+</span>
                    </div>
                    <div style="font-size: 1.15rem; color: var(--text-secondary); margin-top: 1rem; text-transform: uppercase; letter-spacing: 2px;">Years Shipping</div>
                </div>
                
                <!-- Stat 2 -->
                <div style="flex: 1; min-width: 250px; text-align: center;">
                    <div style="font-size: 6rem; font-weight: 700; font-family: 'Space Grotesk', sans-serif; background: linear-gradient(to bottom, #ffffff, #666666); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1;">
                        360&deg;
                    </div>
                    <div style="font-size: 1.15rem; color: var(--text-secondary); margin-top: 1rem; text-transform: uppercase; letter-spacing: 2px;">Digital Services</div>
                </div>

                <!-- Stat 3 -->
                <div style="flex: 1; min-width: 250px; text-align: center;">
                    <div style="font-size: 6rem; font-weight: 700; font-family: 'Space Grotesk', sans-serif; background: linear-gradient(to bottom, #ffffff, #666666); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1;">
                        OMA
                    </div>
                    <div style="font-size: 1.15rem; color: var(--text-secondary); margin-top: 1rem; text-transform: uppercase; letter-spacing: 2px;">Core HQ Location</div>
                </div>
            </div>
        </div>
    </section>

    <!-- How We Work (Elegant List) -->
    <section class="section-padding" style="padding: 10rem 0;">
        <div class="container" style="max-width: 1000px;">
            <div class="fade-up" style="text-align: center; margin-bottom: 6rem;">
                <h2 style="font-size: 3.5rem; margin-bottom: 1.5rem;">How We Operate</h2>
                <p style="font-size: 1.35rem; color: var(--text-secondary); max-width: 700px; margin: 0 auto;">
                    Culture isn't a perk at Rayvotech &mdash; it's our core product. Our entire structure is built purely on curiosity, high-level collaboration, and an absolute obsession with quality.
                </p>
            </div>

            <div class="fade-up delay-1" style="display: flex; flex-direction: column; gap: 2rem;">
                
                <div style="display: flex; gap: 3rem; align-items: flex-start; padding: 3rem; background: rgba(255,255,255,0.02); border-radius: 24px; border: 1px solid rgba(255,255,255,0.05); transition: background 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='rgba(255,255,255,0.02)'">
                    <div style="font-size: 1.5rem; font-weight: bold; color: var(--color-accent); font-family: 'Space Grotesk', sans-serif; width: 40px;">01</div>
                    <div>
                        <h3 style="font-size: 1.75rem; margin-bottom: 1rem;">Move Fast. High Quality.</h3>
                        <p style="font-size: 1.15rem; color: var(--text-secondary); line-height: 1.6; margin: 0;">We iterate at speed without ever cutting corners, operating aggressively but strictly enforcing the highest code and design standards across every deliverable.</p>
                    </div>
                </div>

                <div style="display: flex; gap: 3rem; align-items: flex-start; padding: 3rem; background: rgba(255,255,255,0.02); border-radius: 24px; border: 1px solid rgba(255,255,255,0.05); transition: background 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='rgba(255,255,255,0.02)'">
                    <div style="font-size: 1.5rem; font-weight: bold; color: var(--color-accent); font-family: 'Space Grotesk', sans-serif; width: 40px;">02</div>
                    <div>
                        <h3 style="font-size: 1.75rem; margin-bottom: 1rem;">Creative Strategy</h3>
                        <p style="font-size: 1.15rem; color: var(--text-secondary); line-height: 1.6; margin: 0;">We think outside the box without losing sight of strategy, ensuring that every visual decision directly serves a clear, quantifiable operational goal.</p>
                    </div>
                </div>

                <div style="display: flex; gap: 3rem; align-items: flex-start; padding: 3rem; background: rgba(255,255,255,0.02); border-radius: 24px; border: 1px solid rgba(255,255,255,0.05); transition: background 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='rgba(255,255,255,0.02)'">
                    <div style="font-size: 1.5rem; font-weight: bold; color: var(--color-accent); font-family: 'Space Grotesk', sans-serif; width: 40px;">03</div>
                    <div>
                        <h3 style="font-size: 1.75rem; margin-bottom: 1rem;">Radical Transparency</h3>
                        <p style="font-size: 1.15rem; color: var(--text-secondary); line-height: 1.6; margin: 0;">We communicate ruthlessly at every step. You're never left in the dark about where your project stands, what comes next, or why decisions were made.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>
    """

    final_content = content[:nav_end_idx] + "\n" + new_body + "\n    " + content[footer_start_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("About Us page totally rebuilt to Top Tech standards.")
else:
    print("Could not find boundaries for overhaul.")
