# Credential Harvester Method (SET - Social Engineering Toolkit)



# What is Social Engineering Toolkit (SET)?

SET (Social Engineering Toolkit) is a penetration testing framework included in Kali Linux.

It is designed to simulate social engineering attacks for security testing.

### Uses

- Phishing simulations
- Credential harvesting
- Payload generation
- Website cloning
- Spear phishing
- Wireless attack simulations
- USB attacks

---

# Starting SET

```bash
sudo setoolkit
```

Main Menu

```
SET

│

├── Social Engineering Attacks

├── Website Attack Vectors

├── Infectious Media

├── Payload Generator

├── Mass Mailer

├── Wireless Attacks

└── Others
```

---

# Social Engineering Attack Menu

```
SET

↓

Social Engineering Attacks

↓

1
```

---

# Main Attack Modules

| Option | Attack | Purpose |
|---------|----------|----------|
| 1 | Spear Phishing | Target a specific person |
| 2 | Website Attack Vectors | Simulate website-based phishing attacks |
| 3 | Infectious Media Generator | Create USB/CD attack media |
| 4 | Payload and Listener | Generate payloads for authorized testing |
| 5 | Mass Mailer | Send emails during awareness testing |
| 6 | Arduino Attack | USB device simulations |
| 7 | Wireless Attack | Wireless security assessments |
| 8 | QRCode Generator | Generate QR codes for awareness testing |
| 9 | PowerShell Attack | Windows PowerShell testing |
| 10 | Third Party Modules | Additional security modules |

---

# Spear Phishing Attack

## Definition

A phishing attack that targets one specific person or organization.

Unlike normal phishing:

```
Phishing

↓

Thousands of Users
```

```
Spear Phishing

↓

One Specific Person
```

Example

```
Company CEO

↓

Personalized Email

↓

Credential Theft Simulation
```

---

# Website Attack Vector

Website Attack Vector allows ethical hackers to simulate fake websites during security awareness testing.

Purpose

- Clone websites
- Test user awareness
- Simulate phishing
- Collect test credentials (authorized only)

---

# Website Attack Vector Menu

```
Website Attack Vector

│

├── Java Applet Attack

├── Metasploit Browser Exploit

├── Credential Harvester

├── Tabnabbing

├── Web Jacking

└── Multi Attack
```

---

# Java Applet Attack

## Concept

Older Java browsers displayed popup messages asking users to run Java applications.

Example

```
Popup

↓

Update Java

↓

User Clicks Run

↓

Payload Executes
```

Today:

- Rarely used
- Modern browsers block Java Applets

---

# Browser Exploit Method

Purpose

- Test browser vulnerabilities
- Deliver authorized test payloads
- Simulate browser exploitation

---

# Credential Harvester

## Definition

Credential Harvester creates a cloned login page.

When a user enters credentials:

```
Username

Password

↓

Captured

↓

Stored on Test Server
```

Purpose

- Phishing awareness
- User training
- Security assessments

---

# Credential Harvester Workflow

```
Target Website

↓

Clone Website

↓

Victim Visits Clone

↓

Victim Enters Login

↓

Credentials Captured

↓

Tester Reviews Results
```

---

# Tabnabbing

## Definition

Tabnabbing changes the content of an inactive browser tab.

Example

```
Original Tab

↓

User Leaves Tab

↓

Fake Login Page Appears

↓

User Re-enters Credentials
```

---

# Web Jacking

## Definition

Web Jacking redirects users from one page to another fake page.

Example

```
Original Website

↓

Redirect

↓

Fake Website
```

---

# Multi Attack

## Definition

Multi Attack combines several attack techniques into one campaign.

Example

```
Clone Website

+

Credential Harvester

+

Browser Attack

+

Payload

↓

Combined Simulation
```

---

# Infectious Media Generator

Purpose

Create testing files for:

- USB
- CD
- DVD

Example

```
USB

↓

Payload File

↓

Authorized Testing
```

---

