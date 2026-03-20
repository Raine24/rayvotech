import re

css_file = 'style.css'

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Strip out the previous awwwards-process block if it exists
content = re.sub(r'/\* ==========================================================================\n   Awwwards Process Grid\n   ========================================================================== \*/.*', '', content, flags=re.DOTALL)

split_css = """
/* ==========================================================================
   Split Timeline Approach
   ========================================================================== */
.split-process {
    padding: 8rem 0;
    position: relative;
    z-index: 10;
}
.split-container {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 6rem;
    align-items: flex-start;
}
.process-visual-col {
    position: sticky;
    top: 8rem; /* Sticks below navbar */
}
.process-shaped-frame {
    position: relative;
    width: 100%;
    aspect-ratio: 4 / 5;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.1);
}
.process-shaped-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.8) contrast(1.1);
    transition: transform 0.5s ease;
}
.process-shaped-frame:hover img {
    transform: scale(1.05);
}
.frame-glass-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 50%, rgba(0, 230, 240, 0.1) 100%);
    pointer-events: none;
}
.frame-border-glow {
    position: absolute;
    inset: 0;
    border-radius: 24px;
    box-shadow: inset 0 0 40px rgba(0,0,0,0.8);
    pointer-events: none;
}

/* Timeline Column */
.process-timeline-col {
    position: relative;
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.vertical-connector-track {
    position: absolute;
    left: 17px;
    top: 2rem;
    bottom: 4rem;
    width: 2px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 2px;
}
.vertical-connector-fill {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 30%; /* Could be animated with JS on scroll */
    background: var(--color-accent);
    box-shadow: 0 0 10px var(--color-accent);
}

.v-step-item {
    position: relative;
    padding-left: 4.5rem;
    margin-bottom: 5rem;
}
.v-step-item:last-child {
    margin-bottom: 0;
}
.v-step-node {
    position: absolute;
    left: 0;
    top: 6px;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--color-surface);
    border: 2px solid rgba(255,255,255,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.4s ease;
    z-index: 2;
}
.v-step-item:hover .v-step-node {
    border-color: var(--color-accent);
    background: rgba(0,230,240,0.1);
    box-shadow: 0 0 20px rgba(0, 230, 240, 0.4);
    transform: scale(1.1);
}
.v-step-node::after {
    content: '';
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: var(--color-accent);
    opacity: 0;
    transition: opacity 0.4s ease;
}
.v-step-item:hover .v-step-node::after {
    opacity: 1;
}

.v-step-title {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    color: var(--text-primary);
    transition: color 0.3s ease;
}
.v-step-num {
    font-family: var(--font-mono);
    font-size: 1.1rem;
    font-weight: 400;
    color: var(--color-accent);
}
.v-step-content p {
    font-size: 1.2rem;
    line-height: 1.8;
    color: var(--text-secondary);
    max-width: 90%;
}

@media (max-width: 1024px) {
    .split-container { grid-template-columns: 1fr; gap: 4rem; }
    .process-visual-col { position: relative; top: 0; margin-bottom: 2rem; }
    .process-shaped-frame { aspect-ratio: 21/9; }
}
@media (max-width: 768px) {
    .v-step-title { font-size: 1.5rem; }
    .v-step-content p { font-size: 1.05rem; max-width: 100%; }
    .v-step-item { padding-left: 3.5rem; }
    .vertical-connector-track { left: 17px; }
}
"""

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(content + "\n" + split_css)

print("Split process CSS successfully applied.")
