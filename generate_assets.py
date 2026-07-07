import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(BASE_DIR, "assets", "svg")
os.makedirs(SVG_DIR, exist_ok=True)

# Helper for generic SVG defs
DEFS = """
<defs>
    <style>
        text {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        }
        .hero-title { font-weight: 700; font-size: 42px; fill: #ffffff; letter-spacing: -1px; }
        .hero-role { font-weight: 500; font-size: 18px; fill: #8b949e; letter-spacing: -0.2px; }
        .hero-mission { font-weight: 400; font-size: 15px; fill: #6e7681; }
        
        .cursor { font-weight: 700; fill: #58a6ff; animation: blink 1s step-end infinite; }
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
        
        .shimmer {
            animation: shimmer 8s infinite linear;
        }
        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
    </style>

    <linearGradient id="shimmerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="rgba(255,255,255,0)" />
        <stop offset="50%" stop-color="rgba(255,255,255,0.05)" />
        <stop offset="100%" stop-color="rgba(255,255,255,0)" />
    </linearGradient>

    <linearGradient id="dividerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="rgba(88, 166, 255, 0)" />
        <stop offset="50%" stop-color="rgba(163, 113, 247, 0.4)" />
        <stop offset="100%" stop-color="rgba(57, 197, 207, 0)" />
    </linearGradient>
</defs>
"""

def generate_hero():
    svg = f"""<svg width="800" height="200" viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
    {DEFS}
    <rect width="100%" height="100%" fill="transparent" />
    
    <!-- Subtle particle drift background -->
    <g opacity="0.4">
        <circle cx="100" cy="50" r="1" fill="#58a6ff"><animate attributeName="cy" values="50;40;50" dur="10s" repeatCount="indefinite"/></circle>
        <circle cx="700" cy="150" r="1.5" fill="#a371f7"><animate attributeName="cy" values="150;160;150" dur="12s" repeatCount="indefinite"/></circle>
        <circle cx="400" cy="180" r="1" fill="#39c5cf"><animate attributeName="cx" values="400;410;400" dur="15s" repeatCount="indefinite"/></circle>
        <circle cx="250" cy="120" r="2" fill="#58a6ff" opacity="0.2"><animate attributeName="r" values="2;3;2" dur="8s" repeatCount="indefinite"/></circle>
        <circle cx="650" cy="40" r="1" fill="#8b949e"><animate attributeName="opacity" values="0.1;0.5;0.1" dur="5s" repeatCount="indefinite"/></circle>
    </g>

    <!-- Content -->
    <g transform="translate(400, 85)" text-anchor="middle">
        <text class="hero-title" y="0">Adarsh Binu</text>
        <text class="hero-role" y="32">Software Engineer <tspan fill="#30363d">|</tspan> AI &amp; Distributed Systems</text>
        <text class="hero-mission" y="60">Building robust platforms instead of tutorial projects <tspan class="cursor">_</tspan></text>
    </g>

    <!-- Very subtle shimmer overlay on top text -->
    <rect x="0" y="0" width="800" height="200" fill="url(#shimmerGrad)" style="pointer-events: none;" class="shimmer"/>
</svg>"""
    with open(os.path.join(SVG_DIR, "hero.svg"), "w") as f:
        f.write(svg)

def generate_divider():
    svg = f"""<svg width="800" height="2" viewBox="0 0 800 2" xmlns="http://www.w3.org/2000/svg">
    {DEFS}
    <!-- Moving glowing segment -->
    <rect x="-200" y="0" width="400" height="1" fill="url(#dividerGrad)">
        <animate attributeName="x" values="-400;800" dur="6s" repeatCount="indefinite" />
    </rect>
</svg>"""
    with open(os.path.join(SVG_DIR, "divider.svg"), "w") as f:
        f.write(svg)

