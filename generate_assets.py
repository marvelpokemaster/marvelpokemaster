import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(BASE_DIR, "assets", "svg")
os.makedirs(SVG_DIR, exist_ok=True)

def generate_hero():
    svg = """<svg width="800" height="260" viewBox="0 0 800 260" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&amp;family=Outfit:wght@400;600;800&amp;display=swap');
            text {
                font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            }
            .mono {
                font-family: 'Fira Code', monospace;
            }
            .hero-title { font-weight: 800; font-size: 42px; fill: #ffffff; letter-spacing: -1px; }
            .hero-role { font-weight: 600; font-size: 13px; fill: #8b949e; letter-spacing: 4px; }
            .hero-tag { font-family: 'Fira Code', monospace; font-size: 11px; fill: #a371f7; }
            
            @keyframes pulse {
                0%, 100% { opacity: 0.1; }
                50% { opacity: 0.35; }
            }
            .grid-bg {
                animation: pulse 8s ease-in-out infinite;
            }
            @keyframes rotate-clockwise {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
            @keyframes rotate-counter {
                from { transform: rotate(0deg); }
                to { transform: rotate(-360deg); }
            }
            .spin-cw {
                transform-origin: 130px 130px;
                animation: rotate-clockwise 20s linear infinite;
            }
            .spin-ccw {
                transform-origin: 130px 130px;
                animation: rotate-counter 15s linear infinite;
            }
        </style>
        
        <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
            <path d="M 30 0 L 0 0 0 30" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="1"/>
        </pattern>
        
        <radialGradient id="glow-core" cx="130px" cy="130px" r="100px" gradientUnits="userSpaceOnUse">
            <stop offset="0%" stop-color="rgba(163, 113, 247, 0.25)"/>
            <stop offset="100%" stop-color="rgba(0,0,0,0)"/>
        </radialGradient>
        <radialGradient id="glow-right" cx="600px" cy="130px" r="200px" gradientUnits="userSpaceOnUse">
            <stop offset="0%" stop-color="rgba(88, 166, 255, 0.15)"/>
            <stop offset="100%" stop-color="rgba(0,0,0,0)"/>
        </radialGradient>
    </defs>
    
    <!-- Base Background -->
    <rect width="100%" height="100%" fill="#0a0a0f" rx="16" />
    <rect width="100%" height="100%" fill="url(#grid)" class="grid-bg" rx="16" />
    
    <!-- Glow Effects -->
    <rect width="100%" height="100%" fill="url(#glow-core)" rx="16" />
    <rect width="100%" height="100%" fill="url(#glow-right)" rx="16" />
    
    <!-- Cybernetic Core (Left) -->
    <!-- Outer dashed ring -->
    <circle cx="130" cy="130" r="75" fill="none" stroke="#30363d" stroke-width="1" />
    <circle cx="130" cy="130" r="75" fill="none" stroke="#58a6ff" stroke-width="1.5" stroke-dasharray="15 35" class="spin-cw" />
    
    <!-- Middle detailed ring -->
    <circle cx="130" cy="130" r="55" fill="none" stroke="rgba(163, 113, 247, 0.2)" stroke-width="3" />
    <circle cx="130" cy="130" r="55" fill="none" stroke="#a371f7" stroke-width="1.5" stroke-dasharray="40 15 10 15" class="spin-ccw" />
    
    <!-- Core Hub -->
    <g transform="translate(130, 130)">
        <polygon points="0,-18 16,-9 16,9 0,18 -16,9 -16,-9" fill="#0a0a0f" stroke="#39c5cf" stroke-width="2">
            <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite"/>
        </polygon>
        <circle cx="0" cy="0" r="4" fill="#39c5cf">
            <animate attributeName="opacity" values="0.3;1;0.3" dur="2s" repeatCount="indefinite"/>
        </circle>
    </g>
    
    <!-- Constellation Lines linking Core to Right Side -->
    <path d="M 205 130 L 245 130" stroke="#30363d" stroke-width="1" stroke-dasharray="2 2" />
    <circle cx="205" cy="130" r="2" fill="#58a6ff" />
    <circle cx="245" cy="130" r="2" fill="#a371f7" />
    
    <!-- Title & Role Info (Right) -->
    <g transform="translate(260, 85)">
        <text class="mono hero-tag" y="0">&lt;SYSTEMS_ARCHITECT&gt;</text>
        <text class="hero-title" y="42">ADARSH BINU</text>
        <text class="hero-role" y="68">DISTRIBUTED SYSTEMS &amp; AGENTIC WORKFLOWS</text>
    </g>
    
    <!-- Live Console Output Box -->
    <g transform="translate(260, 175)">
        <!-- Box Outline -->
        <rect width="500" height="55" rx="8" fill="rgba(22, 27, 34, 0.6)" stroke="#30363d" stroke-width="1" />
        <path d="M 0 10 L 0 0 L 10 0" stroke="#a371f7" stroke-width="2" fill="none" />
        <path d="M 500 45 L 500 55 L 490 55" stroke="#a371f7" stroke-width="2" fill="none" />
        
        <!-- Blinking Online Light -->
        <circle cx="25" cy="28" r="4" fill="#39c5cf">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
        </circle>
        <circle cx="25" cy="28" r="8" fill="none" stroke="#39c5cf" stroke-width="1" opacity="0.5">
            <animate attributeName="r" values="4;10;4" dur="2s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.8;0;0.8" dur="2s" repeatCount="indefinite"/>
        </circle>
        
        <text class="mono" x="45" y="32" font-size="11" fill="#c9d1d9">
            <tspan fill="#8b949e">SYSTEM_STATUS:</tspan> ONLINE
            <tspan fill="#8b949e" dx="20">COGNITION_LOAD:</tspan> OPTIMAL
            <tspan fill="#8b949e" dx="20">LOC:</tspan> BLR, IN
        </text>
    </g>
</svg>"""
    with open(os.path.join(SVG_DIR, "hero.svg"), "w") as f:
        f.write(svg)

