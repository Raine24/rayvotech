import glob
import re

html_files = ['terms.html', 'privacy.html', 'cookies.html', 'disclaimer.html']

missing_elements = """
    <!-- Global Page Aurora -->
    <div class="page-aurora" aria-hidden="true">
        <div class="page-aurora-blob pa-1"></div>
        <div class="page-aurora-blob pa-2"></div>
        <div class="page-aurora-blob pa-3"></div>
    </div>

    <!-- Initial Pro Loader -->
    <div id="initial-loader">
        <div class="pro-spinner">
            <div class="pro-spinner-inner"></div>
        </div>
        <div class="loader-progress-bar"></div>
    </div>

    <!-- Reading Progress Indicator -->
    <div class="reading-progress-container">
        <div class="reading-progress-bar" id="reading-progress"></div>
    </div>

    <!-- Custom Cursor -->
    <div class="cursor-dot" data-cursor-dot></div>
    <div class="cursor-outline" data-cursor-outline></div>
"""

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already injected
        if 'id="initial-loader"' not in content:
            # Inject right after <body class="theme-aurora">
            new_content = content.replace('<body class="theme-aurora">', '<body class="theme-aurora">\n' + missing_elements)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed missing structural elements in {filepath}")
        else:
            print(f"{filepath} already contains structural elements.")
    except Exception as e:
        print(f"Failed processing {filepath}: {e}")
