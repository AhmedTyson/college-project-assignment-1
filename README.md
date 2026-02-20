# <img src="https://api.iconify.design/lucide:graduation-cap.svg?color=%238A2BE2" width="32" height="32" align="center" /> College Project — Lab 01

> **Two standalone Python desktop applications demonstrating OOP and GUI development.**
> Featuring a modular Library Management System and a precision Car Loan Calculator.

<div align="center">

| Project Status | Stack                                                                                                   | Framework                                                                     | Paradigm           |
| :------------- | :------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------- | :----------------- |
| `STABLE`       | ![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white) | ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=flat-square) | `OOP Architecture` |

</div>

---

## <img src="https://api.iconify.design/lucide:list.svg?color=%238A2BE2" width="20" height="20" align="center" /> Table of Contents

- [Overview](#overview)
- [Projects](#-projects)
  - [1. Library Management System](#1-library-management-system)
  - [2. Car Loan Calculator](#2-car-loan-calculator-application)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)

---

## Overview

This repository contains two Python assignments submitted as part of a college OOP and GUI development course. Each project is self-contained, requires no external database, and demonstrates core software engineering principles: encapsulation, inheritance, input validation, and clean UI design via Python's standard Tkinter library.

---

---

## <img src="https://api.iconify.design/lucide:package.svg?color=%238A2BE2" width="20" height="20" align="center" /> Projects

### 1. Library Management System

A menu-driven application for managing a library's collection of physical books and e-books.

#### Features

| Feature               | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| **Book Management**   | Add, view, and edit book records (ID, title, author, price)               |
| **EBook Management**  | Manage e-books with extra attributes: file size, format, number of copies |
| **Total File Size**   | Computes and displays the combined size of all e-books in the catalog     |
| **Interactive Menus** | Separate console subsystems for books and e-books with clear prompts      |
| **OOP Architecture**  | `Book`, `EBook`, `Library`, and `Catalog` classes with inheritance        |

#### Class Design

```
Library
├── Book
│   ├── id, title, author, price, publisher
│   └── methods: add(), edit(), display()
└── EBook (inherits Book)
    ├── file_size, file_format, num_copies
    └── methods: compute_total_size()
```

---

### 2. Car Loan Calculator Application

A Tkinter desktop GUI that calculates monthly loan payments and total interest based on user inputs.

#### Features

| Feature                | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| **GUI Entry Fields**   | Car price, down payment, loan term, and job title inputs       |
| **Auto Interest Rate** | Applies the correct interest rate based on selected loan term  |
| **Monthly Payment**    | Computes and displays the exact monthly installment            |
| **Total Cost Summary** | Shows total repayment amount and total interest paid           |
| **Input Validation**   | Ensures all fields are complete and numeric before calculating |
| **Logo Display**       | Renders a car logo image in the GUI if available               |

#### Loan Calculation Formula

```
Monthly Payment = P × [r(1+r)^n] / [(1+r)^n - 1]

Where:
  P = Principal (car price - down payment)
  r = Monthly interest rate (annual rate / 12)
  n = Number of monthly payments (loan term in years × 12)
```

---

---

## <img src="https://api.iconify.design/lucide:cpu.svg?color=%238A2BE2" width="20" height="20" align="center" /> Tech Stack

| Layer             | Technology                  |
| ----------------- | --------------------------- |
| **Language**      | Python 3.x                  |
| **GUI Framework** | Tkinter (Standard Library)  |
| **Paradigm**      | Object-Oriented Programming |
| **Data Storage**  | In-memory (no external DB)  |

---

---

## <img src="https://api.iconify.design/lucide:rocket.svg?color=%238A2BE2" width="20" height="20" align="center" /> Getting Started

### Prerequisites

- Python 3.x installed ([Download](https://www.python.org/downloads/))
- Tkinter is included with the standard Python installation — no pip install needed

### Run the Library Management System

```bash
# Clone the repository
git clone https://github.com/AhmedTyson/college-project-assignment-1.git

# Navigate to the Library Management System
cd "college-project-assignment-1/Library Management System"

# Run the application
python Sierra_ILS.py
```

### Run the Car Loan Calculator

```bash
# Navigate to the Car Loan Calculator
cd "college-project-assignment-1/Car Loan Calculator Application"

# Run the application
python GUI_Car_App.py
```

---

---

## <img src="https://api.iconify.design/lucide:folder-tree.svg?color=%238A2BE2" width="20" height="20" align="center" /> Project Structure

```
college-project-assignment-1/
├── Library Management System/
│   ├── Sierra_ILS.py          # Main OOP library management console app
│   ├── README.md              # Project-specific instructions
│   └── screenshot.png         # UI preview
│
└── Car Loan Calculator Application/
    ├── GUI_Car_App.py         # Tkinter GUI car loan calculator
    ├── README.md              # Project-specific instructions
    └── screenshot.png         # UI preview
```