def generate_divider():
    svg = """<svg width="800" height="24" viewBox="0 0 800 24" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="rgba(48, 54, 61, 0)" />
            <stop offset="15%" stop-color="rgba(48, 54, 61, 1)" />
            <stop offset="50%" stop-color="rgba(163, 113, 247, 0.8)" />
            <stop offset="85%" stop-color="rgba(48, 54, 61, 1)" />
            <stop offset="100%" stop-color="rgba(48, 54, 61, 0)" />
        </linearGradient>
        <radialGradient id="glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#a371f7" stop-opacity="0.4" />
            <stop offset="100%" stop-color="#a371f7" stop-opacity="0" />
        </radialGradient>
    </defs>
    <!-- Glow under the center hexagon -->
    <circle cx="400" cy="12" r="16" fill="url(#glow)">
        <animate attributeName="r" values="8;18;8" dur="3s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.2;0.6;0.2" dur="3s" repeatCount="indefinite" />
    </circle>
    <!-- Center Hexagon -->
    <g transform="translate(400, 12)">
        <polygon points="0,-7 6,-3.5 6,3.5 0,7 -6,3.5 -6,-3.5" fill="#0a0a0f" stroke="#a371f7" stroke-width="1.5">
            <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="10s" repeatCount="indefinite" />
        </polygon>
        <circle cx="0" cy="0" r="2" fill="#39c5cf" />
    </g>
    <!-- Left & Right Lines -->
    <path d="M 50 12 L 380 12" stroke="url(#lineGrad)" stroke-width="1.5" />
    <path d="M 420 12 L 750 12" stroke="url(#lineGrad)" stroke-width="1.5" />
</svg>"""
    with open(os.path.join(SVG_DIR, "divider.svg"), "w") as f:
        f.write(svg)

