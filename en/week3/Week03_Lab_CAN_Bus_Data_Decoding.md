# [Week 3] Agricultural Machinery Communication (CAN & ISOBUS) Data Analysis

## 1. Lab Overview
In this lab, we explore the principles of the **CAN Bus (ISO 11898)** and the **J1939/ISOBUS** protocols, which are central to communication between tractors and implements. We will implement a protocol decoder that directly parses raw data collected from real machines into human-readable physical values (Engine Speed, Vehicle Speed, etc.).

---

## 2. Main Objectives
- Extract **Priority, PGN, and Source Address** using bitwise operations on 29-bit CAN IDs
- Understand and implement the **Little-Endian** byte ordering scheme
- Practice applying Scale and Offset values based on specific PGNs

---

## 3. Core Concepts: J1939 ID Structure
- **Priority (3 bits)**: Message priority (0 is highest)
- **PGN (18 bits)**: Parameter Group Number (Message group ID)
- **Source Address (8 bits)**: The address of the ECU sending the message

---

## 4. Lab Instructions

### [Step 1] CAN Decoding using Python
Run the provided `step1_can_decoder.py` file to see the interpretation results of the sample logs.

```bash
# Run the code
python step1_can_decoder.py
```

### [Step 2] Data Interpretation Assignment
Try adding new data to the `logs` list in the code and answer the following:
1. Can you prove that the PGN for ID `0CF00400` is `61444` through bitwise operations?
2. Can you explain why the coolant temperature is output as 168 degrees (overheating) in terms of the offset (-40)?

---

## 5. Result Interpretation Guide
- **Success**: You can monitor the tractor's condition with just a few lines of code without a professional CAN analyzer.
- **Scalability**: By expanding the PGN table, you can consolidate the management of all machine information, including hydraulic pressure and PTO speed.

---
📌 **[Return to Discussion & Quiz Bank](../../en/QUIZ_BANK.md)**
