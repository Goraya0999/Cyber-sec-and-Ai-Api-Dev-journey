# Sniffing and Spoofing with Kali Linux


## What is Network Traffic?

Network traffic is the flow of data between devices connected to a network.

### Visual

```text
Computer A
     │
     │ Data Packets
     ▼
Network
     ▼
Computer B
```

---

# Sniffing

## Definition

Sniffing is the process of capturing and analyzing network traffic.

Ethical hackers use sniffing to:

- Monitor network traffic.
- Find security weaknesses.
- Detect unencrypted sensitive data.
- Analyze communication between devices.

---

## Sniffing Process

```text
Network Traffic
       │
       ▼
Sniffing Tool
       │
       ▼
Capture Packets
       │
       ▼
Analyze Data
       │
       ▼
Find Vulnerabilities
```

---

# Why Attackers Use Sniffing

Attackers use sniffing to:

- Capture usernames.
- Capture passwords.
- Steal session cookies.
- Read unencrypted communications.
- Monitor network activity.

---

# Why Ethical Hackers Use Sniffing

Ethical hackers use sniffing to:

- Assess network security.
- Detect insecure protocols.
- Monitor suspicious traffic.
- Find data leaks.
- Improve network protection.

---

# Types of Sniffing

```text
Sniffing
│
├── Passive Sniffing
└── Active Sniffing
```

---

# Passive Sniffing

## Definition

Passive sniffing captures network traffic **without changing or interacting** with the network.

The attacker only listens.

---

## Works Best On

- Shared networks
- Hub-based networks

---

## Visual

```text
Computer A
      │
      ▼
 Hub
 ├──────────► Computer B
 ├──────────► Computer C
 └──────────► Sniffer
```

Every connected device receives the packets.

---

## Characteristics

- Does not modify traffic.
- Difficult to detect.
- Only observes communication.
- Cannot redirect packets.

---

## Uses

- Monitor network traffic.
- Troubleshoot network problems.
- Analyze protocols.
- Detect anomalies.

---

# Active Sniffing

## Definition

Active sniffing captures traffic by manipulating the network.

The attacker injects packets to redirect traffic.

---

## Works Best On

- Switched networks

---

## Visual

```text
Computer A
      │
      ▼
 Switch
      │
      ▼
Computer B

        ▲
        │
 Active Sniffer
 (Redirects Traffic)
```

---

## Techniques Used

- ARP Spoofing
- MAC Flooding

---

## Characteristics

- Modifies network traffic.
- More powerful.
- Easier to detect.
- Used in penetration testing.

---

# Passive vs Active Sniffing

| Feature | Passive Sniffing | Active Sniffing |
|----------|-----------------|-----------------|
| Interacts with network | ❌ No | ✅ Yes |
| Injects packets | ❌ No | ✅ Yes |
| Detectability | Low | Higher |
| Traffic manipulation | ❌ No | ✅ Yes |
| Common network | Hub | Switch |
| Main purpose | Monitor traffic | Redirect and capture traffic |

---

# When to Use Passive Sniffing

Used for:

- Network monitoring
- Traffic analysis
- Detecting anomalies
- Performance troubleshooting

---

# When to Use Active Sniffing

Used for:

- Penetration testing
- Security assessment
- Finding hidden vulnerabilities
- Simulating real attacks

---

# Spoofing

## Definition

Spoofing is pretending to be another device, user, or system.

The attacker changes identity information to appear trusted.

---

## Visual

```text
Attacker

Pretends to be

Trusted Device

↓

Victim Trusts Fake Device
```

---

# Why Attackers Use Spoofing

Attackers use spoofing to:

- Bypass security.
- Perform phishing attacks.
- Steal information.
- Redirect users.
- Launch attacks.

---

# Why Ethical Hackers Use Spoofing

Ethical hackers use spoofing to:

- Test authentication.
- Simulate attacks.
- Evaluate security.
- Find trust-related weaknesses.

---

# Types of Spoofing

```text
Spoofing
│
├── IP Spoofing
├── MAC Spoofing
└── DNS Spoofing
```

---

# IP Spoofing

## Definition

The attacker changes the source IP address of a packet.

The packet appears to come from a trusted device.

---

## Visual

```text
Original

Packet
IP = 192.168.1.10

↓

Fake Packet

IP = Trusted Server
```

---

## Uses

- Bypass security
- Hide identity
- Launch DoS attacks
- Access trusted systems

---

# MAC Spoofing

## Definition

Changes the device's MAC address.

The attacker copies another device's MAC address.

---

## Visual

```text
Original MAC

AA:BB:CC:11:22:33

↓

Changed To

11:22:33:44:55:66
```

---

## Uses