def generate_project_card(filename, title, subtitle, desc_lines, accent_color, tech_list, logo_svg):
    badge_x = 0
    badge_html = ""
    for tech in tech_list:
        text_w = len(tech) * 6 + 14
        badge_html += f"""
        <g transform="translate({badge_x}, 0)">
            <rect width="{text_w}" height="22" rx="6" fill="#161b22" stroke="#30363d" stroke-width="1"/>
            <text x="{text_w/2}" y="15" font-family="'Outfit', -apple-system, BlinkMacSystemFont, sans-serif" font-weight="600" font-size="10.5" fill="#c9d1d9" text-anchor="middle">{tech}</text>
        </g>
        """
        badge_x += text_w + 6

    desc_html = ""
    y_offset = 0
    for line in desc_lines:
        desc_html += f'<tspan x="0" y="{y_offset}">{line}</tspan>'
        y_offset += 20

    svg = f"""<svg width="390" height="185" viewBox="0 0 390 185" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&amp;family=Outfit:wght@400;600;700&amp;display=swap');
            text {{
                font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
            }}
            .mono {{
                font-family: 'Fira Code', monospace;
            }}
            .card-border {{
                stroke: url(#border-grad-{title.replace(' ', '')});
                stroke-width: 1.5;
            }}
        </style>
        
        <linearGradient id="bg-{title.replace(' ', '')}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0a0a0f" />
            <stop offset="100%" stop-color="#161b22" />
        </linearGradient>
        
        <radialGradient id="glow-{title.replace(' ', '')}" cx="0%" cy="0%" r="60%">
            <stop offset="0%" stop-color="{accent_color}" stop-opacity="0.15" />
            <stop offset="100%" stop-color="rgba(0,0,0,0)" />
        </radialGradient>
        
        <linearGradient id="border-grad-{title.replace(' ', '')}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{accent_color}" />
            <stop offset="40%" stop-color="#30363d" />
            <stop offset="100%" stop-color="#161b22" />
        </linearGradient>
        
        <!-- Grid pattern inside cards -->
        <pattern id="card-dot-grid" width="14" height="14" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="0.6" fill="rgba(255,255,255,0.04)" />
        </pattern>
    </defs>
    
    <!-- Card Frame -->
    <rect width="390" height="185" rx="12" fill="url(#bg-{title.replace(' ', '')})" class="card-border" />
    <rect width="390" height="185" rx="12" fill="url(#card-dot-grid)" />
    <rect width="390" height="185" rx="12" fill="url(#glow-{title.replace(' ', '')})" style="pointer-events: none;" />
    
    <!-- Rotating Logo container -->
    <g transform="translate(42, 42)">
        <rect x="-24" y="-24" width="48" height="48" rx="10" fill="#0d1117" stroke="#30363d" stroke-width="1" />
        <g>
            {logo_svg}
        </g>
    </g>
    
    <!-- Pulse Indicator -->
    <circle cx="360" cy="30" r="3" fill="{accent_color}">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="360" cy="30" r="6" fill="none" stroke="{accent_color}" stroke-width="1">
        <animate attributeName="r" values="3;10;3" dur="3s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="1;0;1" dur="3s" repeatCount="indefinite"/>
    </circle>
    
    <!-- Headers -->
    <g transform="translate(80, 36)">
        <text font-weight="700" font-size="16" fill="#ffffff" letter-spacing="-0.3px">{title}</text>
        <text y="20" font-weight="500" font-size="11" fill="#8b949e">{subtitle}</text>
    </g>
    
    <!-- Description -->
    <g transform="translate(20, 88)">
      <text font-weight="400" font-size="12.5" fill="#c9d1d9" line-height="1.5">
        {desc_html}
      </text>
    </g>
    
    <!-- Badges -->
    <g transform="translate(20, 145)">
        {badge_html}
    </g>
</svg>"""
    with open(os.path.join(SVG_DIR, filename), "w") as f:
        f.write(svg)

