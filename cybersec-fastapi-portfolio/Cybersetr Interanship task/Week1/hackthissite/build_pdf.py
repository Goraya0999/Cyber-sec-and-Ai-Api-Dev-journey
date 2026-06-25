import os
from weasyprint import HTML, CSS

def read_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception as e:
        return str(e)

summary_txt = read_file('final_results/SUMMARY.txt')
attack_surface_txt = read_file('final_results/attack_surface.txt')
live_hosts_txt = read_file('final_results/live_hosts.txt')
tech_profile_txt = read_file('final_results/tech_profile.txt')
dorking_txt = read_file('final_results/dorking_results.txt')

html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Red Team Reconnaissance Report - hackthissite.org</title>
<style>
    @page {{
        size: A4;
        margin: 20mm;
        @bottom-right {{
            content: "Page " counter(page) " of " counter(pages);
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 10pt;
            color: #666;
        }}
        @bottom-left {{
            content: "CyberStr | Red Team Internship | M. Shafiq Goraya";
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 10pt;
            color: #666;
        }}
    }}
    body {{
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #333;
        line-height: 1.6;
        font-size: 12pt;
    }}
    .cover-page {{
        text-align: center;
        page-break-after: always;
        margin-top: 150px;
    }}
    .cover-page h1 {{
        font-size: 36pt;
        color: #d9534f;
        margin-bottom: 10px;
    }}
    .cover-page h2 {{
        font-size: 24pt;
        color: #555;
        margin-bottom: 50px;
    }}
    .cover-details {{
        font-size: 16pt;
        text-align: left;
        width: 60%;
        margin: 0 auto;
        border-top: 2px solid #d9534f;
        padding-top: 20px;
    }}
    .cover-details strong {{
        color: #d9534f;
    }}
    .cover-logo {{
        max-width: 250px;
        margin-bottom: 40px;
    }}
    h1.section-title {{
        color: #d9534f;
        border-bottom: 2px solid #eee;
        padding-bottom: 5px;
        margin-top: 40px;
        page-break-before: always;
    }}
    h1.first-section {{
        page-break-before: auto;
    }}
    pre {{
        background-color: #2b2b2b;
        color: #f8f8f2;
        padding: 15px;
        border-radius: 5px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 10pt;
        white-space: pre-wrap;
        word-wrap: break-word;
        box-shadow: inset 0 0 10px #000;
    }}
    .screenshot-container {{
        text-align: center;
        margin: 20px 0;
    }}
    .screenshot-container img {{
        max-width: 100%;
        border: 1px solid #ddd;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border-radius: 4px;
    }}
    .screenshot-caption {{
        font-size: 10pt;
        color: #666;
        margin-top: 5px;
        font-style: italic;
    }}
    .grid-container {{
        display: block;
        text-align: center;
    }}
    .grid-item {{
        display: inline-block;
        width: 45%;
        margin: 10px;
        vertical-align: top;
    }}
    .grid-item img {{
        max-width: 100%;
        border: 1px solid #ccc;
    }}
