# Digital Forensics Using Kali Linux Tools 

> 

# 1. What is Digital Forensics?

Digital Forensics is the science of:

- Preserving
- Acquiring
- Documenting
- Analyzing
- Interpreting

digital evidence from computers, mobile devices, storage media, and networks.

It helps investigators determine:

- What happened?
- When did it happen?
- How did it happen?
- Who performed the activity?
- What evidence exists?

---

# 2. Digital Forensics and Ethical Hacking

Digital Forensics is a natural extension of Ethical Hacking.

Ethical hackers use forensic techniques to:

- Investigate security incidents
- Analyze cyber attacks
- Recover deleted evidence
- Understand attacker behavior
- Preserve digital evidence
- Prevent future attacks

---

# 3. Digital Forensics Process

The standard forensic investigation process consists of:

```text
Incident Occurs
        │
        ▼
Evidence Preservation
        │
        ▼
Evidence Acquisition
        │
        ▼
Documentation
        │
        ▼
Evidence Analysis
        │
        ▼
Interpretation
        │
        ▼
Reporting
```

---

# 4. Evidence Preservation

Evidence Preservation ensures that the original evidence remains unchanged.

Goals:

- Prevent data modification
- Maintain evidence integrity
- Preserve the chain of custody
- Ensure legal admissibility

---

# 5. Evidence Acquisition

Acquisition is the process of collecting digital evidence from:

- Hard disks
- SSDs
- USB drives
- Mobile phones
- Memory dumps
- Network captures
- Cloud storage

The collected copy should be an exact duplicate of the original.

---

# 6. Documentation

Every investigation should document:

- Investigator name
- Date and time
- Device information
- Serial numbers
- Hash values
- Investigation steps
- Findings

Proper documentation ensures reproducibility and legal validity.

---

# 7. Evidence Analysis

During analysis, investigators examine:

- Deleted files
- Browser history
- Registry entries
- System logs
- Network logs
- User activity
- Malware
- Hidden files

---

# 8. Interpretation

Interpretation involves explaining:

- Timeline of events
- Attack methods
- Compromised systems
- Impact of the incident
- Supporting evidence

---

# 9. Forensic Carving

## Definition

Forensic Carving is the process of recovering files **without relying on the file system metadata**.

Instead, it searches raw disk or memory data for recognizable file signatures.

---

## Why File Carving?

Useful when files are:

- Deleted
- Corrupted
- Partially overwritten
- Missing file system entries

---

## How File Carving Works

File carving searches for:

- File headers
- File footers
- File signatures

It reconstructs files based on these patterns.

Example:

```text
Raw Disk

↓

Find JPEG Header

↓

Find JPEG Footer

↓

Recover Image
```

---

# 10. Advantages of Forensic Carving

- Recovers deleted files
- Works without file system metadata
- Useful after malware attacks
- Helps recover fragmented evidence

---

# 11. Kali Linux Forensic Carving Tools

## MagicRescue

Interface:

Command Line

Purpose:

- Recovers deleted or damaged files
- Uses file signatures
- Supports multiple file types

---

## Scalpel

Interface:

Command Line

Purpose:

- High-speed file carving
- Searches raw storage
- Detects headers and footers
- Reconstructs deleted files

---

## Scrounge-NTFS

Interface:

Command Line

Purpose:

- Recovers deleted files
- Repairs corrupted NTFS partitions
- Extracts recoverable NTFS data

---

# 12. Forensic Imaging

## Definition

Forensic Imaging creates an exact **bit-by-bit copy** of a storage device.

Every bit is copied exactly.

The original device is never analyzed directly.

---

## Why Use Forensic Imaging?

Benefits:

- Protects original evidence
- Preserves integrity
- Enables repeatable investigations
- Prevents accidental modification

---

## Imaging Process

```text
Original Drive
        │
        ▼
Bit-by-Bit Copy
        │
        ▼
Forensic Image
        │
        ▼
Analysis Performed Here
```

---

# 13. GuyMager

GuyMager is Kali Linux's forensic imaging tool.

It supports:

- Bit-by-bit imaging
- Automated hashing
- Multiple image formats
- Simultaneous imaging
- Write blocker compatibility

---

# 14. Automated Hashing

Hashing creates a unique digital fingerprint.

Example algorithms:

- MD5
- SHA1
- SHA256

Workflow:

```text
Original Drive

↓

Generate Hash

↓

Create Image

↓

Generate Hash Again

↓

Compare Hashes

↓

Match = Integrity Verified
```

---

# 15. Write Blocker

A Write Blocker prevents any changes to the original storage device.

Benefits:

- Prevents accidental writes
- Maintains evidence integrity
- Required for forensic best practices

---

# 16. PDF Forensics

PDF Forensics analyzes PDF files for malicious content.

Attackers often use PDFs to deliver:

- Malware
- Phishing payloads
- JavaScript exploits
- Embedded executables

---

# 17. PDFiD

Interface:

Command Line

Purpose:

Quickly scans PDFs for suspicious indicators.

Detects:

- JavaScript
- Embedded files
- Encoded streams
- Automatic actions

PDFiD is considered a **triage tool** because it provides a quick overview rather than deep analysis.

---

# 18. PDF-Parser

Interface:

Command Line

Purpose:

Provides detailed analysis of PDF objects.

Capabilities:

- Extract objects
- Search objects
- Analyze JavaScript
- Decode streams
- Inspect embedded content

---

# 19. PDFiD vs PDF-Parser

| Feature | PDFiD | PDF-Parser |
|----------|--------|------------|
| Speed | Fast | Moderate |
| Analysis | Basic | Detailed |
| JavaScript Detection | Yes | Yes |
| Embedded Objects | Detects | Extracts & Analyzes |
| Purpose | Triage | Deep Investigation |

---

# 20. The Sleuth Kit (TSK)

The Sleuth Kit is an open-source digital forensic framework.

It consists of:

- C Library
- Command-line utilities

Purpose:

- Disk image analysis
- File system analysis
- Deleted file recovery
- Timeline analysis

---

# 21. Features of TSK

- Analyze disk images
- Recover deleted files
- Examine file systems
- Extract metadata
- Build timelines
- Investigate partitions

---

# 22. Autopsy

Autopsy is a graphical interface built on top of The Sleuth Kit.

Relationship:

```text
The Sleuth Kit (CLI)

↓

Autopsy (GUI)
```

Autopsy makes forensic analysis easier through a user-friendly interface.

---

# 23. Data Anonymization

## Definition

Data Anonymization means removing or hiding Personally Identifiable Information (PII).

Examples:

- Email addresses
- Phone numbers
- Names
- National IDs
- IP addresses (when required)
- Account numbers

---

## Why is Data Anonymization Important?

Benefits:

- Protects privacy
- Complies with laws
- Prevents data leakage
- Supports ethical investigations

---

# 24. Personally Identifiable Information (PII)

Examples:

- Name
- Address
- Email
- Phone number
- Passport number
- National ID
- Credit card number

Investigators should protect PII whenever possible.

---

# 25. Investigation Scope

Before starting any forensic investigation, define the scope.

The scope determines:

- Which systems are authorized
- Which users are included
- Which devices may be analyzed
- Investigation timeframe

---

# 26. Why Scope Matters

A clearly defined scope:

- Prevents unauthorized access
- Avoids accidental damage
- Protects unrelated systems
- Ensures legal compliance

---

# 27. Example Investigation Scope

Authorized:

- Email server
- HR workstation
- Company file server

Not Authorized:

- Employee personal laptop
- Third-party systems
- External cloud accounts

---

# 28. Kali Linux Digital Forensic Tools

| Tool | Purpose |
|------|----------|
| MagicRescue | File recovery |
| Scalpel | File carving |
| Scrounge-NTFS | NTFS recovery |
| GuyMager | Disk imaging |
| PDFiD | PDF scanning |
| PDF-Parser | PDF analysis |
| Sleuth Kit (TSK) | Disk and filesystem analysis |
| Autopsy | GUI for TSK |

---
