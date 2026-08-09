# Metadata Extraction, ExifTool & Google Reconnaissance Tools


# Information Leakage Through Metadata

Many digital files contain hidden information known as **metadata**.

Metadata is information **about the file**, not the visible content itself.

Examples include:

* Author name
* Software used
* Camera model
* GPS coordinates (if enabled)
* Creation date
* Modification date
* Device information
* File size
* Operating system
* Document creator

Attackers often inspect metadata during the **Footprinting** phase because it can reveal useful information about an organization or individual.

---

# What is Metadata?

Metadata is structured information embedded inside digital files.

Examples of files that contain metadata include:

* PDF
* DOC
* DOCX
* PPT
* PPTX
* XLS
* XLSX
* Images (JPG, PNG, TIFF)
* Audio files
* Videos

---

# Why Metadata Matters

Imagine a company publishes a PDF report on its website.

The document itself may only contain public information.

However, the embedded metadata may reveal:

* Employee username
* Internal computer name
* Software version
* Operating system
* Organization name
* Document author

This information can assist attackers during reconnaissance and should be reviewed before publication.

---

# MetaGoofil

## What is MetaGoofil?

MetaGoofil is an **Open Source Information Gathering (OSINT)** tool that downloads publicly available documents from a target domain and extracts their metadata.

---

## Supported File Types

MetaGoofil searches for files such as:

* PDF
* DOC
* DOCX
* PPT
* PPTX
* XLS
* XLSX

---

## Information It Can Extract

Examples include:

* Author names
* Usernames
* Software versions
* Operating system details
* Email addresses
* File paths
* Printer information
* Company names

---

## Why Use MetaGoofil?

During an authorized penetration test, MetaGoofil helps identify information unintentionally exposed through publicly available documents.

---

# ExifTool

## What is ExifTool?

**ExifTool** is one of the most powerful metadata extraction utilities available.

It can read, write, and edit metadata from hundreds of file formats.

Unlike MetaGoofil, which focuses on downloading public documents from websites, ExifTool analyzes metadata from files you already possess.

---

# Common Uses

ExifTool can analyze:

* Images
* PDFs
* Microsoft Office documents
* Audio files
* Video files
* Camera RAW files

---

# Installation (Kali Linux)

ExifTool is commonly pre-installed on Kali Linux.

To verify installation:

```bash
exiftool -ver
```

Display help:

```bash
exiftool -help
```

---

# Basic Syntax

```bash
exiftool filename
```

---

## Example

```bash
exiftool report.pdf
```

---

## Example

```bash
exiftool image.jpg
```

---

# Example Output

Running ExifTool on a PDF might reveal:

```text
File Name              : report.pdf
File Type              : PDF
Creator                : Adobe InDesign CS6
Producer               : Adobe PDF Library
Create Date            : 2013:07:14
Modify Date            : 2013:07:14
Operating System       : Windows
```

---

# Metadata Available in Images

Image metadata may include:

* Camera manufacturer
* Camera model
* Lens information
* Date taken
* Image resolution
* Flash settings
* ISO value
* Exposure
* GPS coordinates (if enabled)
* Orientation

---

# Example Scenario

Suppose someone uploads a photograph to a website.

If the image still contains metadata, ExifTool might reveal:

* Camera model
* Device manufacturer
* Capture date
* Editing software
* GPS location (if available)
* File creation details

Many social media platforms remove or reduce metadata, but files shared directly (such as via email or USB) may retain much of this information.

---

# Example PDF Metadata

The tutorial demonstrates that ExifTool can reveal information such as:

* File creator
* Adobe InDesign version
* Operating system
* Creation date
* Document producer

These details can provide valuable context during authorized security assessments.

---

# Information Commonly Found in Metadata

| Category         | Example                  |
| ---------------- | ------------------------ |
| Author           | John Smith               |
| Software         | Adobe Acrobat            |
| Device           | Sony Camera              |
| Operating System | Windows 11               |
| GPS              | Latitude & Longitude     |
| Company          | ABC Corporation          |
| Creation Date    | 2025-06-20               |
| File Path        | C:\Users\Admin\Documents |

---

# Metadata Risks

Sensitive metadata may unintentionally disclose:

* Employee usernames
* Internal file paths
* Software versions
* Organizational details
* Device information
* Geolocation
* Timestamps

This information can assist attackers in profiling a target.

---

# Metadata Sanitization

Before publishing files online:

* Remove unnecessary metadata.
* Export clean copies of documents.
* Strip GPS data from photographs.
* Remove author information.
* Review document properties.

This process is known as **metadata sanitization**.

---

# Google Reconnaissance Tools

The tutorial introduces several reconnaissance tools that leverage Google search results.

---

# 1. Gooscan

## Purpose

Gooscan automates Google search queries to identify potential security issues and publicly exposed resources.

### Features

