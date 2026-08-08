# Digital Forensics Tools (Kali Linux)

## Forensic Carving Tools

| Tool Name         | Interface    | Description                                                                                                            |
| ----------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **MagicRescue**   | Command Line | A file carving tool that recovers deleted files by searching for specific file type signatures.                        |
| **Scalpel**       | Command Line | A high-performance file carving tool used to recover deleted files by analyzing file headers and footers.              |
| **Scrounge-NTFS** | Command Line | A recovery tool designed to reconstruct NTFS file systems and recover files from damaged or corrupted NTFS partitions. |

---

## Forensic Imaging Tools

| Tool Name    | Interface | Description                                                                                                                                                        |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Guymager** | GUI       | A forensic imaging tool that creates exact bit-by-bit copies of digital storage devices while preserving data integrity through hashing and write-blocker support. |

---

## PDF Forensics Tools

| Tool Name      | Interface    | Description                                                                                                                                                 |
| -------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PDFiD**      | Command Line | A lightweight PDF scanning tool that detects suspicious elements such as JavaScript, embedded files, and encoded streams for quick analysis.                |
| **PDF-Parser** | Command Line | A detailed PDF forensic analysis tool that allows in-depth inspection, extraction, and analysis of PDF objects, streams, and potentially malicious content. |

---

## The Sleuth Kit (TSK) Tools

| Tool Name    | Interface    | Description                                                                                                                                       |
| ------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Autopsy**  | GUI          | A user-friendly digital forensic platform built on The Sleuth Kit that simplifies disk image analysis, file recovery, and evidence investigation. |
| **blkcat**   | Command Line | Extracts the contents of specific file system blocks from a disk image for forensic examination.                                                  |
| **blkls**    | Command Line | Retrieves unallocated file system space, helping investigators recover deleted files and analyze unused disk areas.                               |
| **blkstat**  | Command Line | Displays detailed information about specific file system blocks, including allocation status and metadata.                                        |
| **img_cat**  | Command Line | Extracts raw data directly from disk images for further forensic analysis or processing.                                                          |
| **img_stat** | Command Line | Displays metadata and statistics about a disk image, including image type, size, and layout information.                                          |
| **mactime**  | Command Line | Generates a chronological timeline of file activity based on MAC (Modification, Access, Change) timestamps to assist in forensic investigations.  |
