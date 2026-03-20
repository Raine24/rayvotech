import re

html_file = 'service-website-design.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# The block starts with "<!-- Pricing Table -->" and ends before "<!-- Why Us / CTA -->"
pattern = r'<!-- Pricing Table -->.*?<!-- Why Us / CTA -->'
new_content = re.sub(pattern, '<!-- Why Us / CTA -->', content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Pricing table removed successfully.")
