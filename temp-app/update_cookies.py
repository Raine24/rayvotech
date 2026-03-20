import re

html_file = 'cookies.html'

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
                    
                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 0; margin-bottom: 1rem;">1. Introduction</h3>
                    <p style="margin-bottom: 1.5rem;">At Rayvotech, we believe in being fully transparent about how we collect and use data. This Cookie Policy explains what cookies are, how we use them on our website, and what choices you have regarding their use.</p>
                    <p style="margin-bottom: 1.5rem;">By continuing to use our website, you consent to our use of cookies as described in this policy. If you do not agree, you can adjust your browser settings or discontinue use of our website.</p>
                    <p style="margin-bottom: 2.5rem;">Rayvotech is based at 9029 Burt St, Omaha, Nebraska 68114, USA. For any questions about this policy, contact us at info@rayvotech.com.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">2. What Are Cookies</h3>
                    <p style="margin-bottom: 1.5rem;">Cookies are small text files that are placed on your device — computer, tablet, or smartphone — when you visit a website. They are widely used to make websites work more efficiently, remember your preferences, and provide website owners with analytical information about how their site is being used.</p>
                    <p style="margin-bottom: 1rem;">Cookies can be:</p>
                    <ul style="margin-bottom: 2.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;"><strong>Session cookies</strong> — temporary cookies that are deleted when you close your browser</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Persistent cookies</strong> — cookies that remain on your device for a set period of time or until you delete them manually</li>
                        <li style="margin-bottom: 0.5rem;"><strong>First-party cookies</strong> — cookies set directly by Rayvotech</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Third-party cookies</strong> — cookies set by external services we use on our website</li>
                    </ul>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">3. Why We Use Cookies</h3>
                    <p style="margin-bottom: 1rem;">We use cookies to:</p>
                    <ul style="margin-bottom: 2.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Ensure our website functions correctly and securely</li>
                        <li style="margin-bottom: 0.5rem;">Remember your preferences and settings</li>
                        <li style="margin-bottom: 0.5rem;">Understand how visitors interact with our website</li>
                        <li style="margin-bottom: 0.5rem;">Measure the effectiveness of our content and marketing campaigns</li>
                        <li style="margin-bottom: 0.5rem;">Improve your overall experience on our site</li>
                        <li style="margin-bottom: 0.5rem;">Deliver relevant content to the right audience</li>
                    </ul>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">4. Types of Cookies We Use</h3>
                    
                    <h4 style="color: var(--text-primary); font-size: 1.25rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Essential Cookies</h4>
                    <p style="margin-bottom: 1rem;">These cookies are strictly necessary for our website to function. Without them, core features such as page navigation, form submissions, and security cannot work. These cookies do not collect any personally identifiable information and cannot be disabled without affecting website functionality.</p>
                    <p style="margin-bottom: 0.5rem;">Examples:</p>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Session management cookies</li>
                        <li style="margin-bottom: 0.5rem;">Security and authentication cookies</li>
                        <li style="margin-bottom: 0.5rem;">Load balancing cookies</li>
                    </ul>

                    <h4 style="color: var(--text-primary); font-size: 1.25rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Analytics & Performance Cookies</h4>
                    <p style="margin-bottom: 1rem;">These cookies help us understand how visitors use our website — which pages are visited most, how long users stay, where they came from, and where they exit. This data is aggregated and anonymous, and is used solely to improve the performance and content of our website.</p>
                    <p style="margin-bottom: 0.5rem;">Examples:</p>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Google Analytics</li>
                        <li style="margin-bottom: 0.5rem;">Hotjar</li>
                        <li style="margin-bottom: 0.5rem;">Microsoft Clarity</li>
                    </ul>

                    <h4 style="color: var(--text-primary); font-size: 1.25rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Functional Cookies</h4>
                    <p style="margin-bottom: 1rem;">These cookies allow our website to remember choices you make — such as your language preference or region — and provide enhanced, more personalized features. They may also be used to provide services you have requested.</p>
                    <p style="margin-bottom: 0.5rem;">Examples:</p>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Language and region preference cookies</li>
                        <li style="margin-bottom: 0.5rem;">Chat widget preferences</li>
                        <li style="margin-bottom: 0.5rem;">Form autofill cookies</li>
                    </ul>

                    <h4 style="color: var(--text-primary); font-size: 1.25rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Marketing & Targeting Cookies</h4>
                    <p style="margin-bottom: 1rem;">These cookies track your browsing activity across our website and may be used to show you relevant advertising on other platforms. They are also used to measure the effectiveness of our marketing campaigns. These cookies are only placed with your explicit consent.</p>
                    <p style="margin-bottom: 0.5rem;">Examples:</p>
                    <ul style="margin-bottom: 2.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Google Ads remarketing</li>
                        <li style="margin-bottom: 0.5rem;">Meta Pixel (Facebook/Instagram)</li>
                        <li style="margin-bottom: 0.5rem;">LinkedIn Insight Tag</li>
                    </ul>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">5. Third-Party Cookies</h3>
                    <p style="margin-bottom: 1.5rem;">Some cookies on our website are placed by third-party services that appear on our pages. These third parties may use cookies to collect information about your online activities across different websites. Rayvotech does not control these third-party cookies and they are subject to the respective privacy policies of those third parties.</p>
                    <p style="margin-bottom: 1rem;">Third-party services we use that may set cookies include:</p>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;"><strong>Google Analytics</strong> — website traffic and behavior analysis</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Google Ads</strong> — advertising and remarketing</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Meta Pixel</strong> — social media advertising and analytics</li>
                        <li style="margin-bottom: 0.5rem;"><strong>LinkedIn Insight Tag</strong> — professional audience analytics</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Hotjar</strong> — heatmaps and user behavior recording</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Intercom or similar</strong> — live chat and customer support</li>
                    </ul>
                    <p style="margin-bottom: 2.5rem;">We encourage you to review the privacy and cookie policies of these third-party services for more information on how they handle your data.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">6. Cookie Duration</h3>
                    <p style="margin-bottom: 1.5rem;">The length of time a cookie remains on your device depends on its type:</p>
                    <table style="width: 100%; border-collapse: collapse; margin-bottom: 1.5rem; background: rgba(0,0,0,0.2); border-radius: 8px; overflow: hidden;">
                        <thead>
                            <tr style="background: rgba(255,255,255,0.05); text-align: left;">
                                <th style="padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); color: var(--text-primary);">Cookie Type</th>
                                <th style="padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); color: var(--text-primary);">Duration</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);">Essential cookies</td>
                                <td style="padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);">Session or up to 1 year</td>
                            </tr>
                            <tr>
                                <td style="padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);">Analytics cookies</td>
                                <td style="padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);">Up to 2 years</td>
                            </tr>
                            <tr>
                                <td style="padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);">Functional cookies</td>
                                <td style="padding: 1rem; border-bottom: 1px solid rgba(255,255,255,0.05);">Up to 1 year</td>
                            </tr>
                            <tr>
                                <td style="padding: 1rem;">Marketing cookies</td>
                                <td style="padding: 1rem;">Up to 2 years</td>
                            </tr>
                        </tbody>
                    </table>
                    <p style="margin-bottom: 2.5rem;">These durations may vary depending on the specific cookie and third-party service involved.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">7. Managing Your Cookie Preferences</h3>
                    <p style="margin-bottom: 1.5rem;">You have full control over how cookies are used on your device. Here are your options:</p>
                    
                    <h4 style="color: var(--text-primary); font-size: 1.25rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Browser Settings</h4>
                    <p style="margin-bottom: 1rem;">Most web browsers allow you to control cookies through their settings. You can choose to block all cookies, delete existing cookies, or be notified when a new cookie is placed. Please note that disabling certain cookies may affect the functionality and performance of our website.</p>
                    <p style="margin-bottom: 0.5rem;">Here's how to manage cookies in popular browsers:</p>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;"><strong>Google Chrome</strong> — Settings → Privacy and Security → Cookies and other site data</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Mozilla Firefox</strong> — Settings → Privacy & Security → Cookies and Site Data</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Safari</strong> — Preferences → Privacy → Manage Website Data</li>
                        <li style="margin-bottom: 0.5rem;"><strong>Microsoft Edge</strong> — Settings → Cookies and Site Permissions</li>
                    </ul>

                    <h4 style="color: var(--text-primary); font-size: 1.25rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Opt-Out of Analytics</h4>
                    <p style="margin-bottom: 1.5rem;">You can opt out of Google Analytics tracking by installing the Google Analytics Opt-out Browser Add-on available at <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" style="color: var(--color-accent); text-decoration: none;">tools.google.com/dlpage/gaoptout</a>.</p>

                    <h4 style="color: var(--text-primary); font-size: 1.25rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Opt-Out of Advertising Cookies</h4>
                    <p style="margin-bottom: 0.5rem;">You can opt out of interest-based advertising through:</p>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;"><strong>Google</strong> — <a href="https://adssettings.google.com" target="_blank" style="color: var(--color-accent); text-decoration: none;">adssettings.google.com</a></li>
                        <li style="margin-bottom: 0.5rem;"><strong>Meta</strong> — <a href="https://facebook.com/ads/preferences" target="_blank" style="color: var(--color-accent); text-decoration: none;">facebook.com/ads/preferences</a></li>
                        <li style="margin-bottom: 0.5rem;"><strong>LinkedIn</strong> — <a href="https://linkedin.com/psettings/guest-controls" target="_blank" style="color: var(--color-accent); text-decoration: none;">linkedin.com/psettings/guest-controls</a></li>
                    </ul>

                    <h4 style="color: var(--text-primary); font-size: 1.25rem; margin-top: 1.5rem; margin-bottom: 0.5rem;">Cookie Consent Banner</h4>
                    <p style="margin-bottom: 2.5rem;">When you first visit our website, you will be presented with a cookie consent banner giving you the option to accept or decline non-essential cookies. You can update your preferences at any time by clearing your browser cookies and revisiting our site.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">8. What Happens If You Disable Cookies</h3>
                    <p style="margin-bottom: 1rem;">If you choose to disable or block cookies, some parts of our website may not function as intended. Specifically:</p>
                    <ul style="margin-bottom: 1.5rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Contact forms may not submit correctly</li>
                        <li style="margin-bottom: 0.5rem;">Your preferences may not be saved between visits</li>
                        <li style="margin-bottom: 0.5rem;">Analytics data will not be collected which limits our ability to improve your experience</li>
                        <li style="margin-bottom: 0.5rem;">You may see less relevant content or advertising</li>
                    </ul>
                    <p style="margin-bottom: 2.5rem;">Essential cookies cannot be disabled as they are required for the website to operate.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">9. Do Not Track</h3>
                    <p style="margin-bottom: 2.5rem;">Some browsers have a "Do Not Track" feature that signals to websites that you do not want your online activity tracked. Our website does not currently respond to Do Not Track signals. However, you can use the cookie management options outlined in Section 7 to control tracking on our site.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">10. Children's Privacy</h3>
                    <p style="margin-bottom: 2.5rem;">Our website is not directed at children under the age of 13 and we do not knowingly collect data from children through cookies or any other means. If you believe a child has provided personal data through our website, please contact us at info@rayvotech.com and we will take immediate steps to address it.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">11. Changes to This Cookie Policy</h3>
                    <p style="margin-bottom: 1.5rem;">We may update this Cookie Policy from time to time to reflect changes in technology, legislation, or our business practices. When we do, we will update the date at the top of this page. We encourage you to review this policy periodically to stay informed about how we use cookies.</p>
                    <p style="margin-bottom: 2.5rem;">Your continued use of our website following any updates constitutes your acceptance of the revised Cookie Policy.</p>

                    <h3 style="color: var(--text-primary); font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem;">12. Contact Us</h3>
                    <p style="margin-bottom: 0.5rem;">If you have any questions or concerns about our use of cookies or this Cookie Policy, please contact us:</p>
                    <p style="margin-bottom: 0.5rem;"><strong>Rayvotech</strong></p>
                    <p style="margin-bottom: 0.5rem;">9029 Burt St, Omaha, Nebraska 68114, USA</p>
                    <p style="margin-bottom: 0;">📧 info@rayvotech.com</p>
                    <p style="margin-top: 1.5rem; font-style: italic;">We are happy to address any concerns and will respond to all inquiries within 5 business days.</p>
                    
                </div>
            </div>
        </div>
    </section>
    
    """
    
    updated_content = content[:start_idx] + new_content + content[end_idx:]
    updated_content = updated_content.replace('October 2026', 'March 2026')
    updated_content = updated_content.replace('Cookie Policy —</title>', 'Cookie Policy | Rayvotech</title>')
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("cookies.html successfully updated with exact copy!")
else:
    print("Could not find the section boundaries in cookies.html.")
