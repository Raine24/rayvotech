import re

html_file = 'terms.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# The content section to replace is between <!-- Content --> and <!-- Footer -->
# Wait, let's just replace the inner contents of the section that contains the placeholder.
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
                    
                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 0; margin-bottom: 1rem;">1. Introduction</h3>
                    <p style="margin-bottom: 1.5rem;">Welcome to Rayvotech. These Terms & Conditions govern your use of our website and services. By accessing our website or engaging our services, you agree to be bound by these terms in full. If you disagree with any part of these terms, please do not use our website or services.</p>
                    <p style="margin-bottom: 2.5rem;">Rayvotech is a digital agency based at 9029 Burt St, Omaha, Nebraska 68114, USA. For any questions regarding these terms, contact us at info@rayvotech.com.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">2. Services</h3>
                    <p style="margin-bottom: 2.5rem;">Rayvotech provides digital services including but not limited to website design, UI/UX architecture, web and app development, and SEO & conversion optimization. The specific scope, deliverables, timeline, and pricing of each engagement will be outlined in a separate project agreement or proposal agreed upon by both parties before work begins.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">3. Client Responsibilities</h3>
                    <p style="margin-bottom: 1rem;">To ensure the smooth delivery of your project, you agree to:</p>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Provide all required assets, content, and information in a timely manner</li>
                        <li style="margin-bottom: 0.5rem;">Assign a primary point of contact for the duration of the project</li>
                        <li style="margin-bottom: 0.5rem;">Provide clear and consolidated feedback within agreed timeframes</li>
                        <li style="margin-bottom: 0.5rem;">Ensure all materials provided to Rayvotech are legally owned by you or that you have the rights to use them</li>
                        <li style="margin-bottom: 0.5rem;">Make payments according to the agreed schedule</li>
                    </ul>
                    <p style="margin-bottom: 2.5rem;">Delays caused by late delivery of client materials may result in revised project timelines. Rayvotech will not be held responsible for project delays resulting from client inaction.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">4. Payment Terms</h3>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">A deposit of 50% of the total project fee is required before work begins</li>
                        <li style="margin-bottom: 0.5rem;">The remaining balance is due upon project completion and before final files or live deployment are delivered</li>
                        <li style="margin-bottom: 0.5rem;">All payments are non-refundable once work has commenced on the agreed scope</li>
                        <li style="margin-bottom: 0.5rem;">For ongoing or retainer services, payments are due at the beginning of each billing cycle</li>
                        <li style="margin-bottom: 0.5rem;">Rayvotech reserves the right to pause or suspend work on any project where payment is overdue by more than 7 business days</li>
                    </ul>
                    <p style="margin-bottom: 2.5rem;">All prices are listed in US Dollars (USD) unless otherwise stated.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">5. Revisions & Scope</h3>
                    <p style="margin-bottom: 1.5rem;">Revisions are included as outlined in your chosen package — 1 round for Starter, 3 rounds for Growth, and unlimited rounds for Premium. A revision is defined as minor adjustments to existing designs or content within the agreed project scope.</p>
                    <p style="margin-bottom: 2.5rem;">Requests that fall outside the original agreed scope — including additional pages, new features, or significant redesigns — will be treated as new work and quoted separately. Rayvotech will always notify you before proceeding with any out-of-scope work that incurs additional cost.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">6. Intellectual Property</h3>
                    <p style="margin-bottom: 1.5rem;">Upon receipt of full and final payment, all rights to the final deliverables produced by Rayvotech for your project are transferred to you, the client. This includes design files, source code, and all associated assets specific to your project.</p>
                    <p style="margin-bottom: 1rem;">Rayvotech retains the right to:</p>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Display completed work in our portfolio and marketing materials unless otherwise agreed in writing</li>
                        <li style="margin-bottom: 0.5rem;">Retain ownership of any proprietary tools, frameworks, templates, or processes used in the delivery of your project that are not specific to your brand</li>
                    </ul>
                    <p style="margin-bottom: 2.5rem;">Third-party assets such as stock images, fonts, plugins, or software licenses remain subject to their respective licensing agreements and are the client's responsibility to maintain beyond the project delivery.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">7. Confidentiality</h3>
                    <p style="margin-bottom: 2.5rem;">Both parties agree to keep confidential any sensitive business information, trade secrets, or proprietary data shared during the course of the project. This obligation remains in effect for 2 years following the completion or termination of a project.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">8. Post-Launch Support</h3>
                    <p style="margin-bottom: 2.5rem;">Post-launch support is included in all packages — 30 days for Starter, 60 days for Growth, and 90 days for Premium. Support covers bug fixes, minor content updates, and technical issues arising directly from our work. It does not cover new feature requests, additional design work, or issues caused by third-party platforms or client modifications.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">9. Limitation of Liability</h3>
                    <p style="margin-bottom: 1rem;">Rayvotech will not be held liable for:</p>
                    <ul style="margin-bottom: 2.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Any indirect, incidental, or consequential damages arising from the use of our services</li>
                        <li style="margin-bottom: 0.5rem;">Loss of revenue, data, or business opportunities resulting from project delays, technical issues, or service interruptions beyond our reasonable control</li>
                        <li style="margin-bottom: 0.5rem;">Issues arising from third-party tools, platforms, plugins, or hosting environments not directly managed by Rayvotech</li>
                        <li style="margin-bottom: 0.5rem;">Any damages exceeding the total amount paid by the client for the specific project in question</li>
                    </ul>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">10. Warranties & Disclaimers</h3>
                    <p style="margin-bottom: 1.5rem;">Rayvotech warrants that all work delivered will be completed with professional skill and care. We do not guarantee specific search engine rankings, traffic volumes, or revenue outcomes as these are subject to factors outside our direct control.</p>
                    <p style="margin-bottom: 2.5rem;">All services are provided on an "as delivered" basis following client sign-off. Rayvotech is not responsible for issues arising from client modifications made after project handoff.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">11. Termination</h3>
                    <p style="margin-bottom: 1rem;">Either party may terminate a project engagement with written notice. In the event of termination:</p>
                    <ul style="margin-bottom: 2.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">All work completed up to the point of termination will be invoiced and payment will be due within 7 business days</li>
                        <li style="margin-bottom: 0.5rem;">The deposit is non-refundable under any circumstances</li>
                        <li style="margin-bottom: 0.5rem;">Final deliverables will only be released upon receipt of all outstanding payments</li>
                        <li style="margin-bottom: 0.5rem;">Rayvotech reserves the right to terminate any engagement immediately in cases of client misconduct, non-payment, or breach of these terms</li>
                    </ul>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">12. Governing Law</h3>
                    <p style="margin-bottom: 2.5rem;">These Terms & Conditions are governed by and construed in accordance with the laws of the State of Nebraska, United States. Any disputes arising from these terms or our services will be subject to the exclusive jurisdiction of the courts of Omaha, Nebraska.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">13. Changes to These Terms</h3>
                    <p style="margin-bottom: 2.5rem;">Rayvotech reserves the right to update or modify these Terms & Conditions at any time. Changes will be posted on our website with an updated date. Continued use of our services following any changes constitutes your acceptance of the revised terms.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">14. Contact Us</h3>
                    <p style="margin-bottom: 0.5rem;">If you have any questions about these Terms & Conditions, please contact us:</p>
                    <p style="margin-bottom: 0.5rem;"><strong>Rayvotech</strong></p>
                    <p style="margin-bottom: 0.5rem;">9029 Burt St, Omaha, Nebraska 68114, USA</p>
                    <p style="margin-bottom: 0;">📧 info@rayvotech.com</p>
                    
                </div>
            </div>
        </div>
    </section>
    
    """
    
    # Also update the hero header from "Last Updated: October 2026" to "Last Updated: March 2026"
    updated_content = content[:start_idx] + new_content + content[end_idx:]
    updated_content = updated_content.replace('October 2026', 'March 2026')
    updated_content = updated_content.replace('Terms & Conditions —</title>', 'Terms & Conditions | Rayvotech</title>')
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("terms.html successfully updated with exact copy!")
else:
    print("Could not find the section boundaries in terms.html.")
