# Social Engineering Toolkit (SET) – Credential Harvester Attack (Study Notes)

> **⚠️ Ethical Use Only:** The following notes explain how the **Credential Harvester** feature works from an educational and defensive perspective. It should only be used in **authorized penetration tests or cybersecurity labs** with explicit permission.

---

# What is Credential Harvesting?

Credential Harvesting is a **social engineering technique** where an attacker creates a **fake login page** that closely resembles a legitimate website (such as Gmail, Facebook, or LinkedIn). The goal is to trick users into entering their credentials.

Instead of authenticating the user, the fake page records the submitted username and password.

---

# Credential Harvesting Workflow

```text
Attacker
    │
    ▼
Creates Fake Login Page
    │
    ▼
Sends Link to Victim
    │
    ▼
Victim Opens Link
    │
    ▼
Victim Enters Username & Password
    │
    ▼
Credentials Captured
    │
    ▼
(Optional) Redirect to Legitimate Website
```

---

# What is the Social Engineering Toolkit (SET)?

The **Social Engineering Toolkit (SET)** is an open-source penetration testing framework included with Kali Linux. It helps cybersecurity professionals simulate **social engineering attacks** during authorized security assessments.

### Key Features

- Phishing website simulation
- Credential harvesting
- Payload generation
- Spear phishing campaigns
- Wireless attack simulations
- USB attack simulations
- QR code attacks
- PowerShell attacks
- Email attack simulations

---

# Main Social Engineering Attack Categories

| Option | Attack | Description |
|---------|--------|-------------|
| 1 | Spear Phishing Attack | Targets a specific individual with personalized phishing emails. |
| 2 | Website Attack Vectors | Creates fake websites for phishing simulations. |
| 3 | Infectious Media Generator | Simulates malware delivery through USB/CD media. |
| 4 | Create Payload and Listener | Generates payloads and listens for authorized callback connections. |
| 5 | Mass Mailer Attack | Simulates bulk email campaigns for security awareness testing. |
| 6 | Arduino-Based Attack | Simulates USB keyboard/device attacks using Arduino-compatible hardware. |
| 7 | Wireless Attack Vector | Simulates wireless security attacks in authorized environments. |
| 8 | QRCode Generator Attack | Creates QR codes pointing to user-defined URLs. |
| 9 | PowerShell Attack Vector | Demonstrates PowerShell-based attack simulations on Windows systems. |
| 10 | Third-Party Modules | Additional security testing modules and plugins. |

---

# Website Attack Vector Methods

| Method | Purpose |
|---------|---------|
| Java Applet Attack | Historical Java-based attack simulation (mostly obsolete today). |
| Metasploit Browser Exploit | Uses browser vulnerabilities during authorized testing. |
| Credential Harvester | Creates fake login pages to collect credentials during awareness exercises. |
| Tabnabbing | Replaces inactive browser tabs with fake login pages. |
| Web Jacking | Redirects victims to deceptive websites. |
| Multi-Attack Method | Combines multiple attack techniques into one simulation. |

---

# Credential Harvester Components

| Component | Function |
|-----------|----------|
| Website Cloner | Copies the appearance of a legitimate website. |
| Local Web Server | Hosts the cloned website. |
| Fake Login Page | Displays a convincing login interface. |
| Credential Logger | Stores submitted usernames and passwords. |
| Redirect Mechanism | Optionally forwards users to the real website after submission. |

---

# Credential Harvester Process

```text
Clone Website
      │
      ▼
Host Fake Login Page
      │
      ▼
Share Link with Target
      │
      ▼
Victim Opens Website
      │
      ▼
Victim Enters Credentials
      │
      ▼
Credentials Recorded
      │
      ▼
(Optional Redirect to Original Website)
```

---

# Social Engineering Techniques Used

| Technique | Explanation |
|-----------|-------------|
| Fear | Threatens account suspension or deletion. |
| Urgency | Encourages immediate action. |
| Authority | Appears to come from an official organization. |
| Trust | Uses recognizable branding and logos. |
| Familiarity | Mimics legitimate login pages. |

---

# Why Victims Fall for Credential Harvesting

| Reason | Explanation |
|---------|-------------|
| Trust in Popular Brands | Users recognize familiar websites. |
| Urgent Messages | People act quickly without verification. |
| Professional Appearance | Fake pages closely resemble legitimate websites. |
| Lack of Awareness | Users may not inspect URLs carefully. |
| Habit | Users routinely enter passwords without checking authenticity. |

---

# Common Phishing Indicators

| Warning Sign | Description |
|--------------|-------------|
| Misspelled Domain | Example: `gmai1.com` instead of `gmail.com`. |
| Suspicious URL | Unexpected or unfamiliar web address. |
| Grammar Mistakes | Poor spelling or grammar in messages. |
| Urgent Language | Claims such as "Your account will be deleted today." |
| Unexpected Login Request | Login requested without a legitimate reason. |
| Missing HTTPS | Website lacks a secure connection. |

---

# Defensive Measures

| Defense | Benefit |
|----------|---------|
| Verify URLs | Ensures the website is legitimate. |
| Check HTTPS | Confirms encrypted communication. |
| Enable MFA | Protects accounts even if passwords are compromised. |
| Use Password Managers | Autofills credentials only on legitimate domains. |
| Security Awareness Training | Helps users identify phishing attempts. |
| Email Filtering | Blocks many phishing emails before delivery. |
| Web Filtering | Prevents access to known malicious websites. |

---

# Ethical Applications

| Use Case | Purpose |
|----------|---------|
| Security Awareness Training | Tests employee ability to recognize phishing. |
| Penetration Testing | Evaluates organizational defenses. |
| Red Team Assessments | Simulates real-world attacker behavior. |
| Security Audits | Identifies weaknesses in user awareness. |

---
