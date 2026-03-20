with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_cards = """
                <!-- Project 9 -->
                <div class="testimonial-card fade-up delay-2 glass-card" style="padding: 0; overflow: hidden; justify-content: flex-start;">
                    <div style="height: 450px; background: url('https://i.imgur.com/D4ciMv4.jpg') center/cover no-repeat; border-bottom: 1px solid rgba(255,255,255,0.08);"></div>
                    <div style="padding: 2.5rem;">
                        <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Tibico Health</h3>
                        <p class="tc-quote" style="margin-bottom: 2rem; font-style: normal;">Modern health and wellness platform designed to enhance user engagement and provide seamless content delivery for nutritional guides.</p>
                        <div class="tech-icons" style="margin-bottom:0; justify-content:flex-start;">
                            <span class="tech-badge"><i class="ph ph-heartbeat"></i> Health Tech</span>
                            <span class="tech-badge"><i class="ph ph-paint-brush"></i> UI/UX Design</span>
                        </div>
                    </div>
                </div>

                <!-- Project 10 -->
                <div class="testimonial-card fade-up glass-card" style="padding: 0; overflow: hidden; justify-content: flex-start;">
                    <div style="height: 450px; background: url('https://i.imgur.com/958DvKQ.jpg') center/cover no-repeat; border-bottom: 1px solid rgba(255,255,255,0.08);"></div>
                    <div style="padding: 2.5rem;">
                        <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Women's Foundation</h3>
                        <p class="tc-quote" style="margin-bottom: 2rem; font-style: normal;">Empowering non-profit website crafted to drive donations, showcase impact initiatives, and streamline community outreach programs.</p>
                        <div class="tech-icons" style="margin-bottom:0; justify-content:flex-start;">
                            <span class="tech-badge"><i class="ph ph-globe"></i> Non-Profit</span>
                            <span class="tech-badge"><i class="ph ph-magnifying-glass"></i> SEO</span>
                        </div>
                    </div>
                </div>

                <!-- Project 11 -->
                <div class="testimonial-card fade-up delay-1 glass-card" style="padding: 0; overflow: hidden; justify-content: flex-start;">
                    <div style="height: 450px; background: url('https://i.imgur.com/JrvsgXo.jpg') center/cover no-repeat; border-bottom: 1px solid rgba(255,255,255,0.08);"></div>
                    <div style="padding: 2.5rem;">
                        <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Stapende Auto</h3>
                        <p class="tc-quote" style="margin-bottom: 2rem; font-style: normal;">Sleek automotive showcase platform featuring dynamic inventory searching, high-resolution imagery, and lead generation tools.</p>
                        <div class="tech-icons" style="margin-bottom:0; justify-content:flex-start;">
                            <span class="tech-badge"><i class="ph ph-car"></i> Auto</span>
                            <span class="tech-badge"><i class="ph ph-rocket"></i> Optimization</span>
                        </div>
                    </div>
                </div>

                <!-- Project 12 -->
                <div class="testimonial-card fade-up delay-2 glass-card" style="padding: 0; overflow: hidden; justify-content: flex-start;">
                    <div style="height: 450px; background: url('https://i.imgur.com/lxfKiWw.jpg') center/cover no-repeat; border-bottom: 1px solid rgba(255,255,255,0.08);"></div>
                    <div style="padding: 2.5rem;">
                        <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Absolute Collagen</h3>
                        <p class="tc-quote" style="margin-bottom: 2rem; font-style: normal;">High-converting beauty e-commerce experience tailored to maximize user retention and simplify recurring subscription models.</p>
                        <div class="tech-icons" style="margin-bottom:0; justify-content:flex-start;">
                            <span class="tech-badge"><i class="ph ph-shopping-cart"></i> E-Commerce</span>
                            <span class="tech-badge"><i class="ph ph-chart-line-up"></i> CRO</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

# Replace the closing tags of the grid with the new cards + the closing tags
target = """            </div>
        </div>
    </section>"""

if target in html:
    html = html.replace(target, new_cards)
    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success")
else:
    print("Target not found")
