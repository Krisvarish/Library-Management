# Library Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![CSV](https://img.shields.io/badge/Data-CSV-green.svg)](https://docs.python.org/3/library/csv.html)
[![OOP](https://img.shields.io/badge/Programming-OOP-orange.svg)](https://docs.python.org/3/tutorial/classes.html)

A comprehensive Library Management System built with Python that streamlines library operations through efficient book management, user registration, and borrowing/returning processes. This project utilizes Object-Oriented Programming (OOP) principles to simulate real-world library operations including adding books, registering users, borrowing and returning books, and searching for books by their title.

## 🌟 Features

- **Book Management**: Add, remove, update, and search books in the library inventory
- **User Registration**: Register new library members and manage user accounts
- **Borrowing System**: Issue books to registered users with tracking capabilities
- **Return Processing**: Handle book returns and update availability status
- **Search Functionality**: Find books by title, author, or other attributes
- **Data Persistence**: Store all data in CSV files for easy management
- **Modular Design**: Clean, maintainable code structure using OOP principles
- **Web Interface**: Optional web-based interface for enhanced user experience

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
CSV module (built-in)
Standard Python libraries
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Krisvarish/Library-Management.git
   cd Library-Management
   ```

2. **Install Python** (if not already installed)
   ```bash
   # Ensure Python 3.8+ is installed
   python --version
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
Library-Management/
├── __pycache__/                # Python bytecode cache
├── website/                    # Web interface files
├── Book.csv                    # Books database
├── README.md                   # Project documentation
├── demostu.csv                # Demo student/user data
├── main.py                     # Main application entry point
├── module.py                   # Core library management modules
└── teach.csv                   # Teacher/staff data
```

## 🛠️ Usage

### Running the Main Application

```bash
python main.py
```

### Core Functionality

#### 1. **Book Management**
```python
# Add a new book to the library
add_book("Title", "Author", "ISBN", "Category", quantity)

# Remove a book from inventory
remove_book("ISBN")

# Update book information
update_book("ISBN", new_details)
```

#### 2. **User Management**
```python
# Register a new user
register_user("Name", "Email", "Phone", "Address")

# Search for users
search_user("criteria")
```

#### 3. **Borrowing Operations**
```python
# Issue a book to a user
issue_book("user_id", "book_isbn")

# Return a borrowed book
return_book("user_id", "book_isbn")

# Check user's borrowed books
view_borrowed_books("user_id")
```

### Data Files

The system uses CSV files for data storage:

- **Book.csv**: Contains all book information (Title, Author, ISBN, Availability, etc.)
- **demostu.csv**: Student user accounts and details
- **teach.csv**: Teacher/staff accounts and permissions

## 🏗️ System Architecture

### Core Components

1. **Main Module (`main.py`)**
   - Application entry point
   - User interface coordination
   - System initialization

2. **Library Module (`module.py`)**
   - Core library operations
   - Data management functions
   - Business logic implementation

3. **Data Layer (CSV Files)**
   - Persistent data storage
   - Easy data import/export
   - Human-readable format

4. **Web Interface (`website/`)**
   - Optional web-based access
   - Enhanced user experience
   - Remote library management

### Object-Oriented Design

The system follows OOP principles with classes for:
- **Book**: Represents individual books with properties and methods
- **User**: Manages user accounts and borrowing history
- **Library**: Central system coordination and operations
- **Transaction**: Handles borrowing/returning operations

## 📊 Features & Capabilities

### Book Operations
- ✅ Add new books to inventory
- ✅ Remove books from system
- ✅ Update book information
- ✅ Search books by multiple criteria
- ✅ Check book availability
- ✅ Generate book reports

### User Management
- ✅ Register new library members
- ✅ Update user information
- ✅ Track user borrowing history
- ✅ Manage user permissions
- ✅ Generate user reports

### Transaction Management
- ✅ Issue books to registered users
- ✅ Process book returns
- ✅ Calculate due dates
- ✅ Track overdue books
- ✅ Generate transaction reports

## 💻 Technical Details

### Data Storage Format

**Books (Book.csv)**
```csv
ISBN,Title,Author,Category,Quantity,Available,Publisher,Year
```

**Users (demostu.csv / teach.csv)**
```csv
UserID,Name,Email,Phone,Address,MembershipDate,Status
```

### Key Functions

```python
class Library:
    def add_book(self, book_details)
    def remove_book(self, isbn)
    def search_book(self, criteria)
    def issue_book(self, user_id, isbn)
    def return_book(self, user_id, isbn)
    def generate_report(self, report_type)
```

## 🎯 Use Cases

- **Academic Libraries**: Manage textbooks, research materials, and student accounts
- **Public Libraries**: Handle community book lending and member management
- **School Libraries**: Track educational resources and student borrowing
- **Personal Collections**: Organize and lend personal book collections
- **Small Organizations**: Manage internal resource libraries

## 🔧 Configuration

### CSV File Setup

Ensure your CSV files have the correct headers:

```python
# Book.csv headers
BOOK_HEADERS = ['ISBN', 'Title', 'Author', 'Category', 'Quantity', 'Available']

# User CSV headers  
USER_HEADERS = ['UserID', 'Name', 'Email', 'Phone', 'Address', 'Status']
```

### System Settings

Modify `module.py` to customize:
- Maximum books per user
- Loan duration periods
- Fine calculations
- User categories and permissions

## 🤝 Contributing

We welcome contributions to enhance the Library Management System!

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Areas for Improvement

- **Database Integration**: Migrate from CSV to SQL database
- **GUI Development**: Create desktop application interface
- **Advanced Search**: Implement fuzzy search and filters
- **Reporting System**: Generate detailed analytics and reports
- **Fine Management**: Automated overdue fine calculations
- **Reservation System**: Allow users to reserve books
- **Digital Integration**: Support for e-books and digital resources

## 🔮 Future Enhancements

- **Web Dashboard**: Complete web-based management interface
- **Mobile App**: iOS and Android applications
- **Barcode Scanner**: Integration with barcode scanning for books
- **Email Notifications**: Automated reminders for due dates
- **Multi-location Support**: Manage multiple library branches
- **API Development**: RESTful API for third-party integrations
- **Cloud Storage**: Migration to cloud-based data storage

## 📈 Performance

The system is optimized for:
- **Small to Medium Libraries**: Up to 10,000 books and 1,000 users
- **Fast Search Operations**: Efficient CSV parsing and searching
- **Low Resource Usage**: Minimal system requirements
- **Data Integrity**: Robust error handling and data validation

## 🔧 Troubleshooting

### Common Issues

1. **CSV File Not Found**
   ```python
   # Ensure CSV files exist in the project directory
   # Create empty CSV files with proper headers if missing
   ```

2. **Permission Errors**
   ```bash
   # Check file permissions
   chmod 644 *.csv
   ```

3. **Import Errors**
   ```python
   # Verify all required modules are available
   import csv, os, sys
   ```

## 📝 Example Usage

```python
# Initialize the library system
library = Library()

# Add a new book
library.add_book({
    'isbn': '978-0123456789',
    'title': 'Python Programming',
    'author': 'John Doe',
    'category': 'Technology',
    'quantity': 5
})

# Register a new user
library.register_user({
    'name': 'Alice Johnson',
    'email': 'alice@example.com',
    'phone': '123-456-7890',
    'address': '123 Main St'
})

# Issue a book
library.issue_book('user123', '978-0123456789')

# Return a book
library.return_book('user123', '978-0123456789')
```

## 👥 Author

- **Krisvarish** - *Initial work* - [@Krisvarish](https://github.com/Krisvarish)

## 🙏 Acknowledgments

- Python community for excellent documentation and libraries
- Open-source contributors for inspiration and best practices
- Library science professionals for domain knowledge
- Educational institutions for use case validation

## 📞 Contact

For questions, suggestions, or collaboration opportunities:
- GitHub: [@Krisvarish](https://github.com/Krisvarish)
- Project Link: [https://github.com/Krisvarish/Library-Management](https://github.com/Krisvarish/Library-Management)

---

*Making library management simple, efficient, and accessible* 📚✨
