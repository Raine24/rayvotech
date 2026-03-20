import os
import re

html_path = r"c:\Users\Baker\Documents\RAYVOTECH DIGITAL\temp-app\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the old title and subtitle first because git checkout reverted them
html = html.replace('We Build Brands <br> That <span class="text-gradient liquid-text">Stand Out.</span>', 'Built to Elevate. <br> Designed to <span class="text-gradient liquid-text">Convert.</span>')
html = html.replace('Fluid creativity meets raw technical power. We engineer digital experiences that dominate the modern web landscape.', 'We design, build, and grow digital experiences that attract the right audience <br> and turn them into paying customers.')

# Now replace the hero content structure
# We want to match from <div class="container hero-content"> down to just before <!-- Hero Stats & Tech Stack -->
# and wrap the top part in a flex container

old_hero_top = """        <div class="container hero-content">
            <div class="y2k-badge reveal-text">[YOUR GROWTH PARTNER]</div>
            <h1 class="hero-title reveal-text delay-1">Built to Elevate. <br> Designed to <span class="text-gradient liquid-text">Convert.</span></h1>
            <p class="hero-subtitle reveal-text delay-2">We design, build, and grow digital experiences that attract the right audience <br> and turn them into paying customers.</p>
            <div class="hero-actions reveal-text delay-3">
                <a href="#work" class="btn btn-primary btn-lg">View Our Work <i class="ph ph-arrow-down-right"></i></a>
                <a href="#services" class="btn btn-outline btn-lg">Our Expertise</a>
            </div>

            <!-- Hero Stats & Tech Stack -->"""

new_hero_top = """        <div class="container hero-content">
            
            <style>
                .hero-top-split {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 3rem;
                    align-items: center;
                    margin-bottom: 3rem;
                }
                .hero-text-col {
                    text-align: left;
                }
                .hero-text-col .y2k-badge {
                    margin-left: 0;
                }
                .hero-text-col .hero-title {
                    text-align: left;
                }
                .hero-text-col .hero-subtitle {
                    text-align: left;
                    margin-left: 0;
                    margin-right: 0;
                    max-width: 600px;
                    font-size: clamp(0.95rem, 2vw, 1.1rem);
                    line-height: 1.6;
                }
                .hero-text-col .hero-actions {
                    justify-content: flex-start;
                }
                .hero-image-col img {
                    width: 100%;
                    height: auto;
                    display: block;
                    mix-blend-mode: normal;
                }
                @media(max-width: 900px) {
                    .hero-top-split {
                        grid-template-columns: 1fr;
                    }
                    .hero-text-col {
                        text-align: center;
                    }
                    .hero-text-col .y2k-badge {
                        margin-left: auto;
                        margin-right: auto;
                    }
                    .hero-text-col .hero-title {
                        text-align: center;
                    }
                    .hero-text-col .hero-subtitle {
                        text-align: center;
                        margin-left: auto;
                        margin-right: auto;
                    }
                    .hero-text-col .hero-actions {
                        justify-content: center;
                    }
                }
            </style>

            <div class="hero-top-split">
                <div class="hero-text-col" style="z-index: 2; position: relative;">
                    <div class="y2k-badge reveal-text">[YOUR GROWTH PARTNER]</div>
                    <h1 class="hero-title reveal-text delay-1">Built to Elevate. <br> Designed to <span class="text-gradient liquid-text">Convert.</span></h1>
                    <p class="hero-subtitle reveal-text delay-2">We design, build, and grow digital experiences that attract the right audience <br> and turn them into paying customers.</p>
                    <div class="hero-actions reveal-text delay-3">
                        <a href="#work" class="btn btn-primary btn-lg">View Our Work <i class="ph ph-arrow-down-right"></i></a>
                        <a href="#services" class="btn btn-outline btn-lg">Our Expertise</a>
                    </div>
                </div>

                <div class="hero-image-col reveal-text delay-3" style="position: relative; z-index: 2;">
                    <!-- Blob Image -->
                    <img src="https://i.imgur.com/ua0e7Kj.png" alt="Digital Growth Experience" style="filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));">
                </div>
            </div>

            <!-- Hero Stats & Tech Stack -->"""

if old_hero_top in html:
    html = html.replace(old_hero_top, new_hero_top)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Patched hero section successfully!")
else:
    print("Could not find the exact old hero top string. Please check manual diffs.")
