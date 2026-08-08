# Social Engineering Toolkit (SET) – Credential Harvester (Educational Notes)



# What is the Credential Harvester?

The **Credential Harvester** is a module in the **Social-Engineer Toolkit (SET)** that demonstrates how attackers may attempt to collect usernames and passwords using fake login pages.

> **Purpose in Ethical Hacking**
>
> It is used only during **authorized penetration tests** to evaluate an organization's resistance to phishing attacks and improve security awareness.

---

# Common Social Engineering Attack Modules in SET

| Module | Purpose |
|---------|---------|
| Spear Phishing | Simulates targeted phishing attacks against specific individuals. |
| Website Attack Vectors | Demonstrates attacks involving cloned or simulated websites. |
| Credential Harvester | Simulates credential collection through fake login pages during authorized assessments. |
| Multi-Attack Method | Combines multiple simulated attack techniques in a single assessment. |
| Mass Mailer | Used in security awareness exercises to send bulk emails within an authorized environment. |
| Wireless Attack Tools | Used to assess wireless network security in authorized environments. |
| QR Code Generator | Generates QR codes for legitimate security awareness demonstrations. |
| PowerShell Attack Vectors | Demonstrates PowerShell-based security risks on Windows systems. |

---

# Credential Harvesting Workflow (High-Level)

```text
User Awareness Test
        │
        ▼
Simulated Login Page
        │
        ▼
User Attempts Login
        │
        ▼
Assessment Records Interaction
        │
        ▼
Security Team Reviews Results
        │
        ▼
Organization Improves Security Controls
```

---

# Defensive Learning Points

- Always verify website URLs before entering credentials.
- Look for HTTPS and valid certificates.
- Be suspicious of urgent messages requesting immediate login.
- Enable Multi-Factor Authentication (MFA).
- Use password managers to detect fake websites.
- Report suspicious emails to your IT department.
- Never enter credentials from links received in unexpected emails.

---

# Common Indicators of Phishing

| Indicator | Description |
|-----------|-------------|
| Misspelled domain | URL differs slightly from the legitimate website. |
| Urgent language | Claims account will be suspended immediately. |
| Grammar mistakes | Poor spelling or unusual wording. |
| Unexpected login request | Requests credentials without prior notice. |
| Suspicious sender | Email address does not match the official organization. |

---

# Ethical Use

Credential harvesting demonstrations should only be performed:

- With written authorization
- During approved penetration tests
- In security awareness training
- In laboratory or educational environments

Unauthorized credential collection is illegal and unethical.

---
