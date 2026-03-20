import os
import glob

tawk_script = """
    <!--Start of Tawk.to Script-->
    <script type="text/javascript">
    var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
    (function(){
    var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
    s1.async=true;
    s1.src='https://embed.tawk.to/6938a8d72e7053198ac976f7/1jc2l73cp';
    s1.charset='UTF-8';
    s1.setAttribute('crossorigin','*');
    s0.parentNode.insertBefore(s1,s0);
    })();
    </script>
    <!--End of Tawk.to Script-->"""

html_files = glob.glob('*.html')
updated = 0
skipped = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already injected
    if 'tawk.to' in content:
        print(f"Skipped (already present): {filepath}")
        skipped += 1
        continue

    # Inject before </body>
    if '</body>' in content:
        new_content = content.replace('</body>', tawk_script + '\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected: {filepath}")
        updated += 1
    else:
        print(f"WARNING - no </body> tag found in: {filepath}")

print(f"\nDone! Updated: {updated}, Skipped: {skipped}")
