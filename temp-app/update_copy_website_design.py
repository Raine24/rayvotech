import re

html_file = 'service-website-design.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

nav_end_idx = content.find('</nav>') + len('</nav>')
footer_start_idx = content.find('<!-- Footer -->')

if nav_end_idx > 6 and footer_start_idx != -1:
    new_body = """
    <!-- Page Header -->
    <section class="hero" id="hero" style="min-height: auto; padding-top: 10rem; padding-bottom: 3rem;">
        <div class="container hero-content text-center">
            <div class="y2k-badge reveal-text">WEBSITE DESIGN</div>
            <h1 class="hero-title reveal-text delay-1" style="font-size: 5rem; line-height: 1.1;">Digital <br> <span class="text-gradient liquid-text">Excellence.</span></h1>
            <p class="hero-subtitle reveal-text delay-2" style="max-width: 800px; margin: 0 auto; font-size: 1.25rem;">
                Your website is the most powerful sales tool your business owns. It works 24 hours a day, 7 days a week, representing your brand to every potential client who finds you online.
            </p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 2rem 0 6rem 0;">
        <div class="container" style="max-width: 1200px;">
            
            <div class="fade-up" style="max-width: 900px; margin: 0 auto 6rem auto; text-align: center;">
                <p style="font-size: 1.35rem; line-height: 1.8; color: var(--text-secondary);">
                    At Rayvotech, we don't build websites &mdash; we craft digital experiences that command attention, build trust, and drive action. From the first pixel to the final launch, every decision we make is rooted in one goal: making your brand impossible to ignore.
                </p>
            </div>

            <!-- What We Design (Bento Grid) -->
            <div style="text-align: center; margin-bottom: 3rem;">
                <h2 style="font-size: 3rem;">What We Design</h2>
            </div>
            
            <div class="bento-grid fade-up delay-1" style="margin-bottom: 8rem;">
                <!-- Card 1 -->
                <div class="bento-item glass-card beam-card" style="grid-column: span 2; padding: 3rem; display: flex; flex-direction: column; justify-content: center; position: relative; overflow: hidden;">
                    <div style="position: absolute; top: -100px; left: -100px; width: 300px; height: 300px; background: rgba(0, 230, 240, 0.1); filter: blur(100px); border-radius: 50%;"></div>
                    <div class="card-icon chrome-icon" style="margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-briefcase"></i></div>
                    <h3 style="font-size: 2rem; margin-bottom: 1rem;">Business Websites</h3>
                    <p style="font-size: 1.1rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        Your brand story, told beautifully. We design professional, conversion-focused websites for businesses of all sizes &mdash; built to impress on first visit and keep visitors coming back. Whether you're a solo founder or a growing company, we create a digital home that reflects the quality of what you do.
                    </p>
                </div>

                <!-- Card 2 -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #a855f7, #6366f1); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-rocket"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Landing Pages</h3>
                    <p style="font-size: 1rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        One page. One goal. Maximum impact. Our landing pages are engineered to convert &mdash; with sharp copy, strategic layouts, and clear calls to action that turn visitors into leads and leads into customers.
                    </p>
                </div>

                <!-- Card 3 -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #f59e0b, #ef4444); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-shopping-cart"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">E-Commerce Websites</h3>
                    <p style="font-size: 1rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        We design online stores that don't just display products &mdash; they sell them. Clean product pages, intuitive navigation, frictionless checkout flows, and trust-building design elements.
                    </p>
                </div>

                <!-- Card 4 -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #10b981, #3b82f6); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-paint-brush"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Portfolio & Personal Brand</h3>
                    <p style="font-size: 1rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        Your work speaks for itself &mdash; but only if it's presented right. We design portfolio sites that put your best work front and center, making a lasting impression.
                    </p>
                </div>

                <!-- Card 5 -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon chrome-icon" style="margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-arrows-clockwise"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Redesigns</h3>
                    <p style="font-size: 1rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        Is your current website letting your brand down? We audit what you have, identify what's holding you back, and rebuild it into something you're proud to share. 
                    </p>
                </div>
            </div>

            <!-- What Sets Us Apart -->
            <div class="fade-up" style="margin-bottom: 8rem;">
                <h2 style="font-size: 3rem; text-align: center; margin-bottom: 3rem;">What Sets Our Designs Apart</h2>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; overflow: hidden;">
                    
                    <div style="background: rgba(10,10,14,0.9); padding: 3rem;">
                        <h4 style="font-size: 1.25rem; color: var(--color-accent); margin-bottom: 1rem;">Brand Alignment</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">Every color, font, layout, and image choice is made with your brand identity in mind. Your website should feel like a natural extension of who you are &mdash; not a generic template.</p>
                    </div>
                    
                    <div style="background: rgba(10,10,14,0.9); padding: 3rem;">
                        <h4 style="font-size: 1.25rem; color: var(--color-accent); margin-bottom: 1rem;">Responsive Design</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">Over 60% of web traffic comes from mobile devices. Every website we design looks and performs flawlessly across all screen sizes &mdash; from huge monitors to smartphone screens.</p>
                    </div>

                    <div style="background: rgba(10,10,14,0.9); padding: 3rem;">
                        <h4 style="font-size: 1.25rem; color: var(--color-accent); margin-bottom: 1rem;">Performance Optimized</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">A beautiful website that loads slowly loses customers. We optimize every site for speed &mdash; compressing assets, streamlining code, and keeping bounce rates low.</p>
                    </div>

                    <div style="background: rgba(10,10,14,0.9); padding: 3rem;">
                        <h4 style="font-size: 1.25rem; color: var(--color-accent); margin-bottom: 1rem;">Conversion Focused</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">Good design isn't just about aesthetics &mdash; it's about results. We strategically place calls to action and structure page layouts to guide user behavior.</p>
                    </div>

                    <div style="background: rgba(10,10,14,0.9); padding: 3rem; grid-column: auto;">
                        <h4 style="font-size: 1.25rem; color: var(--color-accent); margin-bottom: 1rem;">SEO Ready</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">Every website we build comes with solid SEO foundations &mdash; clean code structure, proper heading hierarchy, meta tags, and fast load speeds for higher rankings.</p>
                    </div>
                </div>
            </div>

            <!-- Two Column: Process & What You Get -->
            <div class="fade-up" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(450px, 1fr)); gap: 4rem; margin-bottom: 8rem;">
                <!-- Process -->
                <div>
                    <h2 style="font-size: 2.5rem; margin-bottom: 2rem;">Our Design Process</h2>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.5rem;">
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(0,230,240,0.1); color: var(--color-accent); display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">1</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Discovery</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We learn everything about your brand, audience, competitors, and goals.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(0,230,240,0.1); color: var(--color-accent); display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">2</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Strategy</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We define the site structure, page hierarchy, and conversion strategy.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(0,230,240,0.1); color: var(--color-accent); display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">3</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Design</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We create stunning visual designs tailored to your brand identity.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(0,230,240,0.1); color: var(--color-accent); display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">4</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Review</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We refine based on your feedback through structured revision rounds.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(0,230,240,0.1); color: var(--color-accent); display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">5</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Launch & Support</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We deliver a tested, optimized website and stay with you post-launch.</span>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- What You Get -->
                <div class="glass-card" style="padding: 3rem; background: rgba(255,255,255,0.02);">
                    <h2 style="font-size: 2.5rem; margin-bottom: 2rem;">What You Get</h2>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem; font-size: 1.1rem; color: var(--text-primary);">
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: var(--color-accent); font-size: 1.5rem;"></i> Custom responsive design &mdash; no templates, ever</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: var(--color-accent); font-size: 1.5rem;"></i> Mobile and tablet optimized layouts</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: var(--color-accent); font-size: 1.5rem;"></i> Fast loading and performance optimized</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: var(--color-accent); font-size: 1.5rem;"></i> SEO-ready structure and metadata</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: var(--color-accent); font-size: 1.5rem;"></i> Cross-browser tested and compatible</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: var(--color-accent); font-size: 1.5rem;"></i> Clean handoff to your team or CMS</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: var(--color-accent); font-size: 1.5rem;"></i> Post-launch support included</li>
                    </ul>
                </div>
            </div>

            <!-- Pricing Table -->
            <div class="fade-up" style="margin-bottom: 8rem;">
                <h2 style="font-size: 3rem; text-align: center; margin-bottom: 3rem;">Our Packages</h2>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                    
                    <!-- Starter -->
                    <div class="glass-card" style="padding: 3rem; text-align: center; border-radius: 24px;">
                        <h3 style="font-size: 1.75rem; margin-bottom: 1rem; color: var(--text-secondary);">Starter</h3>
                        <div style="font-size: 3rem; font-weight: bold; color: var(--color-accent); margin-bottom: 2rem;">$500</div>
                        <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; display: flex; flex-direction: column; gap: 1rem; color: var(--text-secondary);">
                            <li><strong>Up to 5</strong> Pages</li>
                            <li><strong>1 round</strong> Revisions</li>
                            <li><strong>7 days</strong> Delivery</li>
                            <li><strong>30 days</strong> Support</li>
                        </ul>
                        <a href="hire.html" class="btn btn-outline" style="width: 100%;">Select Starter</a>
                    </div>
                    
                    <!-- Growth -->
                    <div class="glass-card beam-card" style="padding: 3rem; text-align: center; border-radius: 24px; position: relative; overflow: hidden; transform: scale(1.05); z-index: 10;">
                        <div class="y2k-badge" style="position: absolute; top: 1rem; right: 1rem; font-size: 0.75rem; padding: 0.25rem 0.75rem;">MOST POPULAR</div>
                        <h3 style="font-size: 1.75rem; margin-bottom: 1rem; color: var(--text-primary);">Growth</h3>
                        <div style="font-size: 3.5rem; font-weight: bold; color: #fff; margin-bottom: 2rem;">$1,000</div>
                        <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; display: flex; flex-direction: column; gap: 1rem; color: var(--text-primary);">
                            <li><strong>Up to 10</strong> Pages</li>
                            <li><strong>3 rounds</strong> Revisions</li>
                            <li><strong>14 days</strong> Delivery</li>
                            <li><strong>60 days</strong> Support</li>
                        </ul>
                        <a href="hire.html" class="btn btn-primary" style="width: 100%;">Select Growth</a>
                    </div>
                    
                    <!-- Premium -->
                    <div class="glass-card" style="padding: 3rem; text-align: center; border-radius: 24px;">
                        <h3 style="font-size: 1.75rem; margin-bottom: 1rem; color: var(--text-secondary);">Premium</h3>
                        <div style="font-size: 3rem; font-weight: bold; color: var(--color-accent); margin-bottom: 2rem;">$2,000</div>
                        <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; display: flex; flex-direction: column; gap: 1rem; color: var(--text-secondary);">
                            <li><strong>Unlimited</strong> Pages</li>
                            <li><strong>Unlimited</strong> Revisions</li>
                            <li><strong>21 days</strong> Delivery</li>
                            <li><strong>90 days</strong> Support</li>
                        </ul>
                        <a href="hire.html" class="btn btn-outline" style="width: 100%;">Select Premium</a>
                    </div>
                </div>
            </div>

            <!-- Why Us / CTA -->
            <div class="glass-card fade-up" style="padding: 5rem; text-align: center; background: linear-gradient(135deg, rgba(0, 230, 240, 0.1), rgba(168, 85, 247, 0.1)); border-radius: 24px;">
                <h2 style="font-size: 3rem; margin-bottom: 2rem;">Why Rayvotech</h2>
                <p style="font-size: 1.25rem; line-height: 1.8; color: var(--text-secondary); max-width: 900px; margin: 0 auto 2rem auto;">
                    We're a team of designers who genuinely love what we do. Every project we take on gets our full creative energy, strategic thinking, and relentless attention to detail. We don't do cookie-cutter. We don't do average. We build websites that make our clients proud and their competitors nervous.
                </p>
                <p style="font-size: 1.25rem; color: var(--text-primary); font-weight: 500; margin-bottom: 4rem;">
                    <em>Based in Omaha, Nebraska &mdash; built for brands across the entire US market.</em>
                </p>
                
                <h3 style="font-size: 2.25rem; margin-bottom: 0.5rem;">Ready for a website that works as hard as you do?</h3>
                <p style="color: var(--color-accent); font-size: 1.25rem; margin-bottom: 3rem;">Let's build something your visitors will never forget.</p>
                
                <a href="hire.html" class="btn btn-primary btn-lg">Start Your Project &rarr;</a>
            </div>

        </div>
    </section>
    """

    final_content = content[:nav_end_idx] + "\n" + new_body + "\n    " + content[footer_start_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Website Design page rebuilt beautifully.")
else:
    print("Could not find boundaries.")