def generate_tech_stack():
    categories = [
        {
            "title": "LANGUAGES",
            "techs": [
                ("Python", "#3776ab"),
                ("TypeScript", "#3178c6"),
                ("JavaScript", "#f7df1e"),
                ("Go Language", "#00add8"),
                ("Bash Shell", "#4eaa25")
            ]
        },
        {
            "title": "BACKEND & DATA",
            "techs": [
                ("Node.js", "#339933"),
                ("FastAPI", "#009688"),
                ("PostgreSQL", "#4169e1"),
                ("Supabase", "#3ecf8e"),
                ("REST / GraphQL", "#e10098")
            ]
        },
        {
            "title": "FRONTEND & INFRA",
            "techs": [
                ("React", "#61dafb"),
                ("Next.js", "#ffffff"),
                ("TailwindCSS", "#06b6d4"),
                ("Docker", "#2496ed"),
                ("Azure Cloud", "#0078d4")
            ]
        },
        {
            "title": "SYSTEMS & AI",
            "techs": [
                ("Distributed Sys", "#a371f7"),
                ("Agentic Workflows", "#f0883e"),
                ("OSINT Systems", "#39c5cf"),
                ("Git / GitHub", "#f05032"),
                ("Linux OS", "#f82c00")
            ]
        }
    ]
    
    svg = """<svg width="800" height="240" viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&amp;family=Outfit:wght@400;600;700&amp;display=swap');
            text {
                font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
            }
            .mono {
                font-family: 'Fira Code', monospace;
            }
            .cat-title { font-weight: 700; font-size: 11px; fill: #8b949e; letter-spacing: 2px; }
            .tech-text { font-weight: 600; font-size: 11.5px; fill: #c9d1d9; }
            .card-border { stroke: #30363d; stroke-width: 1.5; }
        </style>
        
        <linearGradient id="stackGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0a0a0f" />
            <stop offset="100%" stop-color="#161b22" />
        </linearGradient>
        
        <radialGradient id="stackGlow" cx="0%" cy="0%" r="60%">
            <stop offset="0%" stop-color="#a371f7" stop-opacity="0.1" />
            <stop offset="100%" stop-color="rgba(0,0,0,0)" />
        </radialGradient>
    </defs>
    
    <!-- Card Frame -->
    <rect width="800" height="240" rx="12" fill="url(#stackGrad)" class="card-border" />
    <rect width="800" height="240" rx="12" fill="url(#stackGlow)" style="pointer-events: none;" />
    
    <!-- Title and Subtitle -->
    <text x="25" y="32" font-weight="700" font-size="16" fill="#ffffff" letter-spacing="-0.3px">Technical Arsenal</text>
    <text x="775" y="32" class="mono" font-size="10" fill="#8b949e" text-anchor="end">[ STACK_PROVISIONED ]</text>
    <line x1="25" y1="42" x2="775" y2="42" stroke="#30363d" stroke-width="1" />
    """
    
    col_width = 172
    col_gap = 18
    x_offset = 25
    
    for col_idx, cat in enumerate(categories):
        col_x = x_offset + col_idx * (col_width + col_gap)
        svg += f"""
        <!-- Column {cat['title']} -->
        <g transform="translate({col_x}, 58)">
            <text class="mono cat-title" x="0" y="10">{cat['title']}</text>
        """
        
        y_offset = 24
        for tech_name, tech_color in cat['techs']:
            svg += f"""
            <!-- Tech Badge: {tech_name} -->
            <g transform="translate(0, {y_offset})">
                <rect width="{col_width}" height="28" rx="6" fill="#0d1117" stroke="#30363d" stroke-width="1" />
                <circle cx="12" cy="14" r="3.5" fill="{tech_color}" />
                <text class="tech-text" x="25" y="18">{tech_name}</text>
            </g>
            """
            y_offset += 33
            
        svg += "</g>\n"
        
    svg += "</svg>"
    with open(os.path.join(SVG_DIR, "tech_stack.svg"), "w") as f:
        f.write(svg)