* Automated Google searches
* Reconnaissance support
* Vulnerability discovery
* Search result automation

---

# 2. SiteDigger

## Purpose

SiteDigger searches Google's index for publicly exposed information related to a target website.

### Can Help Identify

* Error messages
* Configuration issues
* Publicly accessible resources
* Indexed sensitive content

---

# 3. Google Hacking Database (GHDB)

GHDB is a collection of carefully crafted Google search queries used to identify publicly accessible information that may indicate security weaknesses.

It is commonly used during authorized reconnaissance to discover exposed resources.

---

# 4. BiLE Suite (Bi-directional Link Extractor)

BiLE Suite analyzes relationships between websites by examining inbound and outbound links.

### Purpose

* Discover related domains
* Analyze website relationships
* Support reconnaissance and mapping efforts

---

# 5. Google Hack Honeypot (GHH)

Google Hack Honeypot is a defensive tool designed to detect and monitor malicious search activity.

### Objectives

* Detect reconnaissance attempts
* Monitor suspicious visitors
* Gather intelligence about attacker behavior
* Improve defensive monitoring

---

# 6. GMapCatcher

Originally designed to download and cache Google Maps for offline viewing.

While mentioned in the tutorial, it is not commonly used in modern penetration testing workflows.

---

# Ethical Considerations

The transcript discusses examples of discovering publicly exposed information. These examples are intended to illustrate how accidental information disclosure can occur.

Ethical hackers should:

* Analyze only systems they own or are authorized to assess.
* Report discovered exposures responsibly.
* Avoid collecting or using sensitive personal information from unauthorized sources.
* Focus on helping organizations remediate security weaknesses.

---

# Best Practices for Organizations

To reduce metadata and information leakage:

* Remove metadata before publishing documents.
* Strip EXIF data from images.
* Review PDF document properties.
* Disable unnecessary GPS tagging.
* Keep software updated.
* Audit publicly available documents.
* Restrict indexing of sensitive resources.
* Conduct regular OSINT assessments.

---

# Comparison of Tools

| Tool                 | Primary Purpose                                 |
| -------------------- | ----------------------------------------------- |
| ExifTool             | Read and edit metadata from local files         |
| MetaGoofil           | Download public documents and extract metadata  |
| SiteDigger           | Search indexed websites for exposed information |
| Gooscan              | Automate Google reconnaissance searches         |
| GHDB                 | Repository of Google Dork queries               |
| BiLE Suite           | Analyze relationships between websites          |
| Google Hack Honeypot | Detect and monitor reconnaissance activity      |
| GMapCatcher          | Cache Google Maps for offline use               |

---

# Key Terms

| Term         | Description                                                     |
| ------------ | --------------------------------------------------------------- |
| Metadata     | Information embedded within a file describing its properties    |
| EXIF         | Exchangeable Image File Format metadata used by digital cameras |
| ExifTool     | Metadata extraction and editing utility                         |
| MetaGoofil   | OSINT tool for extracting metadata from public documents        |
| Sanitization | Removing sensitive metadata before publication                  |
| OSINT        | Open Source Intelligence                                        |
| GHDB         | Google Hacking Database                                         |
| SiteDigger   | Tool for finding indexed information on websites                |
| Honeypot     | Defensive system used to detect and analyze attacker activity   |

---

# Important Notes

* Metadata often reveals more information than users expect.
* Images, PDFs, and Office documents commonly contain metadata.
* ExifTool is one of the most widely used metadata analysis tools.
* MetaGoofil is valuable during authorized OSINT investigations.
* Always sanitize documents before publishing them publicly.
* Metadata analysis should only be performed on files you own or have permission to inspect.

---

# Exam & Interview Questions

## Q1. What is metadata?

**Answer:**
Metadata is information stored within a file that describes its properties, such as author, creation date, software used, and device information.

---

## Q2. What is ExifTool?

**Answer:**
ExifTool is a command-line utility used to read, write, and edit metadata from many file types, including images, PDFs, Office documents, audio, and video files.

---

## Q3. What is MetaGoofil used for?

**Answer:**
MetaGoofil downloads publicly available documents from a target domain and extracts metadata to support authorized OSINT and penetration testing.

---

## Q4. What types of files commonly contain metadata?

**Answer:**

* PDF
* DOC/DOCX
* PPT/PPTX
* XLS/XLSX
* JPG
* PNG
* TIFF
* Audio files
* Video files

---

## Q5. Why should organizations remove metadata before publishing documents?

**Answer:**
Removing metadata helps prevent the accidental disclosure of usernames, software versions, device information, file paths, GPS coordinates, and other sensitive details that could aid attackers.

---

## Q6. What is the difference between ExifTool and MetaGoofil?

**Answer:**

* **ExifTool** analyzes metadata from files you already have.
* **MetaGoofil** discovers publicly available documents from a target website and extracts their metadata.