def generate_project_logo(filename, accent_color, geometric_svg):
    svg = f"""<svg width="64" height="64" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
    <rect width="64" height="64" rx="12" fill="rgba(13, 17, 23, 0.8)" stroke="{accent_color}" stroke-opacity="0.2" stroke-width="1" />
    <g transform="translate(32, 32)">
        {geometric_svg}
    </g>
</svg>"""
    with open(os.path.join(SVG_DIR, filename), "w") as f:
        f.write(svg)

def generate_logos():
    # NullTrace - Purple Triangle
    generate_project_logo(
        "nulltrace-logo.svg", "#a371f7",
        '''
        <path d="M-8,5 L8,13 L0,-12 Z" fill="none" stroke="#a371f7" stroke-width="1.5">
            <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="30s" repeatCount="indefinite"/>
        </path>
        <circle cx="0" cy="0" r="2" fill="#a371f7" />
        '''
    )

    # BuildBridge - Blue Square Matrix
    generate_project_logo(
        "buildbridge-logo.svg", "#58a6ff",
        '''
        <rect x="-8" y="-8" width="16" height="16" fill="none" stroke="#58a6ff" stroke-width="1.5" rx="2">
            <animateTransform attributeName="transform" type="rotate" values="0;90;90;180;180" dur="10s" repeatCount="indefinite" />
        </rect>
        <circle cx="0" cy="0" r="1.5" fill="#58a6ff" />
        '''
    )

    # ReconX - Cyan Orbit
    generate_project_logo(
        "reconx-logo.svg", "#39c5cf",
        '''
        <circle cx="0" cy="0" r="10" fill="none" stroke="#39c5cf" stroke-width="1.5" stroke-dasharray="3 3">
            <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="20s" repeatCount="indefinite"/>
        </circle>
        <circle cx="0" cy="0" r="3" fill="#39c5cf" />
        '''
    )

    # Agentic Marketing - Orange/Red Polygon
    generate_project_logo(
        "agentic-logo.svg", "#f0883e",
        '''
        <polygon points="0,-10 9,6 -9,6" fill="none" stroke="#f0883e" stroke-width="1.5">
            <animateTransform attributeName="transform" type="scale" values="1;1.1;1" dur="6s" repeatCount="indefinite" />
        </polygon>
        '''
    )

