# OS Fingerprinting and Traceroute (Kali Linux)



# Information Gathered Before OS Fingerprinting

Before identifying the operating system, ethical hackers usually collect:

* IP Address
* Network Range
* Domain Name
* DNS Records
* Server Names
* Whois Information

```
Reconnaissance
      │
      ▼
+-------------------+
| Whois Information |
+-------------------+
      │
      ▼
+-------------------+
| DNS Lookup        |
+-------------------+
      │
      ▼
+-------------------+
| IP Address        |
+-------------------+
      │
      ▼
+-------------------+
| OS Fingerprinting |
+-------------------+
```

---

# OS Fingerprinting

## Definition

OS Fingerprinting is the process of identifying the **Operating System** running on a target computer or server.

Examples:

* Windows
* Linux
* Ubuntu
* Debian
* CentOS
* Unix
* FreeBSD

---

## Why OS Fingerprinting?

Knowing the operating system helps an ethical hacker:

* Find suitable vulnerabilities
* Select compatible exploits
* Identify available services
* Plan penetration testing

Example:

```
Target
   │
   ▼
Linux Server
   │
   ▼
Search Linux Vulnerabilities
```

Instead of testing Windows exploits on Linux, the attacker only searches Linux vulnerabilities.

---

# Methods of OS Fingerprinting

## 1. Active Fingerprinting

The tester sends packets directly to the target.

```
Attacker
    │
    │ Sends Packets
    ▼
Target Server
    │
    ▼
Response Analysis
```

Advantages

* More accurate
* More detailed

Disadvantages

* Easier to detect

---

## 2. Passive Fingerprinting

The tester only observes network traffic.

```
Network Traffic
      │
      ▼
Packet Capture
      │
      ▼
Operating System Guess
```

Advantages

* Very stealthy
* Difficult to detect

Disadvantages

* Less information

---

# Common OS Fingerprinting Tools

| Tool     | Purpose                              |
| -------- | ------------------------------------ |
| Nmap     | Detect operating system and services |
| Zenmap   | GUI version of Nmap                  |
| Netcraft | Website technology lookup            |
| Shodan   | Search internet-connected devices    |

---

# Nmap

## Purpose

* Detect Operating System
* Port Scanning
* Service Detection
* Version Detection

Example

```
Target
   │
   ▼
Nmap Scan
   │
   ▼
Linux
Apache
SSH
FTP
```

---

# Zenmap

## Purpose

GUI version of Nmap.

Useful for beginners.

```
Nmap
(Command Line)

      OR

Zenmap
(Graphical Interface)
```

---

# Netcraft

## Purpose

Netcraft is an online service that provides information about websites.

It can display:

* Hosting provider
* Operating system
* Web server
* Domain information
* First seen date

Example

```
Website
     │
     ▼
Netcraft
     │
     ├── Linux
     ├── Apache
     ├── Hosting Provider
     └── Domain Details
```

---

# Shodan

## Definition

Shodan is a search engine for Internet-connected devices.

Unlike Google, it indexes:

* Servers
* Routers
* Cameras
* IoT Devices
* Firewalls
* Databases

```
Internet
      │
      ▼
Shodan Database
      │
      ▼
Search Device
```

---

# What Can Shodan Show?

* Open Ports
* Running Services
* Server Banners
* Geographic Location
* Organization
* Operating System
* IP Address

---

# Example

Searching for Microsoft may show:

* HTTPS Services
* Running Servers
* Countries
* Public Services

If no vulnerable ports appear, it generally indicates a well-secured public infrastructure.

---

# Open Ports

An open port means a service is listening.

Example

```
Port 80
HTTP

Port 22
SSH

Port 21
FTP

Port 443
HTTPS
```

Open ports provide more information about the target.

---

# Traceroute

## Definition

Traceroute is a network diagnostic tool that shows the path packets travel from the source to the destination.

It also displays:

* Routers
* Intermediate devices
* Response time
* Network path

---

# Visual Representation

```
Your PC
   │
   ▼
Router 1
   │
   ▼
Router 2
   │
   ▼
Firewall
   │
   ▼
ISP Router
   │
   ▼
Target Server
```

Traceroute discovers every hop.

---

# What is a Hop?

Every router between source and destination is called a **Hop**.

