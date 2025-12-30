# Inventory Management System

A **Python console application** designed to manage product inventory. This project allows users to **add, view, update, and remove items** while demonstrating core programming concepts such as **Object-Oriented Programming (OOP)**, **data structures**, and **file handling**.

---

## 📦 Project Overview

The Inventory Management System is a menu-driven CLI application that helps manage a collection of products. It supports persistent storage using a text file and applies clean modular design principles for maintainability and clarity.

---

## 🚀 How to Run the Program

1. Ensure you have **Python 3.x** installed on your system.
2. Download or clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the program using the command below:

```bash
python main.py
```

---

## ✅ Features Implemented

- **Data Structures**
  - Dictionaries for inventory storage
  - Lists for product categories
  - Tuples for immutable brand names
  - Sets for tracking unique product IDs

- **User Interaction**
  - Menu-driven interface using loops and conditional statements
  - Options include: Add, View, Update, and Remove products

- **CRUD Operations**
  - Modular functions for **Create**, **Read**, **Update**, and **Delete** operations

- **Object-Oriented Programming (OOP)**
  - `Product` class encapsulates product data and behavior
  - `PerishableProduct` subclass demonstrates inheritance with expiration date handling

- **File Persistence**
  - Inventory data is automatically loaded from a text file at startup
  - Data is saved back to the file upon program exit

---

## ⚠️ Limitations / Known Issues

- **Search Restriction**  
  Products can only be updated or removed using their exact **Product ID**. Searching by product name is not currently supported.

- **Data Formatting**  
  Inventory data is stored in a comma-separated text file. If a product name or brand contains commas, it may cause parsing issues when loading data.

- **Single User Design**  
  The system is intended for single-user use and does not support concurrent file access.

- **Interface**  
  This is a **console-only application (CLI)** and does not include a graphical user interface (GUI).

---

## 🛠️ Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- File I/O
- Built-in Data Structures

---

## 📄 License

This project is intended for **educational purposes** as part of coursework and does not include a commercial license.

---

Feel free to improve or extend the system by adding search functionality, improving file storage (e.g., JSON), or building a GUI.