def generate_status_widget():
    svg = """<svg width="390" height="185" viewBox="0 0 390 185" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&amp;family=Outfit:wght@400;600;700&amp;display=swap');
            text {
                font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
            }
            .mono {
                font-family: 'Fira Code', monospace;
            }
            .card-border { stroke: #30363d; stroke-width: 1.5; }
            
            @keyframes translate-wave1 {
                0% { transform: translate(0px, 0px); }
                100% { transform: translate(-80px, 0px); }
            }
            @keyframes translate-wave2 {
                0% { transform: translate(0px, 0px); }
                100% { transform: translate(-120px, 0px); }
            }
            .wave1 {
                animation: translate-wave1 3s linear infinite;
            }
            .wave2 {
                animation: translate-wave2 2s linear infinite;
            }
        </style>
        
        <linearGradient id="statusGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0a0a0f" />
            <stop offset="100%" stop-color="#161b22" />
        </linearGradient>
        
        <radialGradient id="statusGlow" cx="0%" cy="0%" r="60%">
            <stop offset="0%" stop-color="#39c5cf" stop-opacity="0.1" />
            <stop offset="100%" stop-color="rgba(0,0,0,0)" />
        </radialGradient>
        
        <clipPath id="oscilloscope-clip">
            <rect x="18" y="105" width="354" height="60" rx="6" />
        </clipPath>
        
        <!-- Grid pattern for oscilloscope background -->
        <pattern id="osc-grid" width="10" height="10" patternUnits="userSpaceOnUse">
            <path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="0.75"/>
        </pattern>
        
        <linearGradient id="border-grad-status" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#39c5cf" />
            <stop offset="40%" stop-color="#30363d" />
            <stop offset="100%" stop-color="#161b22" />
        </linearGradient>
    </defs>
    
    <!-- Card Frame -->
    <rect width="390" height="185" rx="12" fill="url(#statusGrad)" stroke="url(#border-grad-status)" stroke-width="1.5" />
    <rect width="390" height="185" rx="12" fill="url(#statusGlow)" style="pointer-events: none;" />
    
    <!-- Header -->
    <g transform="translate(18, 30)">
        <!-- Pulsing Active LED -->
        <circle cx="5" cy="0" r="3" fill="#3ecf8e">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" repeatCount="indefinite"/>
        </circle>
        <text x="18" y="4" class="mono" font-weight="700" font-size="11" fill="#ffffff">SYSTEM MONITOR v2.4</text>
        <text x="354" y="4" class="mono" font-size="9" fill="#8b949e" text-anchor="end">SYS_UPTIME: 99.98%</text>
    </g>
    
    <!-- Monitor Details -->
    <g transform="translate(18, 55)" class="mono" font-size="10" fill="#c9d1d9">
        <text x="0" y="0"><tspan fill="#8b949e">&gt;</tspan> FOCUS: <tspan fill="#58a6ff">Agentic AI Workflows</tspan></text>
        <text x="0" y="16"><tspan fill="#8b949e">&gt;</tspan> MVP: <tspan fill="#a371f7">BuildBridge matching engine</tspan></text>
        <text x="0" y="32"><tspan fill="#8b949e">&gt;</tspan> BANDWIDTH: <tspan fill="#39c5cf">88.4 Gb/s</tspan> <tspan fill="#8b949e" dx="15">CPU:</tspan> <tspan fill="#3ecf8e">12%</tspan></text>
    </g>
    
    <!-- Oscilloscope Display -->
    <!-- Background Frame -->
    <rect x="18" y="105" width="354" height="60" rx="6" fill="#07070a" stroke="#30363d" stroke-width="1" />
    <rect x="18" y="105" width="354" height="60" rx="6" fill="url(#osc-grid)" />
    
    <!-- Oscilloscope Sine Waves (Clipped) -->
    <g clip-path="url(#oscilloscope-clip)">
        <!-- Wave 1 (Cyan) -->
        <g class="wave1">
            <path d="M 0 135 Q 20 115, 40 135 T 80 135 T 120 135 T 160 135 T 200 135 T 240 135 T 280 135 T 320 135 T 360 135 T 400 135 T 440 135 T 480 135 T 520 135" fill="none" stroke="#39c5cf" stroke-width="1.5" opacity="0.8" />
        </g>
        
        <!-- Wave 2 (Purple - Phase Shifted and Slower) -->
        <g class="wave2" transform="translate(0, 5)">
            <path d="M 0 130 Q 30 110, 60 130 T 120 130 T 180 130 T 240 130 T 300 130 T 360 130 T 420 130 T 480 130 T 540 130 T 600 130" fill="none" stroke="#a371f7" stroke-width="1.2" opacity="0.6" />
        </g>
    </g>
    
    <!-- Overlay Glass Effect -->
    <rect x="18" y="105" width="354" height="60" rx="6" fill="rgba(255, 255, 255, 0.01)" style="pointer-events: none;" />
</svg>"""
    with open(os.path.join(SVG_DIR, "status_widget.svg"), "w") as f:
        f.write(svg)

