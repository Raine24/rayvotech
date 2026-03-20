import glob

target = '<span style="display: flex; align-items: center; gap: 0.5rem;"><i class="ph-fill ph-check-circle" style="color: var(--color-accent);"></i> Secure & Operational</span>'

replacement = """<div class="payment-methods" style="display: flex; gap: 1rem; align-items: center; color: var(--text-secondary); opacity: 0.8;">
                    <i class="ph ph-stripe-logo" style="font-size: 1.8rem;" title="Stripe"></i>
                    <i class="ph ph-paypal-logo" style="font-size: 1.8rem;" title="PayPal"></i>
                    <i class="ph ph-google-logo" style="font-size: 1.5rem;" title="Google Pay"></i>
                    <i class="ph ph-apple-logo" style="font-size: 1.5rem;" title="Apple Pay"></i>
                    <i class="ph ph-credit-card" style="font-size: 1.8rem;" title="Credit Card"></i>
                </div>"""

updated_files = 0

for filepath in glob.glob('*.html'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if target in content:
            new_content = content.replace(target, replacement)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files += 1
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

print(f"\nDone! Successfully updated {updated_files} files.")
