import re

html_file = 'service-web-development.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

nav_end_idx = content.find('</nav>') + len('</nav>')
footer_start_idx = content.find('<!-- Footer -->')

if nav_end_idx > 6 and footer_start_idx != -1:
    new_body = """
    <!-- Page Header -->
    <section class="hero" id="hero" style="min-height: auto; padding-top: 10rem; padding-bottom: 3rem;">
        <div class="container hero-content text-center">
            <div class="y2k-badge reveal-text" style="background: rgba(2, 132, 199, 0.1); border-color: rgba(2, 132, 199, 0.3); color: #38bdf8;">WEB & APP DEVELOPMENT</div>
            <h1 class="hero-title reveal-text delay-1" style="font-size: 5rem; line-height: 1.1;">Engineered to <br> <span class="text-gradient liquid-text" style="background: linear-gradient(to right, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Perform.</span></h1>
            <p class="hero-subtitle reveal-text delay-2" style="max-width: 800px; margin: 0 auto; font-size: 1.25rem;">
                We don't just write code. We engineer digital products that perform. Design without development is just a pretty picture. At Rayvotech, we transform your approved designs into fast, scalable, and rock-solid digital products that work flawlessly in the real world.
            </p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 2rem 0 6rem 0;">
        <div class="container" style="max-width: 1200px;">
            
            <div class="fade-up" style="max-width: 900px; margin: 0 auto 6rem auto; text-align: center;">
                <p style="font-size: 1.35rem; line-height: 1.8; color: var(--text-secondary);">
                    Our development team combines technical depth with creative sensibility &mdash; writing clean, maintainable code that brings your vision to life exactly as intended. From simple marketing websites to complex web applications and mobile apps, we build with precision, performance, and your long-term growth in mind.
                </p>
            </div>

            <!-- Massive Image Showcase -->
            <div class="fade-up delay-1" style="width: 100%; height: 600px; border-radius: 32px; overflow: hidden; margin-bottom: 8rem; box-shadow: 0 40px 100px rgba(2,132,199,0.2); border: 1px solid rgba(255,255,255,0.05); position: relative;">
                <img src="https://i.imgur.com/vRNDwZs.jpg" alt="Web Development Architecture" style="width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 60%; background: linear-gradient(to top, rgba(10,10,14,1), transparent); pointer-events: none;"></div>
                <div style="position: absolute; bottom: 3rem; left: 4rem;">
                    <h3 style="color: #fff; font-size: 2.5rem; margin: 0; font-family: 'Space Grotesk', sans-serif;">Build For Scale.</h3>
                </div>
            </div>

            <!-- What We Build (Asymmetrical Grid) -->
            <div style="text-align: center; margin-bottom: 4rem;">
                <h2 style="font-size: 3.5rem;">What We Build</h2>
            </div>
            
            <div class="bento-grid fade-up delay-1" style="margin-bottom: 8rem;">
                <!-- Full Width Feature -->
                <div class="bento-item glass-card beam-card" style="grid-column: span 3; padding: 4rem; display: flex; flex-direction: column; justify-content: center; position: relative; overflow: hidden; border-color: rgba(56, 189, 248, 0.2);">
                    <div style="position: absolute; top: -150px; right: -50px; width: 400px; height: 400px; background: rgba(56, 189, 248, 0.1); filter: blur(120px); border-radius: 50%;"></div>
                    <div class="card-icon chrome-icon" style="margin-bottom: 2rem; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem;"><i class="ph ph-browsers"></i></div>
                    <h3 style="font-size: 2.5rem; margin-bottom: 1.5rem;">Web Applications</h3>
                    <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); max-width: 800px;">
                        Beyond websites &mdash; we build powerful web applications with complex functionality, user authentication, dashboards, data management, and custom workflows tailored to your business needs. If you can imagine it, we can engineer it.
                    </p>
                </div>

                <!-- Card 2 -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #3b82f6, #0ea5e9); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-globe"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Marketing Websites</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        Your brand's digital foundation. We develop fast, responsive, and SEO-optimized marketing websites that represent your business professionally and convert visitors into customers around the clock.
                    </p>
                </div>

                <!-- Card 3 -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #f59e0b, #eab308); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-shopping-cart-simple"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">E-Commerce Platforms</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        We develop online stores built to scale &mdash; with seamless product management, secure payment gateways, inventory systems, and optimized checkout flows that maximize every sale opportunity.
                    </p>
                </div>

                <!-- Card 4 -->
                <div class="bento-item glass-card" style="grid-column: span 1; padding: 3rem;">
                    <div class="card-icon gradient-icon" style="background: linear-gradient(135deg, #8b5cf6, #d946ef); margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-device-mobile"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Mobile Applications</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        Your users live on their phones. We build native-feeling iOS and Android applications with smooth performance, intuitive interfaces, and deep functionality that keeps users engaged.
                    </p>
                </div>

                <!-- Card 5 (Span 2) -->
                <div class="bento-item glass-card" style="grid-column: span 2; padding: 3rem; background: linear-gradient(135deg, rgba(255,255,255,0.02), rgba(56, 189, 248, 0.05));">
                    <div class="card-icon chrome-icon" style="margin-bottom: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="ph ph-plugs-connected"></i></div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">API & CMS Integrations</h3>
                    <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin: 0;">
                        We connect your digital product to CRMs, payment processors, and entirely headless CMS systems (Sanity, Contentful, WordPress). Your tech stack should work together seamlessly, and we give your team the limitless ability to manage content without touching code.
                    </p>
                </div>
            </div>

            <!-- THE TECH STACK (Code Terminal/Neon Array) -->
            <div class="fade-up" style="margin-bottom: 8rem;">
                <div class="glass-card beam-card" style="padding: 5rem; border-radius: 32px; background: rgba(5,5,10,0.8); border: 1px solid rgba(56, 189, 248, 0.2); position: relative; overflow: hidden;">
                    <div style="position: absolute; top: -200px; left: 50%; transform: translateX(-50%); width: 800px; height: 400px; background: radial-gradient(circle, rgba(56,189,248,0.15) 0%, transparent 70%); pointer-events: none;"></div>
                    
                    <div style="text-align: center; margin-bottom: 4rem; position: relative; z-index: 2;">
                        <h2 style="font-size: 3.5rem; margin-bottom: 1rem;">Our Tech Stack</h2>
                        <p style="font-size: 1.25rem; color: var(--text-secondary); max-width: 700px; margin: 0 auto;">We work with modern, battle-tested technologies chosen for performance, scalability, and long-term maintainability.</p>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; position: relative; z-index: 2;">
                        
                        <!-- Frontend -->
                        <div>
                            <h4 style="color: #38bdf8; font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 1.5rem; border-bottom: 1px solid rgba(56,189,248,0.3); padding-bottom: 0.5rem;">Frontend</h4>
                            <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.75rem; color: #cbd5e1; font-family: monospace; font-size: 1rem;">
                                <li>&rsaquo; React & Next.js</li>
                                <li>&rsaquo; Tailwind CSS</li>
                                <li>&rsaquo; Framer Motion</li>
                                <li>&rsaquo; TypeScript</li>
                                <li>&rsaquo; HTML5 & CSS3</li>
                            </ul>
                        </div>

                        <!-- Backend -->
                        <div>
                            <h4 style="color: #10b981; font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 1.5rem; border-bottom: 1px solid rgba(16,185,129,0.3); padding-bottom: 0.5rem;">Backend</h4>
                            <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.75rem; color: #cbd5e1; font-family: monospace; font-size: 1rem;">
                                <li>&rsaquo; Node.js & Express</li>
                                <li>&rsaquo; Python & Django</li>
                                <li>&rsaquo; REST APIs</li>
                                <li>&rsaquo; GraphQL</li>
                                <li>&rsaquo; Postgres & MongoDB</li>
                            </ul>
                        </div>

                        <!-- Mobile & CMS -->
                        <div>
                            <h4 style="color: #f43f5e; font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 1.5rem; border-bottom: 1px solid rgba(244,63,94,0.3); padding-bottom: 0.5rem;">Mobile / CMS</h4>
                            <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.75rem; color: #cbd5e1; font-family: monospace; font-size: 1rem;">
                                <li>&rsaquo; React Native</li>
                                <li>&rsaquo; iOS & Android</li>
                                <li>&rsaquo; WordPress & Webflow</li>
                                <li>&rsaquo; Shopify</li>
                                <li>&rsaquo; Sanity & Contentful</li>
                            </ul>
                        </div>

                        <!-- DevOps -->
                        <div>
                            <h4 style="color: #f59e0b; font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 1.5rem; border-bottom: 1px solid rgba(245,158,11,0.3); padding-bottom: 0.5rem;">DevOps</h4>
                            <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.75rem; color: #cbd5e1; font-family: monospace; font-size: 1rem;">
                                <li>&rsaquo; Vercel & Netlify</li>
                                <li>&rsaquo; AWS</li>
                                <li>&rsaquo; Google Cloud</li>
                                <li>&rsaquo; GitHub CI/CD</li>
                                <li>&rsaquo; Docker</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Development Standards -->
            <div class="fade-up" style="margin-bottom: 8rem;">
                <h2 style="font-size: 3rem; text-align: center; margin-bottom: 3rem;">Our Development Standards</h2>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; overflow: hidden;">
                    
                    <div style="background: rgba(10,10,14,0.9); padding: 3rem; position: relative;">
                        <h4 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-code" style="color: #38bdf8;"></i> Clean Code</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">We write code that is readable, well-documented, and built to last. No spaghetti code, no shortcuts, no technical debt handed off to your team.</p>
                    </div>
                    
                    <div style="background: rgba(10,10,14,0.9); padding: 3rem;">
                        <h4 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-lightning" style="color: #eab308;"></i> Performance First</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">Every product we build is optimized for speed &mdash; fast load times, efficient database queries, optimized assets, and infrastructure that handles traffic spikes.</p>
                    </div>

                    <div style="background: rgba(10,10,14,0.9); padding: 3rem;">
                        <h4 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-shield-check" style="color: #10b981;"></i> Security Built In</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">Security is never an afterthought. We follow industry best practices for data protection, authentication, input validation, and secure API communication from day one.</p>
                    </div>

                    <div style="background: rgba(10,10,14,0.9); padding: 3rem;">
                        <h4 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-trend-up" style="color: #a855f7;"></i> Scalability By Design</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">We architect your product to grow with your business. Whether you go from 100 to 100,000 users, your foundation will hold.</p>
                    </div>

                    <div style="background: rgba(10,10,14,0.9); padding: 3rem; grid-column: auto;">
                        <h4 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-devices" style="color: #f43f5e;"></i> Cross-Browser Testing</h4>
                        <p style="color: var(--text-secondary); line-height: 1.6; margin: 0;">Every product we ship is rigorously tested across browsers, devices, and operating systems &mdash; because your users don't all use the same setup.</p>
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
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(56,189,248,0.1); color: #38bdf8; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(56,189,248,0.3);">1</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Discovery & Architecture</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We audit requirements, define technical scope, choose the stack, and plan the database schema before writing code.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(56,189,248,0.1); color: #38bdf8; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(56,189,248,0.3);">2</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Development</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We build in focused sprints with regular updates and demos so you're never left in the dark.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(56,189,248,0.1); color: #38bdf8; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(56,189,248,0.3);">3</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Quality Assurance</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We test everything &mdash; functionality, performance, security, and compatibility &mdash; before it goes live.</span>
                            </div>
                        </li>
                        <li style="display: flex; gap: 1.5rem; align-items: flex-start;">
                            <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(56,189,248,0.1); color: #38bdf8; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; border: 1px solid rgba(56,189,248,0.3);">4</div>
                            <div>
                                <strong style="display: block; font-size: 1.15rem; margin-bottom: 0.25rem;">Launch & Support</strong>
                                <span style="color: var(--text-secondary); line-height: 1.6;">We deploy with zero-downtime releases and stay on hand post-launch to squash bugs and keep things smooth.</span>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- What You Get -->
                <div class="glass-card" style="padding: 3rem; background: rgba(255,255,255,0.02); border-color: rgba(56, 189, 248, 0.2);">
                    <h2 style="font-size: 2.5rem; margin-bottom: 2rem;">What You Get</h2>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.25rem; font-size: 1.1rem; color: var(--text-primary);">
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #38bdf8; font-size: 1.5rem;"></i> Production-ready, clean and documented code</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #38bdf8; font-size: 1.5rem;"></i> Fully responsive across all devices and browsers</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #38bdf8; font-size: 1.5rem;"></i> Performance and speed optimized</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #38bdf8; font-size: 1.5rem;"></i> Security best practices throughout</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #38bdf8; font-size: 1.5rem;"></i> Third-party integrations and API connections</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #38bdf8; font-size: 1.5rem;"></i> CMS setup for easy content management</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #38bdf8; font-size: 1.5rem;"></i> Full handoff with documentation</li>
                        <li style="display: flex; align-items: center; gap: 1rem;"><i class="ph ph-check-circle" style="color: #38bdf8; font-size: 1.5rem;"></i> Post-launch support on every package</li>
                    </ul>
                </div>
            </div>

            <!-- Pricing Table -->
            <div class="fade-up" style="margin-bottom: 8rem;">
                <h2 style="font-size: 3.5rem; text-align: center; margin-bottom: 3rem;">Development Packages</h2>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                    
                    <!-- Starter -->
                    <div class="glass-card" style="padding: 3rem; text-align: center; border-radius: 24px;">
                        <h3 style="font-size: 1.75rem; margin-bottom: 1rem; color: var(--text-secondary);">Starter</h3>
                        <div style="font-size: 3rem; font-weight: bold; color: #38bdf8; margin-bottom: 2rem;">$500</div>
                        <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; display: flex; flex-direction: column; gap: 1rem; color: var(--text-secondary);">
                            <li><strong>Up to 5</strong> pages</li>
                            <li><strong>1 round</strong> Revisions</li>
                            <li><strong>7 days</strong> Delivery</li>
                            <li><strong>30 days</strong> Support</li>
                        </ul>
                        <a href="hire.html" class="btn btn-outline" style="width: 100%;">Select Starter</a>
                    </div>
                    
                    <!-- Growth -->
                    <div class="glass-card beam-card" style="padding: 3rem; text-align: center; border-radius: 24px; position: relative; overflow: hidden; transform: scale(1.05); z-index: 10; border-color: rgba(56, 189, 248, 0.4);">
                        <div class="y2k-badge" style="position: absolute; top: 1rem; right: 1rem; font-size: 0.75rem; padding: 0.25rem 0.75rem; background: #38bdf8; color: #000;">MOST POPULAR</div>
                        <h3 style="font-size: 1.75rem; margin-bottom: 1rem; color: var(--text-primary);">Growth</h3>
                        <div style="font-size: 3.5rem; font-weight: bold; color: #fff; margin-bottom: 2rem;">$1,000</div>
                        <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; display: flex; flex-direction: column; gap: 1rem; color: var(--text-primary);">
                            <li><strong>Up to 10</strong> pages</li>
                            <li><strong>3 rounds</strong> Revisions</li>
                            <li><strong>14 days</strong> Delivery</li>
                            <li><strong>60 days</strong> Support</li>
                        </ul>
                        <a href="hire.html" class="btn btn-primary" style="width: 100%; background: #38bdf8; color: #000;">Select Growth</a>
                    </div>
                    
                    <!-- Premium -->
                    <div class="glass-card" style="padding: 3rem; text-align: center; border-radius: 24px;">
                        <h3 style="font-size: 1.75rem; margin-bottom: 1rem; color: var(--text-secondary);">Premium</h3>
                        <div style="font-size: 3rem; font-weight: bold; color: #38bdf8; margin-bottom: 2rem;">$2,000</div>
                        <ul style="list-style: none; padding: 0; margin: 0 0 2rem 0; display: flex; flex-direction: column; gap: 1rem; color: var(--text-secondary);">
                            <li><strong>Unlimited</strong> pages</li>
                            <li><strong>Unlimited</strong> Revisions</li>
                            <li><strong>21 days</strong> Delivery</li>
                            <li><strong>90 days</strong> Support</li>
                        </ul>
                        <a href="hire.html" class="btn btn-outline" style="width: 100%;">Select Premium</a>
                    </div>
                </div>
            </div>

            <!-- Why Us / CTA -->
            <div class="glass-card fade-up" style="padding: 6rem; text-align: center; background: linear-gradient(135deg, rgba(56, 189, 248, 0.08), rgba(2, 132, 199, 0.08)); border-radius: 32px; border: 1px solid rgba(56, 189, 248, 0.1); position: relative; overflow: hidden;">
                <h2 style="font-size: 3.5rem; margin-bottom: 2rem;">Why Rayvotech</h2>
                <p style="font-size: 1.35rem; line-height: 1.8; color: var(--text-secondary); max-width: 900px; margin: 0 auto 2rem auto;">
                    We've seen what happens when businesses cut corners on development &mdash; slow websites, broken features, security vulnerabilities, and codebases that nobody can maintain. That's not what we do. At Rayvotech, every product we ship reflects our commitment to quality, performance, and craft.
                </p>
                <p style="font-size: 1.35rem; color: var(--text-primary); font-weight: 500; margin-bottom: 4rem;">
                    We take pride in building things that work &mdash; beautifully and reliably &mdash; for the businesses and users who depend on them every day.
                </p>
                
                <h3 style="font-size: 2.5rem; margin-bottom: 1rem; color: #38bdf8;">Ready to build your next digital product?</h3>
                <p style="color: var(--text-secondary); font-size: 1.35rem; margin-bottom: 3.5rem;">Let's turn your idea into something the internet hasn't seen before.</p>
                
                <a href="hire.html" class="btn btn-primary btn-lg" style="padding: 1.25rem 3rem; font-size: 1.25rem; border-radius: 50px; background: #38bdf8; color: #000; border: none;">Start Your Project &rarr;</a>
            </div>

        </div>
    </section>
    """

    final_content = content[:nav_end_idx] + "\n" + new_body + "\n    " + content[footer_start_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Web Dev page rebuilt to Awwwards standards. Ready for Tim Cook & Bill Gates.")
else:
    print("Could not find boundaries for overhaul.")
