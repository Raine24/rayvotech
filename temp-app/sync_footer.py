import re

# Read the latest index.html to extract the master footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# The footer starts with <footer class="footer" and ends with </footer>
match = re.search(r'<footer class="footer" id="contact">.*?</footer>', index_content, re.DOTALL)
if not match:
    # Maybe id="contact" isn't present, try generic
    match = re.search(r'<footer class="footer".*?</footer>', index_content, re.DOTALL)

if match:
    master_footer = match.group(0)
    
    # Read contact.html
    with open('contact.html', 'r', encoding='utf-8') as f:
        contact_content = f.read()
    
    # Replace the footer in contact.html
    # We find the existing footer in contact.html
    contact_footer_match = re.search(r'<footer class="footer">.*?</footer>', contact_content, re.DOTALL)
    
    if contact_footer_match:
        # We need to strip out the massive CTA section from the contact page footer
        # because the contact page IS the CTA page
        # We'll parse the master_footer to remove the massive-cta div just for contact.html
        cta_pattern = re.compile(r'<div class="massive-cta fade-up">.*?</div>\s*<style>', re.DOTALL)
        clean_contact_footer = cta_pattern.sub('<style>', master_footer)
        
        new_contact_content = contact_content[:contact_footer_match.start()] + clean_contact_footer + contact_content[contact_footer_match.end():]
        
        with open('contact.html', 'w', encoding='utf-8') as f:
            f.write(new_contact_content)
            
        print("Successfully synced footer to contact.html (and removed the redundant CTA module from it).")
    else:
        print("Could not find footer in contact.html")
else:
    print("Could not extract footer from index.html")
