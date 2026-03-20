import re

css_file = 'style.css'

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace old process styling with new Awwards grid
new_css = """
/* ==========================================================================
   Awwwards Process Grid
   ========================================================================== */
.awwwards-process {
    padding: 8rem 0;
    overflow: hidden;
}
.awwwards-process-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
    position: relative;
    z-index: 10;
}
.process-card {
    position: relative;
    padding: 3rem;
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    overflow: hidden;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background 0.4s ease, border-color 0.4s ease;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    min-height: 380px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    backdrop-filter: blur(10px);
}
.process-card.span-2 {
    grid-column: span 2;
}
.process-card:hover {
    transform: translateY(-8px);
    background: rgba(255, 255, 255, 0.04);
    border-color: rgba(0, 230, 240, 0.2);
}
.p-card-bg-number {
    position: absolute;
    bottom: -15%;
    right: -5%;
    font-size: 18rem;
    font-family: var(--font-heading);
    font-weight: 800;
    color: transparent;
    -webkit-text-stroke: 1px rgba(255, 255, 255, 0.04);
    line-height: 1;
    z-index: 0;
    pointer-events: none;
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}
.process-card:hover .p-card-bg-number {
    -webkit-text-stroke: 1px rgba(0, 230, 240, 0.15);
    transform: scale(1.05) translate(-15px, -15px);
}
.p-card-content {
    position: relative;
    z-index: 1;
}
.p-card-header {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 1.5rem;
    margin-bottom: 2rem;
}
.p-icon-box {
    width: 65px;
    height: 65px;
    border-radius: 16px;
    background: rgba(0, 230, 240, 0.1);
    color: var(--color-accent);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    border: 1px solid rgba(0, 230, 240, 0.2);
}
.p-card-header h3 {
    font-size: 2rem;
    margin: 0;
    font-weight: 700;
}
.p-card-content p {
    color: var(--text-secondary);
    font-size: 1.15rem;
    line-height: 1.7;
    max-width: 90%;
}

@media (max-width: 1024px) {
    .awwwards-process-grid { grid-template-columns: 1fr; }
    .process-card.span-2 { grid-column: span 1; }
    .process-card { min-height: 300px; padding: 2.5rem; }
}
@media (max-width: 768px) {
    .p-card-bg-number { font-size: 12rem; right: -10%; bottom: -5%; }
    .process-card { padding: 2rem; }
    .p-card-header h3 { font-size: 1.5rem; }
    .p-card-content p { font-size: 1rem; max-width: 100%; }
}
"""

with open(css_file, 'a', encoding='utf-8') as f:
    f.write(new_css)
print("CSS appended.")