# Payload and Listener

One of the most commonly used penetration testing features.

Purpose

- Generate payloads
- Wait for authorized connections
- Test endpoint security

Workflow

```
Generate Payload

↓

Deliver During Test

↓

Listener Waits

↓

Authorized Connection
```

---

# Mass Mailer

Purpose

Simulate phishing campaigns.

Used for:

- Email awareness
- Security training
- User education

Example

```
Tester

↓

Email Campaign

↓

Employees

↓

Measure Click Rate
```

---

# Arduino Attack Vector

Purpose

Use programmable USB devices to simulate keyboard attacks.

Example

```
USB Device

↓

Acts Like Keyboard

↓

Types Commands Automatically
```

---

# Wireless Attack

Purpose

Evaluate wireless network security.

Examples

- Rogue Access Point
- Evil Twin
- Wireless Monitoring
- Authentication Testing

---

# Rogue Access Point Concept

```
Real Wi-Fi

↓

Company_WiFi
```

Attacker creates

```
Company_WiFi_Free

↓

User Connects

↓

Traffic Passes Through Tester
```

Purpose

- Security testing
- Awareness exercises
- Wireless assessments

---

# Man-in-the-Middle (MITM)

## Definition

A Man-in-the-Middle attack occurs when an attacker secretly sits between two communicating parties.

```
User

↓

Tester

↓

Website
```

Tester can observe network traffic during authorized assessments.

---

# Network Traffic Analysis Tools

Common tools mentioned:

| Tool | Purpose |
|-------|----------|
| Wireshark | Packet analysis |
| Ettercap | MITM testing |
| Aircrack-ng | Wireless security testing |

---

# QR Code Generator

Purpose

Generate QR codes pointing to a URL.

Workflow

```
Generate QR

↓

User Scans

↓

Browser Opens URL
```

Common uses

- Awareness campaigns
- Internal testing
- Company demonstrations

---

# PowerShell Attack Vector

Designed mainly for:

- Windows 8+
- Windows 10
- Windows 11

Purpose

- PowerShell security testing
- Script execution testing
- Defensive validation

---

# Third Party Modules

Contains additional modules such as:

- RAT simulation (for authorized labs)
- Extra penetration testing utilities
- Community extensions

---

# Credential Harvester Walkthrough (Concept)

### Step 1

Start SET

```bash
sudo setoolkit
```

---

### Step 2

Choose

```
1

Social Engineering Attacks
```

---

### Step 3

Choose

```
2

Website Attack Vector
```

---

### Step 4

Choose

```
3

Credential Harvester
```

---

### Step 5

Select

```
Site Cloner
```

---

# Site Cloner

Purpose

Copies the appearance of a legitimate website.

Example

```
Original Login Page

↓

Clone

↓

Looks Almost Identical
```

---

# Site Cloner Options

| Option | Purpose |
|---------|----------|
| Web Templates | Use built-in templates |
| Custom Import | Import your own HTML page |
| Site Cloner | Clone an existing website |

---

# Network Configuration

SET asks for your local IP address.

Example

```bash
ifconfig
```

Output

```
eth0

192.168.1.10
```

Purpose

The cloned website is hosted on the tester's machine during an authorized lab exercise.

---

# Target URL

SET requests a URL.

Example

```
https://example.com
```

SET clones the website layout for awareness testing.

---

# Credential Harvester Process

```
Real Website

↓

Clone Website

↓

Victim Opens Clone

↓

Login Form

↓

Credentials Submitted

↓

Captured on Test Server
```

---

# Why Organizations Use Credential Harvesters

- Employee awareness training
- Phishing simulations
- Security assessments
- Measure phishing susceptibility
- Improve cybersecurity education

---

# Important Ethical Rule

Always use Credential Harvester:

- In your own lab
- During authorized penetration tests
- With written permission
- For awareness training

Never use it against:

- Real users without consent
- Public websites
- Organizations without authorization

Unauthorized credential harvesting is illegal and unethical.
