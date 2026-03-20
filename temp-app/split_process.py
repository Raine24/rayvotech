import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<!-- Process Breakdown Redesign -->.*?</section>', re.DOTALL)

split_process_html = """<!-- Process Breakdown Redesign -->
    <section class="process split-process section-padding" id="process">
        <div class="container split-container">
            
            <!-- Left Column: Visual & Header -->
            <div class="process-visual-col fade-up">
                <div class="section-header" style="margin-bottom: 3rem;">
                    <span class="section-tag">Our Approach</span>
                    <h2 style="font-size: clamp(2.5rem, 4vw, 3.5rem); letter-spacing: -1px; margin-top: 1rem;">How We Build <br> <span class="text-gradient">Exceptional Brands</span></h2>
                </div>
                
                <div class="process-shaped-frame">
                    <!-- High-end abstract image serving as the visual anchor -->
                    <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2000&auto=format&fit=crop" alt="Digital creation process" />
                    <div class="frame-glass-overlay"></div>
                    <div class="frame-border-glow"></div>
                </div>
            </div>

            <!-- Right Column: Vertical Timeline -->
            <div class="process-timeline-col">
                <div class="vertical-connector-track">
                    <div class="vertical-connector-fill" id="process-progress"></div>
                </div>
                
                <!-- Step 1 -->
                <div class="v-step-item fade-up delay-1">
                    <div class="v-step-node"></div>
                    <div class="v-step-content">
                        <h3 class="v-step-title"><span class="v-step-num">01.</span> Discover & Strategy</h3>
                        <p>We dive deep into your brand, understanding your goals, audience, and market to craft a tailored digital strategy. We lay the foundation for success.</p>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="v-step-item fade-up delay-2">
                    <div class="v-step-node"></div>
                    <div class="v-step-content">
                        <h3 class="v-step-title"><span class="v-step-num">02.</span> Design & Prototyping</h3>
                        <p>Our creative team brings concepts to life with wireframes and interactive prototypes, focusing on user experience, aesthetics, and brand alignment.</p>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="v-step-item fade-up delay-3">
                    <div class="v-step-node"></div>
                    <div class="v-step-content">
                        <h3 class="v-step-title"><span class="v-step-num">03.</span> Development & SEO</h3>
                        <p>We build robust, scalable platforms using cutting-edge tech. Simultaneously, we implement advanced SEO strategies to ensure you rank high.</p>
                    </div>
                </div>

                <!-- Step 4 -->
                <div class="v-step-item fade-up delay-4">
                    <div class="v-step-node"></div>
                    <div class="v-step-content">
                        <h3 class="v-step-title"><span class="v-step-num">04.</span> Launch & Scale</h3>
                        <p>Rigorous testing precedes the launch. Once live, we monitor performance, gather data, and continuously optimize for better conversion rates.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

if pattern.search(content):
    new_content = pattern.sub(split_process_html, content)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced process breakdown with new 2-column split layout.")
else:
    print("Could not find the target HTML section.")
