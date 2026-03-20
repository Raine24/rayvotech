import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the existing process section
pattern = re.compile(r'<!-- Process Breakdown -->.*?</section>', re.DOTALL)

premium_process_html = """<!-- Process Breakdown Redesign -->
    <section class="process awwwards-process section-padding" id="process">
        <div class="container">
            <div class="section-header text-center fade-up" style="margin-bottom: 5rem;">
                <span class="section-tag">Our Approach</span>
                <h2 style="font-size: clamp(2.8rem, 5vw, 4rem); letter-spacing: -1px; margin-top: 1rem;">How We Build <br> <span class="text-gradient">Exceptional Brands</span></h2>
            </div>
            
            <div class="awwwards-process-grid">
                
                <!-- Step 1 -->
                <div class="process-card fade-up glass-card delay-1 span-2">
                    <div class="p-card-bg-number">01</div>
                    <div class="p-card-content">
                        <div class="p-card-header">
                            <div class="p-icon-box"><i class="ph ph-compass-tool"></i></div>
                            <h3>Discover & Strategy</h3>
                        </div>
                        <p>We dive deep into your brand, understanding your goals, audience, and market to craft a tailored digital strategy. We lay the foundation for success.</p>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="process-card fade-up glass-card delay-2">
                    <div class="p-card-bg-number">02</div>
                    <div class="p-card-content">
                        <div class="p-card-header">
                            <div class="p-icon-box"><i class="ph ph-bezier-curve"></i></div>
                            <h3>Design & Prototyping</h3>
                        </div>
                        <p>Our creative team brings concepts to life with wireframes and interactive prototypes, focusing on user experience, aesthetics, and brand alignment.</p>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="process-card fade-up glass-card delay-3">
                    <div class="p-card-bg-number">03</div>
                    <div class="p-card-content">
                        <div class="p-card-header">
                            <div class="p-icon-box"><i class="ph ph-code-block"></i></div>
                            <h3>Development & SEO</h3>
                        </div>
                        <p>We build robust, scalable platforms using cutting-edge tech. Simultaneously, we implement advanced SEO strategies to ensure you rank high.</p>
                    </div>
                </div>

                <!-- Step 4 -->
                <div class="process-card fade-up glass-card delay-4 span-2">
                    <div class="p-card-bg-number">04</div>
                    <div class="p-card-content">
                        <div class="p-card-header">
                            <div class="p-icon-box"><i class="ph ph-rocket-launch"></i></div>
                            <h3>Launch & Scale</h3>
                        </div>
                        <p>Rigorous testing precedes the launch. Once live, we monitor performance, gather data, and continuously optimize for better conversion rates.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

if pattern.search(content):
    new_content = pattern.sub(premium_process_html, content)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully injected Awwwards process HTML into index.html")
else:
    print("Could not find the process section in index.html")