- Bypass MAC filtering
- Gain network access
- Impersonate devices

---

# DNS Spoofing

## Definition

Also called **DNS Cache Poisoning**.

The attacker changes DNS responses so users visit fake websites.

---

## Visual

```text
User

www.bank.com

↓

DNS Server

↓

Fake IP Address

↓

Fake Website
```

---

## Uses

- Phishing
- Credential theft
- Fake login pages

---

# Man-in-the-Middle (MITM)

## Definition

The attacker secretly sits between two communicating devices.

The attacker can:

- Read traffic.
- Modify traffic.
- Record information.

---

## Visual

```text
User
   │
   ▼
Attacker
   │
   ▼
Server
```

The user believes they are communicating directly with the server.

---

## MITM Activities

An attacker may:

- Read messages.
- Change messages.
- Capture passwords.
- Steal cookies.
- Hijack sessions.

---

# Why Ethical Hackers Simulate MITM

- Test encryption.
- Verify secure communication.
- Detect protocol weaknesses.
- Improve network security.

---

# Kali Linux Sniffing Tools

| Tool | Interface | Purpose |
|------|-----------|---------|
| **Wireshark** | GUI | Captures and analyzes network packets with a graphical interface. |
| **tcpdump** | Command Line | Lightweight packet capture tool for terminals and servers. |
| **Ettercap** | GUI / Command Line | Network sniffer that also supports MITM attacks and protocol analysis. |

---

# Wireshark

## Purpose

Network packet analyzer.

### Features

- Packet capture
- Protocol analysis
- Traffic inspection
- Filtering
- Troubleshooting

---

## Visual

```text
Network

↓

Wireshark

↓

Captured Packets

↓

Protocol Analysis
```

---

# tcpdump

## Purpose

Command-line packet capture tool.

### Features

- Fast
- Lightweight
- Terminal based
- Works on remote servers

---

## Visual

```text
Network

↓

tcpdump

↓

Packet Capture

↓

Terminal Output
```

---

# Ettercap

## Purpose

Sniffing and MITM testing tool.

### Features

- Packet capture
- ARP poisoning
- MITM testing
- Protocol analysis

---

# Kali Linux Spoofing Tools

| Tool | Interface | Purpose |
|------|-----------|---------|
| **ARPspoof** | Command Line | Performs ARP spoofing attacks for MITM testing. |
| **Bettercap** | Command Line | Advanced framework for network monitoring, spoofing, MITM attacks, and packet manipulation. |
| **DNSspoof** | Command Line | Performs DNS spoofing by sending fake DNS responses to redirect users. |

---

# ARPspoof

## Purpose

Performs ARP spoofing attacks.

### Process

```text
Victim

↓

Fake ARP Reply

↓

Victim Updates ARP Table

↓

Traffic Redirected
```

---

# Bettercap

## Purpose

Advanced network attack framework.

### Features

- ARP spoofing
- DNS spoofing
- HTTPS interception
- Packet sniffing
- Network discovery

---

# DNSspoof

## Purpose

Redirects users to fake websites by sending fake DNS replies.

### Visual

```text
Victim

↓

DNS Request

↓

Fake DNS Reply

↓

Fake Website
```

---

# Complete Sniffing Workflow

```text
Network Traffic

↓

Capture Packets

↓

Analyze Packets

↓

Identify Sensitive Data

↓

Find Vulnerabilities

↓

Improve Security
```

---

# Complete Spoofing Workflow

```text
Choose Identity

↓

Fake Identity

↓

Send Fake Packets

↓

Victim Trusts Sender

↓

Traffic Redirected

↓

Security Assessment
```

---

# Comparison of Sniffing and Spoofing

| Feature | Sniffing | Spoofing |
|----------|----------|----------|
| Purpose | Capture traffic | Fake identity |
| Modifies traffic | Sometimes | Yes |
| Captures packets | Yes | No |
| Impersonates devices | No | Yes |
| Used in MITM | Yes | Yes |
| Ethical use | Security monitoring | Security testing |

---

# Kali Linux Tools Summary

| Category | Tools |
|----------|------|
| Packet Analysis | Wireshark |
| Packet Capture | tcpdump |
| Sniffing & MITM | Ettercap |
| ARP Spoofing | ARPspoof |
| Advanced MITM | Bettercap |
| DNS Spoofing | DNSspoof |

---

# Complete Attack Simulation

```text
Reconnaissance
      │
      ▼
Network Discovery
      │
      ▼
Packet Sniffing
      │
      ▼
Traffic Analysis
      │
      ▼
Spoofing
      │
      ▼
MITM Simulation
      │
      ▼
Security Assessment
      │
      ▼
Report Vulnerabilities
```
