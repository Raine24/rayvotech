import re

html_file = 'service-ui-ux-design.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# We will replace the <div class="article-content"...> block
new_article = """<div class="article-content fade-up" style="max-width: 900px; margin: 0 auto; background: transparent; padding: 0;">
            <!-- Drop cap / Lead Paragraph -->
            <p style="font-size: 1.35rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 2rem; font-weight: 600;">
                There is a version of your digital product that your users love so much they tell other people about it. A version where everything is exactly where they expect it to be. Where every interaction feels smooth and satisfying. Where the path from landing on your page to completing a purchase, booking a call, or signing up for your service feels so natural that they barely notice they are being guided at all. That version exists. Getting there is what our UI/UX design service is built to do.
            </p>
            
            <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 3rem;">
                At Rayvotech, we believe that design is not decoration — it is problem solving. Our UI/UX service goes far beyond making things look good. We architect the entire experience your users have when they interact with your digital product, from the very first moment they arrive to the moment they complete the action you most want them to take. Every element of that journey is studied, considered, tested, and refined until it works exactly as it should.
            </p>

            <!-- Huge Image Break -->
            <div style="width: 100%; height: 500px; border-radius: 24px; overflow: hidden; margin: 4rem 0; box-shadow: 0 30px 60px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.05); position: relative;">
                <img src="https://i.imgur.com/l5BnUoy.jpg" alt="UI/UX Design Mockup" style="width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform 0.5s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </div>

            <h3 style="font-size: 2rem; color: var(--color-accent); margin-bottom: 1.5rem;">The Architecture of Experience</h3>
            <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 4rem;">
                UI stands for User Interface — the visual layer that users interact with directly. Buttons, menus, forms, cards, icons, typography, color, spacing. Every visual component that makes up the surface of your product. UX stands for User Experience — the logic, structure, and flow beneath that surface. How information is organized. How users move from one section to another. How friction is identified and eliminated. How the product makes people feel at every stage of their interaction with it. We design both, together, because they cannot be separated. A beautiful interface built on a confusing structure will still frustrate your users. A logical structure wrapped in a poor visual design will still lose their trust.
            </p>

            <h3 style="font-size: 2rem; color: var(--text-primary); margin-bottom: 2rem;">Our Design Process</h3>
            
            <div style="display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 4rem;">
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 2.5rem; border-radius: 20px; transition: all 0.3s;" onmouseover="this.style.borderColor='rgba(0, 230, 240, 0.4)'; this.style.transform='translateX(10px)';" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='translateX(0)';">
                    <h4 style="color: var(--color-accent); font-size: 1.25rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-magnifying-glass"></i> 1. Research & Discovery</h4>
                    <p style="font-size: 1.05rem; color: var(--text-secondary); line-height: 1.7; margin: 0;">Our process begins with research. We do not make assumptions about what your users want or need. We study them. We develop detailed user personas that represent your real audience — their goals, their frustrations, their behaviors, and their expectations. We map out every journey a user might take through your product, identifying where they are likely to get confused, where they are likely to drop off, and where the greatest opportunities to delight them exist.</p>
                </div>
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 2.5rem; border-radius: 20px; transition: all 0.3s;" onmouseover="this.style.borderColor='rgba(0, 230, 240, 0.4)'; this.style.transform='translateX(10px)';" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='translateX(0)';">
                    <h4 style="color: var(--color-accent); font-size: 1.25rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-tree-structure"></i> 2. Information Architecture</h4>
                    <p style="font-size: 1.05rem; color: var(--text-secondary); line-height: 1.7; margin: 0;">From that research, we build information architecture — a clear and logical blueprint of how your content and features should be organized to serve your users most effectively. This is the skeleton of your product, and getting it right at this stage saves enormous time and cost later in the process.</p>
                </div>
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 2.5rem; border-radius: 20px; transition: all 0.3s;" onmouseover="this.style.borderColor='rgba(0, 230, 240, 0.4)'; this.style.transform='translateX(10px)';" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='translateX(0)';">
                    <h4 style="color: var(--color-accent); font-size: 1.25rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-blueprint"></i> 3. Wireframing</h4>
                    <p style="font-size: 1.05rem; color: var(--text-secondary); line-height: 1.7; margin: 0;">With the architecture established, we move into wireframing. Wireframes are simplified, structural representations of each screen in your product. They show layout and flow without the distraction of color or visual detail, allowing us to focus entirely on how things work before we decide how they look. This is where we solve the hard problems — where we test different approaches, eliminate confusion, and ensure that every screen serves a clear purpose in the user's journey.</p>
                </div>
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 2.5rem; border-radius: 20px; transition: all 0.3s;" onmouseover="this.style.borderColor='rgba(0, 230, 240, 0.4)'; this.style.transform='translateX(10px)';" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='translateX(0)';">
                    <h4 style="color: var(--color-accent); font-size: 1.25rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-cursor-click"></i> 4. Interactive Prototyping</h4>
                    <p style="font-size: 1.05rem; color: var(--text-secondary); line-height: 1.7; margin: 0;">Once wireframes are approved, we build interactive prototypes that simulate the real experience of using your product. These prototypes are tested with real users, generating feedback that is incorporated into the design before development begins. This testing phase is one of the most valuable parts of our process, because it catches problems early when they are cheap to fix rather than late when they are expensive.</p>
                </div>
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 2.5rem; border-radius: 20px; transition: all 0.3s;" onmouseover="this.style.borderColor='rgba(0, 230, 240, 0.4)'; this.style.transform='translateX(10px)';" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='translateX(0)';">
                    <h4 style="color: var(--color-accent); font-size: 1.25rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;"><i class="ph ph-paint-brush"></i> 5. Final Visual Design</h4>
                    <p style="font-size: 1.05rem; color: var(--text-secondary); line-height: 1.7; margin: 0;">The final UI design layer brings everything to life visually — applying your brand's color system, typography, imagery, and motion to create an interface that is not only functional but genuinely beautiful. We build design systems that ensure consistency across every screen and every interaction, and we document everything so your development team can build with confidence and your brand can scale without losing coherence.</p>
                </div>
            </div>

            <div style="padding: 3rem; background: linear-gradient(135deg, rgba(255, 95, 86, 0.1), rgba(0, 230, 240, 0.1)); border-radius: 24px; border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 4rem;">
                <p style="font-size: 1.2rem; line-height: 1.8; color: var(--text-primary); font-weight: 600; margin: 0;">
                    Investing in UI/UX design is one of the highest-return decisions a business can make. Companies that prioritize user experience consistently outperform those that do not — with higher conversion rates, lower customer acquisition costs, stronger brand loyalty, and better word-of-mouth. In a digital landscape where your competitors are just one click away, the experience you deliver is your most powerful differentiator.
                </p>
            </div>

            <div style="text-align: center; margin-bottom: 2rem;">
                <a href="hire.html" class="btn btn-primary btn-lg">Start Your Project <i class="ph ph-arrow-right"></i></a>
            </div>
        </div>"""

match = re.search(r'<div class="article-content fade-up".*?</div>\s*</div>\s*</div>', content, re.DOTALL)
if match:
    # Need to be careful because the regex matches up to a certain point.
    pass

# Simpler replacement strategy:
# We know <div class="article-content fade-up" starts the block, and the next section is <!-- Footer -->
start_idx = content.find('<div class="article-content fade-up"')
end_idx = content.find('</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    final_content = content[:start_idx] + new_article + '\\n    ' + content[end_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("UI/UX page redesigned successfully.")
else:
    print("Could not find replacement boundaries.")
