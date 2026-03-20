import re

html_file = 'service-seo-growth.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

nav_end_idx = content.find('</nav>') + len('</nav>')
footer_start_idx = content.find('<!-- Footer -->')

if nav_end_idx > 6 and footer_start_idx != -1:
    new_body = """
    <!-- Page Header -->
    <section class="hero" id="hero" style="min-height: auto; padding-top: 10rem; padding-bottom: 3rem;">
        <div class="container hero-content text-center">
            <div class="y2k-badge reveal-text" style="background: rgba(168, 85, 247, 0.1); border-color: rgba(168, 85, 247, 0.3); color: #c084fc;">SEO & GROWTH</div>
            <h1 class="hero-title reveal-text delay-1" style="font-size: 5rem; line-height: 1.1;">Dominate <br> <span class="text-gradient liquid-text" style="background: linear-gradient(to right, #c084fc, #38bdf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Search.</span></h1>
            <p class="hero-subtitle reveal-text delay-2" style="max-width: 900px; margin: 0 auto; font-size: 1.25rem;">
                You could have the most beautifully designed, flawlessly developed website in your industry and still lose to a competitor with a worse product simply because they show up on Google and you don't. That's the brutal reality of the digital landscape. At Rayvotech, we make sure that never happens to you.
            </p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 2rem 0 6rem 0;">
        <div class="container" style="max-width: 1200px;">
            
            <div class="fade-up" style="max-width: 900px; margin: 0 auto 6rem auto; text-align: center;">
                <p style="font-size: 1.35rem; line-height: 1.8; color: var(--text-secondary);">
                    Our SEO and conversion optimization service is built to do two things: bring the right people to your website and turn them into paying customers once they arrive. Traffic without conversion is vanity. Conversion without traffic is invisibility. We deliver both.
                </p>
            </div>

            <!-- Massive Image Showcase -->
            <div class="fade-up delay-1" style="width: 100%; height: 600px; border-radius: 32px; overflow: hidden; margin-bottom: 8rem; box-shadow: 0 40px 100px rgba(168, 85, 247, 0.2); border: 1px solid rgba(255,255,255,0.05); position: relative;">
                <img src="https://i.imgur.com/ZvaT5CT.jpg" alt="SEO and Growth Strategy" style="width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 60%; background: linear-gradient(to top, rgba(10,10,14,1), transparent); pointer-events: none;"></div>
                <div style="position: absolute; bottom: 3rem; left: 4rem;">
                    <h3 style="color: #fff; font-size: 2.5rem; margin: 0; font-family: 'Space Grotesk', sans-serif;">Own Your Market.</h3>
                </div>
            </div>

            <!-- What We Do (Asymmetrical Bento Grid) -->
            <div style="text-align: center; margin-bottom: 4rem;">
                <h2 style="font-size: 3.5rem;">What We Do</h2>
            </div>
            
            <div class="bento-grid fade-up delay-1" style="margin-bottom: 8rem;">
                
                <!-- Main Card: Conversion Rate Optimization -->
                <div class="bento-item glass-card beam-card" style="grid-column: span 3; padding: 4rem; display: flex; flex-direction: column; justify-content: center; position: relative; overflow: hidden; border-color: rgba(168, 85, 247, 0.2);">
                    <div style="position: absolute; top: -150px; right: -50px; width: 400px; height: 400px; background: rgba(168, 85, 247, 0.1); filter: blur(120px); border-radius: 50%;"></div>
                    <div class="card-icon chrome-icon" style="margin-bottom: 2rem; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem;"><i class="ph ph-chart-line-up"></i></div>
                    <h3 style="font-size: 2.5rem; margin-bottom: 1.5rem;">Conversion Rate Optimization (CRO)</h3>
                    <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); max-width: 800px;">
                        Getting traffic to your site is only half the battle. We analyze how visitors behave once they arrive &mdash; where they click, where they scroll, where they drop off &mdash; and use that data to make strategic improvements that turn more of your existing traffic into leads, sales, and revenue. A/B testing, heatmap analysis, CTA optimization, form improvements, and landing page refinement are all part of the process.
                    </p>
                </div>

                <!-- Technical SEO -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #a855f7, #6366f1); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-wrench"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Technical SEO</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        The foundation everything else is built on. We audit and optimize the technical health of your website ensuring search engines can crawl, index, and understand your content without friction. Fast load times, clean site architecture, and mobile optimization.
                    </p>
                </div>

                <!-- On-Page SEO -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #f59e0b, #eab308); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-file-text"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">On-Page SEO</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        Every page on your website is an opportunity to rank. We optimize your content, headings, metadata, image alt tags, internal linking structure, and keyword placement making sure every page speaks the language of both search engines and customers.
                    </p>
                </div>

                <!-- Keyword Strategy -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #38bdf8, #0ea5e9); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-target"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Keyword Strategy</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        We don't chase vanity keywords with impossible competition. We identify specific search terms your target audience is using &mdash; high intent, high relevance &mdash; and build an optimization strategy around them.
                    </p>
                </div>

                <!-- Content Strategy -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #10b981, #3b82f6); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-pen-nib"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Content Optimization</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        Content is the engine of SEO. We develop a strategy that positions your brand as an authority. From blog posts to service pages, we create and optimize content that ranks, educates, and converts.
                    </p>
                </div>

                <!-- Local SEO -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #ec4899, #f43f5e); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-map-pin"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Local SEO</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        For businesses serving specific markets, local visibility is everything. We optimize your Google Business Profile, build citations, and ensure you show up when people near you are searching.
                    </p>
                </div>

                <!-- Link Building -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #14b8a6, #06b6d4); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-link"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Link Building</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        Authority matters. We build a strategic backlink profile through ethical, white-hat link building &mdash; earning mentions from reputable websites that signal to Google your site is trustworthy.
                    </p>
                </div>

                <!-- SEO Audits -->
                <div class="bento-item glass-card" style="grid-column: span 3; padding: 3rem; background: linear-gradient(135deg, rgba(255,255,255,0.02), rgba(168, 85, 247, 0.05)); border: 1px dashed rgba(168,85,247,0.3);">
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: #c084fc;">SEO Audits</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        Not sure why your site isn't ranking? We dig deep into your current SEO performance &mdash; technical issues, content gaps, backlink profile, competitor analysis &mdash; and deliver a clear, actionable roadmap for improvement.
                    </p>
                </div>
            </div>

            <!-- What Good SEO Delivers & The Long term investment Callout -->
            <div class="fade-up" style="margin-bottom: 8rem;">
                <h2 style="font-size: 3rem; text-align: center; margin-bottom: 3rem;">What Good SEO Actually Delivers</h2>
                
                <div class="glass-card" style="padding: 4rem; background: rgba(5,5,10,0.6); border-radius: 32px; border: 1px solid rgba(168, 85, 247, 0.2);">
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
                        <div style="display: flex; gap: 1rem; align-items: flex-start;">
                            <i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem; margin-top: 0.25rem;"></i>
                            <span style="font-size: 1.15rem; color: var(--text-primary); line-height: 1.6;">Higher rankings on Google for searches your customers are making.</span>
                        </div>
                        <div style="display: flex; gap: 1rem; align-items: flex-start;">
                            <i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem; margin-top: 0.25rem;"></i>
                            <span style="font-size: 1.15rem; color: var(--text-primary); line-height: 1.6;">More qualified organic traffic &mdash; people actively looking for what you offer.</span>
                        </div>
                        <div style="display: flex; gap: 1rem; align-items: flex-start;">
                            <i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem; margin-top: 0.25rem;"></i>
                            <span style="font-size: 1.15rem; color: var(--text-primary); line-height: 1.6;">Stronger brand credibility and authority in your actual market.</span>
                        </div>
                        <div style="display: flex; gap: 1rem; align-items: flex-start;">
                            <i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem; margin-top: 0.25rem;"></i>
                            <span style="font-size: 1.15rem; color: var(--text-primary); line-height: 1.6;">Lower customer acquisition costs over time compared to paid ads.</span>
                        </div>
                        <div style="display: flex; gap: 1rem; align-items: flex-start;">
                            <i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem; margin-top: 0.25rem;"></i>
                            <span style="font-size: 1.15rem; color: var(--text-primary); line-height: 1.6;">More leads, more conversions, and more revenue consistently.</span>
                        </div>
                    </div>

                    <div style="padding: 2.5rem; background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(56, 189, 248, 0.1)); border-radius: 16px; border-left: 4px solid #c084fc;">
                        <p style="font-size: 1.25rem; font-weight: 500; color: #fff; margin: 0; line-height: 1.7;">
                            SEO is not a quick fix. It is a long-term investment that compounds over time and the brands that start early are the ones that dominate their market later.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Two Column: Process & What You Get -->
            <div class="fade-up" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(450px, 1fr)); gap: 4rem; margin-bottom: 8rem;">
                <!-- Process -->
                <div>
                    <h2 style="font-size: 2.5rem; margin-bottom: 2rem;">Our Process</h2>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.5rem;">
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(168,85,247,0.1); color: #c084fc; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(168,85,247,0.3);">1</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Audit</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We conduct a full technical and content audit of your current website and SEO performance.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(168,85,247,0.1); color: #c084fc; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(168,85,247,0.3);">2</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Research</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We analyze your competitors, identify keyword opportunities, and map your content gaps.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(168,85,247,0.1); color: #c084fc; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(168,85,247,0.3);">3</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Strategy</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We build a clear, prioritized SEO and CRO roadmap tailored to your business goals.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(168,85,247,0.1); color: #c084fc; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(168,85,247,0.3);">4</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Optimize</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We implement on-page and technical optimizations across your entire site.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(168,85,247,0.1); color: #c084fc; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(168,85,247,0.3);">5</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Create</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We develop high-quality content designed to rank and convert.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(168,85,247,0.1); color: #c084fc; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(168,85,247,0.3);">6</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Monitor</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We track rankings, traffic, and conversions &mdash; reporting clearly on what's working.</span>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- What You Get -->
                <div class="glass-card" style="padding: 3rem; background: rgba(255,255,255,0.02); border-color: rgba(168, 85, 247, 0.2);">
                    <h2 style="font-size: 2.5rem; margin-bottom: 2rem;">What You Get</h2>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem; font-size: 1.1rem; color: var(--text-primary);">
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem;"></i> Full technical SEO audit and implementation</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem;"></i> Keyword research and content strategy</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem;"></i> On-page optimization across all pages</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem;"></i> Google Business Profile setup and optimization</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem;"></i> Monthly performance reporting</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem;"></i> Conversion rate analysis and improvements</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem;"></i> A/B testing on key pages and CTAs</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #c084fc; font-size: 1.5rem;"></i> Ongoing monitoring and refinement</li>
                    </ul>
                </div>
            </div>

            <!-- Why Us / CTA -->
            <div class="glass-card fade-up" style="padding: 6rem; text-align: center; background: linear-gradient(135deg, rgba(168, 85, 247, 0.08), rgba(56, 189, 248, 0.05)); border-radius: 32px; border: 1px solid rgba(168, 85, 247, 0.1); position: relative; overflow: hidden;">
                <h2 style="font-size: 3.5rem; margin-bottom: 2rem;">Why Rayvotech</h2>
                <p style="font-size: 1.35rem; line-height: 1.8; color: var(--text-secondary); max-width: 900px; margin: 0 auto 2rem auto;">
                    Most agencies treat SEO as an add-on. At Rayvotech it is a core discipline &mdash; woven into everything we build from day one. We don't believe in black-hat shortcuts, keyword stuffing, or strategies that get you penalized six months down the line. We build sustainable, long-term organic growth that keeps delivering results.
                </p>
                <p style="font-size: 1.35rem; color: var(--text-primary); font-weight: 500; margin-bottom: 4rem;">
                    Your competitors are investing in SEO right now. The question is whether you'll catch up &mdash; or get left behind. <br><em style="font-size: 1.2rem; color: var(--text-secondary); margin-top: 1rem; display: block;">Based in Omaha, Nebraska &mdash; driving organic growth for brands across the entire US market.</em>
                </p>
                
                <h3 style="font-size: 2.5rem; margin-bottom: 1rem; color: #c084fc;">Ready to own your market on Google?</h3>
                <p style="color: var(--text-secondary); font-size: 1.35rem; margin-bottom: 3.5rem;">Let's make sure your ideal customers find you before they find anyone else.</p>
                
                <a href="hire.html" class="btn btn-primary btn-lg" style="padding: 1.25rem 3rem; font-size: 1.25rem; border-radius: 50px; background: #c084fc; color: #000; border: none;">Start Your Project &rarr;</a>
            </div>

        </div>
    </section>
    """

    final_content = content[:nav_end_idx] + "\n" + new_body + "\n    " + content[footer_start_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("SEO & Growth page strictly rebuilt to modern premium standards.")
else:
    print("Could not find boundaries for overhaul.")