</style>
</head>
<body>

    <!-- COVER PAGE -->
    <div class="cover-page">
        <img src="Assets/Front-Page -of -report/organization-logo-must-be-in-front-page.jpeg" class="cover-logo" alt="CyberStr Logo">
        <h1>Red Team Reconnaissance Report</h1>
        <h2>Target: hackthissite.org</h2>
        
        <div class="cover-details">
            <p><strong>Organization:</strong> CyberStr</p>
            <p><strong>Role:</strong> Red Team Internship</p>
            <p><strong>Intern Name:</strong> Muhammad Shafiq Goraya</p>
            <p><strong>Instructor:</strong> Umar Niaz</p>
            <p><strong>Date:</strong> June 25, 2026</p>
            <p><strong>Week:</strong> 1 - Information Gathering</p>
        </div>
    </div>

    <!-- EXECUTIVE SUMMARY -->
    <h1 class="section-title first-section">1. Executive Summary</h1>
    <p>This document contains the consolidated results of the week 1 reconnaissance task on the authorized training target <strong>hackthissite.org</strong>. The process involved passive information gathering using various Open Source Intelligence (OSINT) techniques and automated enumeration tools.</p>
    <pre>{summary_txt}</pre>

    <!-- LIVE ASSET RECON -->
    <h1 class="section-title">2. Live Asset & Visual Reconnaissance</h1>
    <p>The following screenshots were captured during the engagement, highlighting the tools utilized for subdomain enumeration and the results of visual reconnaissance using Aquatone.</p>
    
    <h3>2.1 Tool Execution Evidence</h3>
    <div class="screenshot-container">
        <img src="final_results/screenshots/Screenshot From 2026-06-25 04-59-18.png" alt="Subfinder Execution">
        <div class="screenshot-caption">Figure 1: Subfinder passive subdomain enumeration.</div>
    </div>
    
    <div class="screenshot-container">
        <img src="final_results/screenshots/Screenshot From 2026-06-25 07-12-57.png" alt="httpx Execution">
        <div class="screenshot-caption">Figure 2: Verifying live hosts and identifying tech stacks using httpx.</div>
    </div>

    <h3>2.2 Target Visual Evidence</h3>
    <p>Aquatone was used to capture visual representations of the live subdomains. The following assets were deemed of interest.</p>
    <div class="grid-container">
        <div class="grid-item">
            <img src="final_results/screenshots/http__hp_hackthissite_org__da39a3ee5e6b4b0d.png" alt="HackThisSite Main">
            <div class="screenshot-caption">Figure 3: Login panel identified on hp.hackthissite.org.</div>
        </div>
        <div class="grid-item">
            <img src="final_results/screenshots/https__h5ai_hackthissite_org__da39a3ee5e6b4b0d.png" alt="h5ai Subdomain">
            <div class="screenshot-caption">Figure 4: h5ai mirror development server page.</div>
        </div>
    </div>

    <pre>{live_hosts_txt}</pre>

    <!-- INFRASTRUCTURE PROFILE -->
    <h1 class="section-title">3. Infrastructure & Tech Profile</h1>
    <p>Infrastructure profiling helps in mapping out the target's underlying network, cloud providers, and web technology stacks. The results incorporate WhatWeb, Wappalyzer, WHOIS, and DNS querying.</p>
    <div class="screenshot-container" style="max-width: 60%; margin: 0 auto;">
        <img src="final_results/screenshots/Screenshot From 2026-06-25 06-52-13.png" alt="Wappalyzer Check">
        <div class="screenshot-caption">Figure 5: Wappalyzer extension verifying technology stack (jQuery 1.8.1).</div>
    </div>
    <br>
    <pre>{tech_profile_txt}</pre>

    <!-- ATTACK SURFACE -->
    <h1 class="section-title">4. Comprehensive Attack Surface</h1>
    <p>The consolidated list of discovered subdomains derived from Subfinder, Assetfinder, Amass, CRT.sh, and DNSDumpster, deduplicated and categorized by confidence level.</p>
    <pre>{attack_surface_txt}</pre>

    <!-- DORKING RESULTS -->
    <h1 class="section-title">5. OSINT & Dorking Findings</h1>
    <p>Advanced Google dorking and GitHub secret hunting were performed to identify potential data exposures, credential leaks, and backup files.</p>
    <div class="screenshot-container" style="max-width: 70%; margin: 0 auto;">
        <img src="final_results/screenshots/Screenshot From 2026-06-25 06-34-29.png" alt="Robots.txt verification">
        <div class="screenshot-caption">Figure 6: Manual verification of robots.txt paths.</div>
    </div>
    <br>
    <pre>{dorking_txt}</pre>
    
    <br><br>
    <hr>
    <p style="text-align:center; font-size:10pt; color:#888;">
        <strong>Disclaimer:</strong> This report is intended solely for educational purposes and is authorized under the CyberStr Red Team Internship program.
    </p>

</body>
</html>
"""

with open('report.html', 'w') as f:
    f.write(html_content)

try:
    print("Generating PDF...")
    HTML('report.html', base_url=os.path.abspath('.')).write_pdf('report.pdf')
    print("PDF generated successfully: report.pdf")
except Exception as e:
    print(f"Error generating PDF: {e}")
