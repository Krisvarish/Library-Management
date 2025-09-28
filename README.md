# 📚 Library Management System

A simple **Library Management System** built with Python and Flask.  
It allows students, teachers, and librarians to log in, manage books, and track borrowing activity.

---

## 🚀 Features

- 👩‍🎓 **Student Login** – Access available books and borrowing records.  
- 👨‍🏫 **Teacher Login** – Manage assigned books and borrowing details.  
- 📖 **Librarian Login** – Add, update, and remove books.  
- 🗄 **CSV Storage** – Books, students, and teachers are stored in `.csv` files.  
- 🌐 **Flask Web Interface** – User-friendly HTML templates with a simple frontend.  

---

## 📂 Project Structure

```
Library-Management/
│── Book.csv                  # Book records
│── demostu.csv               # Student records
│── teach.csv                 # Teacher records
│── main.py                   # Entry point for the application
│── module.py                 # Core library management functions
│
├── website/                  # Flask web app
│   ├── __init__.py           # Flask app initialization
│   ├── auth.py               # Authentication routes
│   ├── views.py              # Main routes
│   │
│   ├── static/               # Static files (JS, images)
│   │   ├── index.js
│   │   ├── libpic.jpg
│   │   └── logo.png
│   │
│   ├── templates/            # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── library.html
│   │   ├── student_login.html
│   │   ├── teacher_login.html
│   │   ├── librarian_login.html
│   │   └── ... (other UI templates)
│
└── __pycache__/              # Compiled cache files
```

---

## ⚙️ Installation & Setup

1. **Clone or Extract the Project**
   ```bash
   git clone https://github.com/Krisvarish/Library-Management
   cd Library-Management
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install flask
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🔑 Default Logins

Check the CSV files for existing users:  
- **Students:** `demostu.csv`  
- **Teachers:** `teach.csv`  
- **Books:** `Book.csv`  

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask**
- **HTML, CSS, JavaScript**
- **CSV for storage**

---

## 📌 Future Improvements

- Switch from CSV to a proper database (SQLite / PostgreSQL).  
- Add book search and filtering.  
- Improve authentication with password hashing.  
- Add borrowing deadlines and penalties system.  
