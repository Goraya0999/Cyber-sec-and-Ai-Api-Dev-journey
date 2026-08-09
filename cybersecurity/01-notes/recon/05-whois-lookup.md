# Google Hacking Database (GHDB), WHOIS Lookup & Metadata Extraction


# 1. Introduction

This lecture focuses on **Passive Reconnaissance (Footprinting)**, where an ethical hacker gathers publicly available information about a target **without directly interacting with the target's systems**.

The major topics covered are:

* Google Hacking Database (GHDB)
* Google Dorks
* WHOIS Lookup
* Metadata Extraction
* ExifTool
* Introduction to DNS Interrogation

> **Note:** Passive reconnaissance helps security professionals understand a target's public exposure while minimizing the chance of detection.

---

# 2. Google Hacking Database (GHDB)

## What is GHDB?

The **Google Hacking Database (GHDB)** is a repository of carefully crafted **Google search operators (Google Dorks)** that help locate publicly accessible information indexed by Google.

These searches are useful during **authorized security assessments** and **OSINT investigations**.

### Examples of information that may be discovered

* Public PDF files
* Login portals
* Configuration files
* Backup files
* Open directories
* Test environments
* Exposed documentation

---

## Important Note

Google Dorking **does not hack a system**.

It only searches Google's publicly indexed content.

Finding exposed information **does not grant permission to access or exploit it**.

Ethical hackers only investigate systems they are authorized to test.

---

# 3. Exploit-DB and Google Dorks

Historically, the **Google Hacking Database** was maintained by **Exploit-DB**.

It categorized hundreds of Google Dorks into different groups such as:

* Files containing passwords
* Vulnerable web applications
* Open directories
* Database backups
* Login pages
* Security cameras
* Error messages

Today, many researchers also maintain updated Google Dork collections on GitHub.

---

## Common Google Dorks

```text
site:example.com

filetype:pdf

intitle:"index of"

inurl:admin

intext:"confidential"
```

These operators help narrow search results during reconnaissance.

---

# 4. WHOIS Lookup

## What is WHOIS?

WHOIS is a protocol used to query public registration databases for information about:

* Domain names
* IP addresses
* Autonomous Systems (ASN)

It provides registration information maintained by domain registrars and regional internet registries.

---

## Information Available Through WHOIS

Depending on privacy settings, WHOIS may reveal:

* Domain name
* Registrar
* Registration date
* Expiration date
* Last updated date
* Name servers
* DNSSEC status
* Registrant organization
* Administrative contacts (if not privacy protected)

---

## Example

```text
Domain:
example.com

Registrar:
Cloudflare

Registered:
2018

Expires:
2028

Nameservers:
ns1.cloudflare.com
ns2.cloudflare.com
```

---

## Why Attackers Use WHOIS

WHOIS helps attackers gather:

* Registrar information
* Hosting provider
* Domain age
* DNS provider
* Nameservers

This information assists in mapping an organization's infrastructure during reconnaissance.

---

## Why Defenders Use WHOIS

Security professionals use WHOIS for:

* Incident response
* Threat intelligence
* Investigating phishing domains
* Domain ownership verification

---

# Modern Reality

Older WHOIS records often revealed personal information.

Today, most registrars hide personal details because of:

* GDPR
* Privacy protection services
* ICANN privacy policies

Instead of

```text
John Smith
Phone Number
Email Address
```

you usually see

```text
REDACTED FOR PRIVACY
```

---

# 5. Metadata Extraction

## What is Metadata?

Metadata means:

> Data about data.

Many files contain hidden information that users never see.

---

## Metadata Examples

### Images

* Camera model
* GPS coordinates
* Date taken
* Software used
* Device information

### PDF Files

* Author
* Company
* Creation date
* Modification date
* Editing software

### Microsoft Office Documents

* Username
* Company name
* Template
* Printer information
* Revision history

---

# Why Metadata Matters

Metadata can reveal valuable OSINT information about:

* Employees
* Software versions
* Internal usernames
* Company structure
* Office locations

---

# 6. ExifTool

## What is ExifTool?

ExifTool is one of the most powerful metadata extraction tools.

It supports hundreds of file formats including:

* JPG
* PNG
* PDF
* DOCX
* XLSX
* MP4
* TIFF

---

## Basic Command

```bash
exiftool image.jpg
```

---

## Example Output

```text
Camera:
Canon EOS R6

GPS:
34.1234

Software:
Adobe Photoshop

Date:
2025
```

---

## Example with a PDF

```bash
exiftool Annual_Report.pdf
```

Possible output:

```text
Author:
Alice

Software:
Adobe InDesign

Company:
ABC Corporation

Creation Date:
2024
```

---

## Why This Is Useful

Suppose a company uploads:

```text
Annual_Report.pdf
```

Metadata may reveal:

* Employee names
* Internal software
* Company name
* Creation dates
* Editing history

This information is valuable during passive reconnaissance.

---

# Modern Note

Many online services automatically remove image metadata.

Examples:

* Instagram
* Facebook
* X (Twitter)

However, metadata is often preserved in:

* Email attachments
* Direct file sharing
* Internal document repositories
* Company websites

---

# 7. DNS Interrogation (Introduction)

The instructor briefly introduces DNS interrogation, which will be covered in the next lecture.

Topics include:

* DNS Records
* A Records
* AAAA Records
* MX Records
* TXT Records
* NS Records
* Reverse DNS
* Zone Transfers

DNS interrogation is another important passive reconnaissance technique.

---

# 8. Incorrect or Outdated Claims in the Lecture

## Claim 1

> Google stores everything forever.

**Correction**

False.

Google continuously updates its index.

Pages may change, disappear, or be removed.

---

## Claim 2

> Anyone can always view domain owner information.

**Correction**

Mostly false today.

Privacy regulations and registrar privacy services hide personal information for many domains.

---

## Claim 3

Several GUI WHOIS applications demonstrated in the lecture are outdated.

Modern professionals usually prefer:

* Linux `whois`
* Online WHOIS services
* Threat intelligence platforms
* OSINT frameworks

---

# 9. Modern Alternatives and Best Practices

| Tool           | Purpose                    | Status         |
| -------------- | -------------------------- | -------------- |
| WHOIS          | Domain registration lookup | ✅ Essential    |
| ExifTool       | Metadata extraction        | ✅ Excellent    |
| Google Dorking | OSINT searches             | ✅ Essential    |
| GHDB           | Collection of Google Dorks | ✅ Relevant     |
| SmartWhois     | GUI WHOIS                  | ⚠️ Less common |
| ActiveWhois    | GUI WHOIS                  | ⚠️ Less common |

---

