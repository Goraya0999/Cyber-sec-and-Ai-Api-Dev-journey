# DNS Footprinting & DNS Interrogation

>

# 1. Introduction



The goal is to gather publicly available DNS information about a target organization **without directly attacking its systems**.

Information collected through DNS footprinting can help identify:

* Domain names
* Subdomains
* Public IP addresses
* Mail servers
* Name servers
* Network infrastructure

This information helps ethical hackers understand an organization's attack surface during an authorized security assessment.

---

# 2. What is DNS?

**DNS (Domain Name System)** is often called the **phonebook of the Internet**.

Humans remember domain names like:

```text
google.com
```

Computers communicate using IP addresses like:

```text
142.250.190.14
```

DNS translates domain names into IP addresses so users can access websites without memorizing numeric addresses.

---

# 3. What is DNS Footprinting?

DNS Footprinting is the process of collecting publicly available DNS information about a target.

The collected information may include:

* Domain names
* Subdomains
* IP addresses
* Mail servers
* Name servers
* DNS records
* Network providers

Since DNS information is publicly available, gathering it is considered a form of **Passive Reconnaissance**.

---

# 4. Why Attackers Perform DNS Footprinting

Attackers use DNS footprinting to:

* Identify important servers
* Discover public IP addresses
* Find email servers
* Enumerate subdomains
* Map network infrastructure
* Prepare for later attack phases

Example:

A company may have:

```text
mail.company.com
vpn.company.com
dev.company.com
portal.company.com
```

Discovering these subdomains helps create a map of the organization's external infrastructure.

---

# 5. DNS Interrogation

## What is DNS Interrogation?

DNS interrogation is the process of sending DNS queries to a DNS server to retrieve DNS records.

The DNS server responds with publicly available information about the requested domain.

This process is completely normal and is used by:

* Browsers
* Email servers
* Network administrators
* Security professionals

---

## Information That Can Be Retrieved

DNS interrogation can reveal:

* IP addresses
* Mail servers
* Name servers
* Canonical names (Aliases)
* Domain authority
* Reverse DNS records

---

# 6. Important DNS Records

Understanding DNS records is essential for ethical hacking.

---

## A Record (Address Record)

Maps a domain name to an IPv4 address.

Example:

```text
example.com → 93.184.216.34
```

---

## AAAA Record

Maps a domain name to an IPv6 address.

Example:

```text
example.com → 2606:2800:220:1:248:1893:25c8:1946
```

---

## MX Record (Mail Exchange)

Specifies which mail server receives email for the domain.

Example:

```text
example.com

Mail Server:
mail.example.com
```

---

## NS Record (Name Server)

Identifies the authoritative DNS servers for the domain.

Example:

```text
ns1.cloudflare.com
ns2.cloudflare.com
```

---

## CNAME Record (Canonical Name)

Creates an alias for another hostname.

Example:

```text
blog.example.com

↓

hosting.example.net
```

---

## SOA Record (Start of Authority)

Contains administrative information about the DNS zone.

It includes:

* Primary DNS server
* Administrator email
* Serial number
* Refresh interval
* Retry interval
* Expiration time

---

## PTR Record (Pointer Record)

Used for reverse DNS lookup.

Instead of:

```text
Domain → IP
```

PTR performs:

```text
IP → Domain
```

---

# 7. DNS Footprinting Methodology

A typical DNS footprinting process follows these steps:

### Step 1

Identify the target domain.

Example:

```text
example.com
```

---

### Step 2

Query public DNS records.

Retrieve:

* A
* AAAA
* MX
* NS
* TXT
* CNAME
* SOA

---

### Step 3

Identify public IP addresses.

Determine which systems are internet-facing.

---

### Step 4

Identify mail infrastructure.

Locate mail servers through MX records.

---

### Step 5

Identify authoritative name servers.

Determine where DNS is hosted.

---

### Step 6

Map the external infrastructure.

Create a list of:

* Servers
* Domains
* Services
* Public hosts

---

# 8. DNS Interrogation Tools

The instructor demonstrates several DNS lookup websites.

Examples include:

* dnsstuff.com
* dnsqueries.com
* network-tools.com

These websites allow users to:

* Query DNS records
* Perform WHOIS lookups
* Retrieve IP information
* View DNS configurations

---

## Modern DNS Tools

Today, professionals commonly use:

### Linux

```bash
dig example.com
```

---

```bash
nslookup example.com
```

---

```bash
host example.com
```

---

## Online Tools

Examples include:

* DNSChecker
* MXToolbox
* ViewDNS
* SecurityTrails

These provide detailed DNS analysis through a web interface.

---

# 9. Kali Linux DNS Tools

The instructor explains that Kali Linux already includes many reconnaissance tools.

Common tools include:

| Tool     | Purpose                             |
| -------- | ----------------------------------- |
| dig      | DNS queries                         |
| nslookup | DNS lookups                         |
| host     | DNS information                     |
| dnsenum  | DNS enumeration                     |
| fierce   | DNS reconnaissance                  |
| dnsrecon | Advanced DNS enumeration            |
| Nmap     | Network discovery and DNS scripting |
| Zenmap   | GUI for Nmap                        |

---

## Example Commands

Query A Record

```bash
dig example.com
```

---

Query MX Records

```bash
dig MX example.com
```

---

Query Name Servers

```bash
dig NS example.com
```

---

Reverse Lookup

```bash
dig -x 8.8.8.8
```

---

Using nslookup

```bash
nslookup example.com
```

---

# 10. Instructor's Demonstration

The instructor demonstrates querying domains such as:

```text
microsoft.com
```

The DNS server returns information including:

* Parent DNS servers
* Public IP addresses
* DNS hierarchy
* Name servers

This demonstrates how DNS can reveal publicly available infrastructure information.

---

# 11. Modern Best Practices

Modern penetration testers typically combine multiple OSINT sources rather than relying on a single DNS lookup.

Common workflow:

1. WHOIS lookup
2. DNS enumeration
3. Subdomain discovery
4. Certificate Transparency logs
5. Public cloud asset discovery
6. Search engine reconnaissance

This provides a more complete view of the target's attack surface.

---

# 12. Incorrect or Outdated Claims in the Lecture

## Claim 1

> Kali Linux contains every required tool.

### Correction

Mostly true for many reconnaissance tasks, but professionals often install additional tools or update existing ones based on project requirements.

---

## Claim 2

Some websites demonstrated in the lecture are outdated or no longer widely used.

Modern alternatives include:

* MXToolbox
* SecurityTrails
* DNSChecker
* ViewDNS
* VirusTotal (for DNS and domain intelligence)

---

## Claim 3

The instructor suggests DNS information alone is enough for social engineering.

### Correction

DNS information is only one source of intelligence. Effective reconnaissance combines DNS data with WHOIS, metadata, search engines, public repositories, social media, and other OSINT sources.

---

# 13. Exam Notes (CEH, Security+, PNPT)

Remember the following key points:

* DNS translates domain names into IP addresses.
* DNS Footprinting is a passive reconnaissance technique.
* DNS interrogation retrieves publicly available DNS records.
* Important DNS records include:

  * A
  * AAAA
  * MX
  * NS
  * CNAME
  * SOA
  * PTR
* MX records identify mail servers.
* NS records identify authoritative DNS servers.
* SOA records contain administrative information about a DNS zone.
* Kali Linux includes several built-in DNS enumeration tools.
* DNS footprinting helps map an organization's external infrastructure before deeper security testing.

---