Example

```
PC
 │
 ▼
Router A  ← Hop 1
 │
 ▼
Router B  ← Hop 2
 │
 ▼
Router C  ← Hop 3
 │
 ▼
Google
```

---

# Protocol Used

Traceroute mainly uses:

* ICMP
* TTL (Time To Live)

---

# What is TTL?

TTL means **Time To Live**.

TTL limits how long a packet can travel.

Every router decreases TTL by **1**.

---

# TTL Example

Packet starts with

```
TTL = 4
```

Travel

```
PC

TTL=4
   │

Router1

TTL=3
   │

Router2

TTL=2
   │

Router3

TTL=1
   │

Router4

TTL=0
```

Packet is discarded.

Router sends an ICMP reply.

---

# How Traceroute Works

## Step 1

Traceroute sends packet

```
TTL = 1
```

```
PC
 │
 ▼
Router1
```

TTL becomes zero.

Router replies.

Traceroute records:

* IP Address
* Response Time

---

## Step 2

Traceroute sends

```
TTL = 2
```

```
PC
 │
 ▼
Router1
 │
 ▼
Router2
```

Router2 drops the packet.

Reply is recorded.

---

## Step 3

Traceroute sends

```
TTL = 3
```

Packet reaches Router3.

Same process continues.

---

## Final Step

Eventually

```
TTL Large Enough
```

Packet reaches destination.

Target replies with ICMP response.

---

# Information Obtained from Traceroute

Traceroute can reveal:

* Router IP Addresses
* Number of Hops
* Response Time
* DNS Names
* Network Path
* Approximate Geographic Route

---

# Example Output

```
Hop 1
192.168.1.1
2 ms

Hop 2
10.10.0.1
8 ms

Hop 3
203.0.113.5
15 ms

Hop 4
Request Timed Out

Hop 5
216.239.36.10
25 ms
```

---

# Request Timed Out

This usually means:

* Firewall blocked ICMP
* Router ignored packet
* Device does not respond
* Packet expired

It does **not** always mean the device is offline.

---

# Response Time

Traceroute measures:

```
Packet Sent
      │
      ▼
Router
      │
      ▼
Reply
```

Time is displayed in milliseconds (ms).

Example

```
2 ms
10 ms
24 ms
35 ms
```

Lower values generally indicate faster communication.

---

# Why Ethical Hackers Use Traceroute

* Discover routers
* Find firewalls
* Identify gateways
* Map network topology
* Identify bottlenecks
* Understand packet paths

---

# Network Topology Example

```
                Internet
                    │
                    ▼
            ISP Router
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
 Firewall                    VPN Gateway
      │                           │
      ▼                           ▼
 Internal Router            DMZ Server
      │
      ▼
 Target Server
```

Traceroute helps reveal this path.

---

# Advantages of Traceroute

* Maps network paths
* Finds intermediate devices
* Measures latency
* Helps troubleshoot routing issues
* Useful during reconnaissance

---

# Limitations

* Some routers block ICMP
* Firewalls may hide devices
* Results may be incomplete
* Dynamic routing can change paths
* Not all devices reply

---

# OS Fingerprinting Workflow

```
Whois
   │
   ▼
DNS Lookup
   │
   ▼
IP Address
   │
   ▼
OS Fingerprinting
   │
   ▼
Port Scanning
   │
   ▼
Service Detection
   │
   ▼
Vulnerability Assessment
```

---

# Important Terms

| Term                   | Meaning                                              |
| ---------------------- | ---------------------------------------------------- |
| OS Fingerprinting      | Identifying the operating system of a target         |
| Active Fingerprinting  | Sending packets to detect OS                         |
| Passive Fingerprinting | Observing traffic without sending packets            |
| Hop                    | Each router between source and destination           |
| TTL                    | Time To Live value in an IP packet                   |
| ICMP                   | Internet Control Message Protocol                    |
| Traceroute             | Shows the route packets travel                       |
| Nmap                   | Network scanning and OS detection tool               |
| Zenmap                 | GUI version of Nmap                                  |
| Netcraft               | Online website technology lookup service             |
| Shodan                 | Search engine for Internet-connected devices         |
| Open Port              | A port where a service is actively listening         |
| Response Time          | Time taken for a packet to reach a device and return |
