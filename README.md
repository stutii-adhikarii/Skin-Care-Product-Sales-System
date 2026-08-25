# 💆‍♀️ WeCare: Skin Care Product Sales System

### A Command-Line Inventory & Billing Tool for Skin Care Retailers

WeCare is a Python-based command-line system built to manage day-to-day operations for a skin care store which includes selling products to customers, restocking from suppliers, and keeping stock levels accurate, all through a simple menu-driven interface.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-informational?style=for-the-badge)
![File--Based](https://img.shields.io/badge/Storage-File--Based-yellow?style=for-the-badge)

---

## 📌 Overview

WeCare gives a store admin a straightforward menu to run the shop's daily transactions: sell items to a customer, restock items from a supplier, or exit the system. Every transaction reads and writes product data from a text file, so stock counts stay up to date, and each sale or restock generates its own invoice.

---

## ⚙️ Features

- 🛒 Sell products to customers with live stock validation
- 📦 Restock products from suppliers and update inventory
- 🎁 Automatic "buy more, get one free" discount logic on sales
- 🧾 Auto-generated invoices for both sales and purchases
- ✅ Input validation for names, phone numbers, and quantities
- ⚠️ Error handling for invalid entries and stock shortages
- 💾 Persistent storage via a product data file 

---

## 🛠️ Tech Stack

| Language | Tools              |
| -------- | ------------------ |
| Python 3 | Visual Studio Code |
|          | Git                |
|          | GitHub             |

---

## 📂 Project Structure

```
Skin-Care-Product-Sales-System/
│
├── main.py          # Entry point — displays the menu and routes user choices
├── operation.py      # Core logic for selling and restocking products
├── read.py           # Reads and displays product data
├── write.py           # Rewrites product data and creates invoices
├── store.txt          # Product inventory data file
│
└── README.md
```

---

## ▶️ How It Works

1. Run `main.py` to launch the system
2. Choose an option from the menu:
   - **1** — Sell products to a customer
   - **2** — Restock products from a supplier
   - **3** — Exit the system
3. Follow the prompts to enter customer/supplier details and product IDs
4. Stock is updated automatically and an invoice is generated for the transaction

---

## 📚 What I Learned

Working on this project helped strengthen my understanding of:

- File handling and persistent data storage in Python
- Structuring a project across multiple modules (separating logic, I/O, and entry point)
- Input validation and exception handling
- Building real-world business logic (stock deduction, pricing, discount rules)
- Writing clear docstrings and inline documentation

---

## 🚀 Future Improvements

- Migrate storage from a text file to a proper database
- Add a graphical or web-based interface
- Generate downloadable/printable invoice files
- Add login/authentication for different admin roles
- Sales history and reporting dashboard

---

### ⭐ If you found this project useful, consider giving it a star!