def write_readme():
    content = """<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/svg/hero.svg">
    <img src="./assets/svg/hero.svg" alt="Adarsh Binu - Software Engineer" width="100%">
  </picture>
</div>

<div align="center">
  <img src="./assets/svg/divider.svg" width="100%" alt="divider">
</div>

## ✦ Current Focus

Currently architecting the MVP for **BuildBridge**, a scalable workforce infrastructure platform, while exploring **Agentic AI workflows** and **Distributed Systems**. I enjoy designing robust, production-ready systems that solve real engineering problems rather than following textbook tutorials.

<div align="center">
  <img src="./assets/svg/divider.svg" width="100%" alt="divider">
</div>

## ✦ Featured Projects

<a href="https://github.com/marvelpokemaster/NullTrace">
  <img src="./assets/svg/nulltrace-logo.svg" align="left" width="64" height="64" alt="NullTrace Logo" style="margin-right: 15px;">
</a>
<h3><a href="https://github.com/marvelpokemaster/NullTrace" style="text-decoration: none; color: inherit;">NullTrace</a></h3>
<p>AI-powered Opinion & Feedback Analytics Platform. Engineered with JWT authentication, role-based access control, and granular feedback analytics within a containerized Azure deployment.</p>
<p><code>Flask</code> • <code>Next.js</code> • <code>PostgreSQL</code> • <code>Docker</code> • <code>Azure</code></p>
<br clear="left"/>

<a href="https://github.com/marvelpokemaster/BuildBridge">
  <img src="./assets/svg/buildbridge-logo.svg" align="left" width="64" height="64" alt="BuildBridge Logo" style="margin-right: 15px;">
</a>
<h3><a href="https://github.com/marvelpokemaster/BuildBridge" style="text-decoration: none; color: inherit;">BuildBridge</a></h3>
<p>Workforce Infrastructure Platform connecting contractors and workers seamlessly. Architected as a high-performance startup MVP with robust authentication and state management.</p>
<p><code>React</code> • <code>Node.js</code> • <code>Supabase</code> • <code>Vercel</code></p>
<br clear="left"/>

<a href="https://github.com/marvelpokemaster/ReconX">
  <img src="./assets/svg/reconx-logo.svg" align="left" width="64" height="64" alt="ReconX Logo" style="margin-right: 15px;">
</a>
<h3><a href="https://github.com/marvelpokemaster/ReconX" style="text-decoration: none; color: inherit;">ReconX</a></h3>
<p>OSINT & Internet Asset Intelligence Platform providing domain intelligence, DNS record enumeration, certificate discovery, and comprehensive infrastructure mapping.</p>
<p><code>Python</code> • <code>FastAPI</code> • <code>React</code></p>
<br clear="left"/>

<a href="https://github.com/marvelpokemaster/Agentic-Marketing">
  <img src="./assets/svg/agentic-logo.svg" align="left" width="64" height="64" alt="Agentic Marketing Logo" style="margin-right: 15px;">
</a>
<h3><a href="https://github.com/marvelpokemaster/Agentic-Marketing" style="text-decoration: none; color: inherit;">Agentic Marketing</a></h3>
<p>AI-powered Marketing Automation utilizing autonomous lead discovery, orchestrated LLM workflows, and intelligent campaign execution.</p>
<p><code>Gemini API</code> • <code>PyTorch</code> • <code>Transformers</code></p>
<br clear="left"/>

<div align="center">
  <img src="./assets/svg/divider.svg" width="100%" alt="divider">
</div>

## ✦ Technical Arsenal

- **Languages:** Python, TypeScript, JavaScript, Java, C, SQL
- **Frontend:** React, Next.js, TailwindCSS
- **Backend & Database:** Node.js, Flask, FastAPI, PostgreSQL, Supabase
- **Infrastructure & DevOps:** Docker, Azure, Vercel, Linux, Git
- **AI & ML:** PyTorch, Transformers, Gemini API

<div align="center">
  <img src="./assets/svg/divider.svg" width="100%" alt="divider">
</div>

## ✦ GitHub Telemetry

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=marvelpokemaster&show_icons=true&theme=transparent&title_color=ffffff&text_color=8b949e&icon_color=58a6ff&bg_color=0d1117&hide_border=true&hide_title=true">
    <img src="https://github-readme-stats.vercel.app/api?username=marvelpokemaster&show_icons=true&theme=transparent" alt="GitHub Stats">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=marvelpokemaster&layout=compact&theme=transparent&title_color=ffffff&text_color=8b949e&icon_color=a371f7&bg_color=0d1117&hide_border=true&hide_title=true">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=marvelpokemaster&layout=compact&theme=transparent" alt="Top Languages">
  </picture>
</div>

<div align="center">
  <img src="./assets/svg/divider.svg" width="100%" alt="divider">
</div>

## ✦ Engineering Philosophy

Code is a liability; architecture is an asset. I strive to design systems that are minimal, scalable, and inherently resilient. Rather than piecing together quick fixes, I deeply value rigorous engineering standards and well-considered system design, ensuring that what I build today remains maintainable tomorrow.

<br/>

<div align="center">
  <a href="mailto:adarsh.binu@outlook.com"><code>Contact</code></a> &nbsp; • &nbsp;
  <a href="https://linkedin.com/in/adarshbinu"><code>LinkedIn</code></a> &nbsp; • &nbsp;
  <a href="https://github.com/marvelpokemaster"><code>GitHub</code></a>
</div>
"""
    with open(os.path.join(BASE_DIR, "README.md"), "w") as f:
        f.write(content)

if __name__ == "__main__":
    generate_hero()
    generate_divider()
    generate_logos()
    write_readme()
    print("Assets successfully generated.")
