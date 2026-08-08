# Kali Linux Information Gathering




# 1. What is Footprinting?

Footprinting is the **first phase of Ethical Hacking**.

It involves collecting as much information as possible about a target before attempting any security assessment.

The collected information helps security professionals understand:

- Target infrastructure
- Domains
- Servers
- Email addresses
- Network topology
- Technologies used
- Operating systems
- Public IP addresses
- DNS configuration

---

# 2. Types of Footprinting

## Passive Footprinting

No direct interaction with the target.

Examples

- Google Search
- WHOIS
- DNS Records
- Public documents
- Social media
- Search engines

Very stealthy.

---

## Active Footprinting

Direct interaction with the target.

Examples

- Nmap
- Ping
- Traceroute
- DNS Zone Transfer
- Port Scanning

More information can be collected but is easier to detect.

---

# 3. Google Hacking Database (GHDB)

Google Hacking Database (GHDB) contains hundreds of carefully designed Google search queries (Google Dorks).

These queries help locate publicly exposed information.

Examples include finding:

- Login pages
- Configuration files
- Cameras
- PDFs
- Backup files
- Open directories
- Sensitive documents

Examples of Google operators

```
site:
```

```
inurl:
```

```
intitle:
```

```
filetype:
```

```
intext:
```

---

## Important Note

Google Dorks should only be used for:

- Security research
- Authorized penetration testing
- Defensive security

Never use them to access unauthorized information.

---

# 4. WHOIS Lookup

WHOIS is a protocol used to retrieve information about:

- Domain names
- IP address ownership
- Autonomous Systems (AS)
- Domain registration

---

## Information Available through WHOIS

- Domain name
- Registrar
- Registration date
- Expiration date
- Last updated
- Name servers
- Administrative contact
- Technical contact
- Organization
- Country
- Email (sometimes privacy protected)

---

## Why Attackers Use WHOIS

WHOIS information helps identify:

- Organization details
- Domain owners
- Contact information
- Registration dates
- DNS servers

This information may later assist in:

- Asset inventory
- Organization mapping
- Security assessments
- Social engineering awareness exercises

---

## WHOIS Command

```
whois example.com
```

---

# 5. DNS Footprinting

DNS Footprinting means gathering DNS-related information about a target.

DNS stores valuable information about an organization's infrastructure.

---

## DNS Footprinting Can Reveal

- Domain names
- Hostnames
- IP addresses
- Mail servers
- Name servers
- Subdomains
- DNS records

---

## Why DNS Footprinting Matters

Understanding DNS allows defenders and authorized testers to:

- Identify exposed services
- Understand infrastructure
- Validate DNS configuration
- Detect misconfigurations

---

# 6. DNS Interrogation

DNS interrogation means querying DNS servers for information.

The DNS server responds with DNS records.

---

## Common DNS Records

### A Record

Maps:

```
Domain → IPv4 Address
```

Example

```
example.com → 93.184.216.34
```

---

### AAAA Record

Maps

```
Domain → IPv6 Address
```

---

### MX Record

Mail Exchange Server

Example

```
mail.example.com
```

---

### NS Record

Name Server

Shows authoritative DNS servers.

---

### CNAME Record

Alias of another hostname.

Example

```
www.example.com

↓

example.com
```

---

### SOA Record

Start of Authority

Contains

- Primary DNS Server
- Serial Number
- Refresh Time
- Retry Time
- Expiry

---

### PTR Record

Reverse DNS

Maps

```
IP Address

↓

Hostname
```

---

# 7. DNS Interrogation Process

```
Attacker
     │
     │ DNS Query
     ▼
DNS Server
     │
     │ DNS Records
     ▼
Information Returned
```

Returned information may include

- A Record
- MX Record
- NS Record
- SOA
- CNAME
- TXT Records

---

# 8. DNS Zone Transfer

A DNS Zone Transfer copies all DNS records from one DNS server to another.

If misconfigured, an unauthorized user may obtain an entire list of DNS entries.

Properly configured servers should restrict zone transfers to authorized secondary DNS servers only.

---

# 9. Network Footprinting

Network Footprinting collects information about a target network.

Information includes

- Network range
- Live hosts
- Gateways
- Routers
- Firewalls
- Operating Systems
- Services

---

## Objectives

Determine

- Network topology
- Active hosts
- Routing paths
- IP allocation
- Device information

---

# 10. Network Range

Network range defines all IP addresses within a network.

Knowing the network range helps identify:

- Active hosts
- Internal addressing
- Network size
- Device distribution

---

# 11. Private IPv4 Address Ranges

These ranges are reserved for private networks and are **not routable on the public Internet**.

| Network | CIDR |
|----------|------|
| 10.0.0.0 – 10.255.255.255 | /8 |
| 172.16.0.0 – 172.31.255.255 | /12 |
| 192.168.0.0 – 192.168.255.255 | /16 |

---

# 12. Traceroute

Traceroute discovers the path packets take to reach a destination.

It displays

- Routers
- Gateways
- Hop count
- Delay between hops

Useful for

- Troubleshooting
- Network mapping
- Connectivity analysis

---

# 13. Information Gathering Tools in Kali Linux

## Internet Information Gathering

| Tool | Interface | Purpose |
|-------|-----------|----------|
| theHarvester | CLI | Collects emails, domains, subdomains, hostnames |
| Maltego | GUI | Relationship mapping between people, domains, organizations |
| Recon-ng | CLI | Modular OSINT framework |
| Whois | CLI | Domain registration lookup |
| Dig | CLI | DNS query utility |

---

## Social Engineering Assessment Tools

| Tool | Interface | Purpose |
|-------|-----------|----------|
| Social Engineering Toolkit (SET) | CLI | Simulates phishing and other authorized social engineering exercises |
| BeEF | GUI | Browser exploitation framework for security testing |

---

## Network Scanning Tools

| Tool | Interface | Purpose |
|-------|-----------|----------|
| Nmap | CLI | Host discovery, port scanning, OS fingerprinting |
| Zenmap | GUI | Graphical interface for Nmap |
| Netdiscover | CLI | ARP-based host discovery |
| Masscan | CLI | High-speed port scanner |
| Wireshark | GUI | Network packet analyzer |
| Ping | CLI | Checks host availability |
| ARP-scan | CLI | Discovers devices using ARP |

---

# 14. Popular DNS Tools

Examples include:

- Dig
- Host
- nslookup
- DNS Stuff
- DomainTools
- DNSWatch
- NetworkTools
- NirSoft DNS utilities

Kali Linux already includes many command-line tools, so additional installations are often unnecessary.

---

# 15. Information Collected During Footprinting

A footprinting exercise may reveal:

- Company name
- Domain names
- Subdomains
- Email addresses
- Public IP addresses
- DNS records
- Network ranges
- Mail servers
- Web servers
- Technologies
- Operating systems
- Registrar information
- DNS providers

---

# 16. Why Kali Linux?

Kali Linux includes hundreds of preinstalled security tools.

Advantages include:

- Ready-to-use environment
- Regular updates
- No need to manually install most security tools
- Large community support
- Designed for penetration testing and security assessments

---

# 17. Footprinting Workflow

```text
Target
   │
   ▼
Google Search
   │
   ▼
WHOIS
   │
   ▼
DNS Footprinting
   │
   ▼
Network Footprinting
   │
   ▼
Host Discovery
   │
   ▼
Port Scanning
   │
   ▼
Service Enumeration
```

---
