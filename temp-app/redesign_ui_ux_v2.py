import re

html_file = 'service-ui-ux-design.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace everything from the start of the Hero section to the start of the Footer.
# Find the end of <nav>
nav_end_idx = content.find('</nav>') + len('</nav>')
# Find the start of <!-- Footer -->
footer_start_idx = content.find('<!-- Footer -->')

if nav_end_idx > 6 and footer_start_idx != -1:
    new_body = """
    <!-- Page Header -->
    <section class="hero" id="hero" style="min-height: auto; padding-top: 10rem; padding-bottom: 3rem;">
        <div class="container hero-content text-center">
            <div class="y2k-badge reveal-text">UI/UX DESIGN</div>
            <h1 class="hero-title reveal-text delay-1" style="font-size: 5rem; line-height: 1.1;">Experience <br> <span class="text-gradient liquid-text">Engineered.</span></h1>
            <p class="hero-subtitle reveal-text delay-2" style="max-width: 700px; margin: 0 auto;">There is a version of your digital product that your users love so much they tell other people about it. Getting there is what our UI/UX design service is built to do.</p>
        </div>
    </section>

    <section style="padding: 2rem 0 6rem 0;">
        <div class="container" style="max-width: 1200px;">
            
            <!-- Intro Block -->
            <div class="fade-up" style="max-width: 800px; margin: 0 auto 5rem auto; text-align: center;">
                <p style="font-size: 1.25rem; line-height: 1.8; color: var(--text-secondary);">
                    At Rayvotech, we believe that design is not decoration &mdash; it is problem solving. Our UI/UX service goes far beyond making things look good. We architect the entire experience your users have when they interact with your digital product, from the very first moment they arrive to the moment they complete the action you most want them to take. Every element of that journey is studied, considered, tested, and refined until it works exactly as it should.
                </p>
            </div>

            <!-- Bento Grid Section -->
            <div class="bento-grid fade-up delay-1" style="margin-bottom: 6rem;">
                
                <!-- Main Architecture Card -->
                <div class="bento-item glass-card beam-card" style="grid-column: span 2; padding: 4rem; display: flex; flex-direction: column; justify-content: center; position: relative; overflow: hidden;">
                    <div style="position: absolute; top: -100px; right: -100px; width: 300px; height: 300px; background: rgba(0, 230, 240, 0.15); filter: blur(100px); border-radius: 50%;"></div>
                    <div class="card-icon chrome-icon" style="margin-bottom: 2rem; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem;"><i class="ph ph-intersect"></i></div>
                    <h3 style="font-size: 2.5rem; margin-bottom: 1.5rem;">The Architecture of Experience</h3>
                    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 1.5rem;">
                        <strong>UI stands for User Interface</strong> — the visual layer that users interact with directly. Buttons, menus, forms, cards, icons, typography, color, spacing. Every visual component that makes up the surface of your product.
                    </p>
                    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary);">
                        <strong>UX stands for User Experience</strong> — the logic, structure, and flow beneath that surface. How information is organized. How users move from one section to another. How friction is identified and eliminated. How the product makes people feel at every stage of their interaction with it. 
                    </p>
                    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--color-accent); font-weight: 500; margin-top: 1.5rem;">
                        We design both, together. A beautiful interface built on a confusing structure will frustrate your users. A logical structure wrapped in a poor visual design will lose their trust.
                    </p>
                </div>

                <!-- Image Card -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 0; overflow: hidden; height: 100%; min-height: 400px; position: relative;">
                    <img src="https://i.imgur.com/l5BnUoy.jpg" alt="UI/UX Visual Design" style="width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                    <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 2rem; background: linear-gradient(to top, rgba(10,10,14,0.9), transparent);">
                        <h4 style="color: #fff; font-size: 1.5rem; margin: 0;">Pixel Perfect Precision</h4>
                    </div>
                </div>

            </div>

            <!-- The Process Section -->
            <div style="text-align: center; margin-bottom: 4rem;">
                <div class="y2k-badge" style="margin-bottom: 1rem;">METHODOLOGY</div>
                <h2 style="font-size: 3rem;">Our Design Process</h2>
            </div>

            <div class="flat-card glass-card fade-up delay-2" style="padding: 0; overflow: hidden; margin-bottom: 6rem; border-radius: 24px;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                    
                    <!-- Step 1 -->
                    <div style="padding: 3rem; border-right: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
                        <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #a855f7, #6366f1); box-shadow: 0 10px 20px rgba(168, 85, 247, 0.2); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-magnifying-glass"></i></div>
                        <h4 style="font-size: 1.5rem; margin-bottom: 1rem;">1. Research & Discovery</h4>
                        <p style="font-size: 1rem; line-height: 1.7; color: var(--text-secondary);">We do not make assumptions about what your users want or need. We study them. We develop detailed user personas that represent your real audience, and map out every journey a user might take through your product.</p>
                    </div>

                    <!-- Step 2 -->
                    <div style="padding: 3rem; border-right: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
                        <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #3b82f6, #06b6d4); box-shadow: 0 10px 20px rgba(59, 130, 246, 0.2); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-tree-structure"></i></div>
                        <h4 style="font-size: 1.5rem; margin-bottom: 1rem;">2. Information Architecture</h4>
                        <p style="font-size: 1rem; line-height: 1.7; color: var(--text-secondary);">From that research, we build a clear and logical blueprint of how your content and features should be organized to serve your users most effectively. This is the skeleton of your product.</p>
                    </div>

                    <!-- Step 3 -->
                    <div style="padding: 3rem; border-bottom: 1px solid rgba(255,255,255,0.05);">
                        <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #10b981, #3b82f6); box-shadow: 0 10px 20px rgba(16, 185, 129, 0.2); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-blueprint"></i></div>
                        <h4 style="font-size: 1.5rem; margin-bottom: 1rem;">3. Strategic Wireframing</h4>
                        <p style="font-size: 1rem; line-height: 1.7; color: var(--text-secondary);">We build simplified, structural representations showing layout and flow without the distraction of color or visual detail, allowing us to solve hard user interaction problems early.</p>
                    </div>

                    <!-- Step 4 -->
                    <div style="padding: 3rem; border-right: 1px solid rgba(255,255,255,0.05);">
                        <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #f59e0b, #ef4444); box-shadow: 0 10px 20px rgba(245, 158, 11, 0.2); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-cursor-click"></i></div>
                        <h4 style="font-size: 1.5rem; margin-bottom: 1rem;">4. Interactive Prototyping</h4>
                        <p style="font-size: 1rem; line-height: 1.7; color: var(--text-secondary);">Once wireframes are approved, we build interactive prototypes that simulate the real experience. These prototypes are tested with real users, generating vital feedback before development begins.</p>
                    </div>

                    <!-- Step 5 -->
                    <div style="padding: 3rem; grid-column: auto;">
                        <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #f43f5e, #a855f7); box-shadow: 0 10px 20px rgba(244, 63, 94, 0.2); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-paint-brush"></i></div>
                        <h4 style="font-size: 1.5rem; margin-bottom: 1rem;">5. Final Visual Design</h4>
                        <p style="font-size: 1rem; line-height: 1.7; color: var(--text-secondary);">The final layer brings everything to life visually — applying your brand's color system, typography, imagery, and motion. We build design systems that ensure consistency and scale seamlessly.</p>
                    </div>
                    
                    <!-- Invisible spacer if grid is an odd number to fill space -->
                    <div style="padding: 3rem; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.2);">
                        <a href="hire.html" class="btn btn-outline" style="width: 100%; border-color: rgba(255,255,255,0.1);">Start Your Project <i class="ph ph-arrow-right"></i></a>
                    </div>
                </div>
            </div>

            <!-- ROI Block -->
            <div class="glass-card fade-up" style="padding: 4rem; text-align: center; background: linear-gradient(135deg, rgba(0, 230, 240, 0.05), rgba(168, 85, 247, 0.05)); border: 1px solid rgba(0, 230, 240, 0.1);">
                <i class="ph ph-chart-line-up" style="font-size: 3rem; color: var(--color-accent); margin-bottom: 1.5rem;"></i>
                <h3 style="font-size: 2.5rem; margin-bottom: 1.5rem;">The ROI of Design</h3>
                <p style="font-size: 1.25rem; line-height: 1.8; color: var(--text-secondary); max-width: 900px; margin: 0 auto;">
                    Investing in UI/UX design is one of the highest-return decisions a business can make. Companies that prioritize user experience consistently outperform those that do not — with higher conversion rates, lower customer acquisition costs, stronger brand loyalty, and better word-of-mouth. In a digital landscape where your competitors are just one click away, the experience you deliver is your most powerful differentiator.
                </p>
                <div style="margin-top: 3rem;">
                    <a href="hire.html" class="btn btn-primary btn-lg">Transform Your UI/UX Today</a>
                </div>
            </div>

        </div>
    </section>
    """

    final_content = content[:nav_end_idx] + "\n" + new_body + "\n    " + content[footer_start_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("UI/UX page fundamentally rebuilt.")
else:
    print("Could not find boundaries for overhaul.")
