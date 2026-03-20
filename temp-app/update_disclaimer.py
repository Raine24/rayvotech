import re

html_file = 'disclaimer.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Content -->'
end_marker = '<!-- Footer -->'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = """<!-- Content -->
    <section class="section-padding" style="padding-top: 2rem; padding-bottom: 6rem;">
        <div class="container" style="max-width: 900px;">
            <div class="glass-card fade-up" style="padding: 4rem; border-radius: 24px; background: rgba(10,10,14,0.6); border: 1px solid rgba(255,255,255,0.05);">
                
                <div class="legal-content" style="color: var(--text-secondary); line-height: 1.8; font-size: 1.1rem;">
                    
                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 0; margin-bottom: 1rem;">1. General Information</h3>
                    <p style="margin-bottom: 1.5rem;">The information provided on the Rayvotech website (rayvotech.com) is for general informational purposes only. While we make every effort to keep the content accurate, complete, and up to date, Rayvotech makes no warranties or representations of any kind — express or implied — about the completeness, accuracy, reliability, suitability, or availability of any information, products, services, or related graphics contained on this website.</p>
                    <p style="margin-bottom: 2.5rem;">Any reliance you place on such information is strictly at your own risk.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">2. No Professional Advice</h3>
                    <p style="margin-bottom: 1.5rem;">The content on this website does not constitute professional legal, financial, technical, or business advice. Nothing on this site should be interpreted as a substitute for professional consultation tailored to your specific circumstances.</p>
                    <p style="margin-bottom: 2.5rem;">If you require advice specific to your situation, we strongly recommend consulting a qualified professional in the relevant field. For project-specific guidance, contact us directly at info@rayvotech.com.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">3. Results Disclaimer</h3>
                    <p style="margin-bottom: 1.5rem;">Rayvotech does not guarantee specific results from the use of our services. While we are committed to delivering high-quality work and apply industry best practices across all our projects, outcomes such as search engine rankings, website traffic, conversion rates, revenue growth, or business performance are influenced by many factors outside our direct control.</p>
                    <p style="margin-bottom: 2.5rem;">Any examples, case studies, or results referenced on this website are illustrative of past performance and are not a guarantee of future results. Every business is unique and individual results will vary.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">4. Website Accuracy</h3>
                    <p style="margin-bottom: 1.5rem;">We strive to ensure that all information on our website — including service descriptions, pricing, timelines, and package details — is current and accurate at the time of publication. However, this information is subject to change without notice.</p>
                    <p style="margin-bottom: 2.5rem;">Pricing, deliverables, and timelines presented on this website are indicative only. Final project scope, cost, and delivery schedule will always be confirmed in a written proposal or agreement before work begins.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">5. Third-Party Links & Resources</h3>
                    <p style="margin-bottom: 1.5rem;">Our website may contain links to third-party websites, tools, platforms, or resources for your convenience and reference. These links do not constitute an endorsement or recommendation by Rayvotech of any third-party content, products, or services.</p>
                    <p style="margin-bottom: 2.5rem;">Rayvotech has no control over the nature, content, or availability of third-party sites. We accept no responsibility for any loss or damage that may arise from your use of third-party websites or resources.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">6. Technology & Compatibility</h3>
                    <p style="margin-bottom: 1.5rem;">Rayvotech builds digital products using modern technologies and industry-standard best practices. However, we cannot guarantee that all websites, applications, or digital products we deliver will function identically across every browser, device, operating system, or third-party platform — particularly as technology environments evolve over time.</p>
                    <p style="margin-bottom: 2.5rem;">Post-launch support is included in all packages within the agreed support period. Beyond that period, ongoing compatibility and maintenance are the responsibility of the client unless a separate support agreement is in place.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">7. Intellectual Property</h3>
                    <p style="margin-bottom: 2.5rem;">All content on the Rayvotech website — including text, graphics, logos, icons, images, and code — is the intellectual property of Rayvotech unless otherwise stated. Unauthorized reproduction, distribution, or use of any content from this website without prior written permission from Rayvotech is strictly prohibited.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">8. Limitation of Liability</h3>
                    <p style="margin-bottom: 1rem;">To the fullest extent permitted by law, Rayvotech and its team members, partners, and affiliates shall not be liable for any direct, indirect, incidental, consequential, or special damages arising from:</p>
                    <ul style="margin-bottom: 2.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Your use of or inability to use this website</li>
                        <li style="margin-bottom: 0.5rem;">Any errors or omissions in website content</li>
                        <li style="margin-bottom: 0.5rem;">Any interruption or unavailability of the website</li>
                        <li style="margin-bottom: 0.5rem;">Any third-party content, tools, or platforms referenced or linked on this site</li>
                        <li style="margin-bottom: 0.5rem;">Any decisions made based on information found on this website</li>
                    </ul>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">9. Indemnification</h3>
                    <p style="margin-bottom: 2.5rem;">By using our website or services, you agree to indemnify and hold harmless Rayvotech, its team members, partners, and affiliates from any claims, damages, losses, or expenses — including reasonable legal fees — arising from your use of our website, your violation of these terms, or your infringement of any third-party rights.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">10. Governing Law</h3>
                    <p style="margin-bottom: 2.5rem;">This Disclaimer is governed by the laws of the State of Nebraska, United States. Any disputes arising in connection with this Disclaimer shall be subject to the exclusive jurisdiction of the courts of Omaha, Nebraska.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">11. Changes to This Disclaimer</h3>
                    <p style="margin-bottom: 2.5rem;">Rayvotech reserves the right to update or modify this Disclaimer at any time without prior notice. Changes will be reflected by updating the date at the top of this page. Your continued use of this website following any changes constitutes your acceptance of the updated Disclaimer.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">12. Contact Us</h3>
                    <p style="margin-bottom: 0.5rem;">If you have any questions about this Disclaimer, please contact us:</p>
                    <p style="margin-bottom: 0.5rem;"><strong>Rayvotech</strong></p>
                    <p style="margin-bottom: 0.5rem;">9029 Burt St, Omaha, Nebraska 68114, USA</p>
                    <p style="margin-bottom: 0;">📧 info@rayvotech.com</p>
                    
                </div>
            </div>
        </div>
    </section>
    
    """
    
    updated_content = content[:start_idx] + new_content + content[end_idx:]
    updated_content = updated_content.replace('October 2026', 'March 2026')
    updated_content = updated_content.replace('Disclaimer —</title>', 'Disclaimer | Rayvotech</title>')
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("disclaimer.html successfully updated with exact copy!")
else:
    print("Could not find the section boundaries in disclaimer.html.")