def generate_cards():
    # NullTrace card
    nulltrace_logo = """
    <path d="M-6,4 L6,10 L0,-10 Z" fill="none" stroke="#a371f7" stroke-width="1.5">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="25s" repeatCount="indefinite"/>
    </path>
    <circle cx="0" cy="0" r="1.5" fill="#a371f7" />
    """
    generate_project_card(
        "nulltrace-card.svg",
        "NullTrace",
        "AI-Powered Feedback Analytics",
        [
            "An opinion & feedback analytics engine engineered with JWT auth,",
            "granular role-based access control, and real-time statistics.",
            "Deployed as containerized microservices on Azure infrastructure."
        ],
        "#a371f7",
        ["Flask", "Next.js", "PostgreSQL", "Docker", "Azure"],
        nulltrace_logo
    )

    # BuildBridge card
    buildbridge_logo = """
    <rect x="-7" y="-7" width="14" height="14" fill="none" stroke="#58a6ff" stroke-width="1.5" rx="1.5">
        <animateTransform attributeName="transform" type="rotate" values="0;90;90;180;180" dur="8s" repeatCount="indefinite" />
    </rect>
    <circle cx="0" cy="0" r="1.2" fill="#58a6ff" />
    """
    generate_project_card(
        "buildbridge-card.svg",
        "BuildBridge",
        "Workforce Infrastructure Platform",
        [
            "High-performance matching infrastructure connecting contractors",
            "with skilled labor. Developed as a secure startup MVP featuring",
            "real-time data synchronization and resilient session handling."
        ],
        "#58a6ff",
        ["React", "Node.js", "Supabase", "Vercel"],
        buildbridge_logo
    )

    # ReconX card
    reconx_logo = """
    <circle cx="0" cy="0" r="8" fill="none" stroke="#39c5cf" stroke-width="1.5" stroke-dasharray="3 2">
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="15s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="2.5" fill="#39c5cf" />
    """
    generate_project_card(
        "reconx-card.svg",
        "ReconX",
        "OSINT & Asset Intelligence",
        [
            "Advanced passive reconnaissance tool executing automated DNS",
            "enumeration, TLS certificate chain analysis, and attack surface",
            "footprinting with asynchronous API request orchestration."
        ],
        "#39c5cf",
        ["Python", "FastAPI", "React"],
        reconx_logo
    )

    # Agentic Marketing card
    agentic_logo = """
    <polygon points="0,-8 7,5 -7,5" fill="none" stroke="#f0883e" stroke-width="1.5">
        <animateTransform attributeName="transform" type="scale" values="1;1.15;1" dur="5s" repeatCount="indefinite" />
    </polygon>
    <circle cx="0" cy="1" r="1" fill="#f0883e" />
    """
    generate_project_card(
        "agentic-card.svg",
        "Agentic Marketing",
        "Autonomous Campaign Orchestrator",
        [
            "Multi-agent marketing intelligence platform automating lead discovery,",
            "scoring qualification models, and drafting personalized, highly",
            "targeted outreach copy powered by Gemini API pipelines."
        ],
        "#f0883e",
        ["PyTorch", "Gemini API", "Hugging Face"],
        agentic_logo
    )

if __name__ == "__main__":
    generate_hero()
    generate_divider()
    generate_cards()
    generate_tech_stack()
    generate_status_widget()
    print("Assets successfully generated.")
