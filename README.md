# Airline Management System

## Overview
The **Airline Management System** is a web application designed to manage airline operations, bookings, and related activities. It uses Python and Flask as the backend framework and includes a SQLite database for data storage.

## Features
- User authentication and management.
- Flight booking and cancellation functionality.
- Dashboard for airline administrators.
- Responsive front-end using HTML templates.

## Project Structure
```
Airline-Management-System/
├── static/         # Static assets (CSS, JavaScript, images)
├── templates/      # HTML templates for the web application
├── instance/       # Configuration files and sensitive data
├── airline.db      # SQLite database file
├── app.py          # Main Python application file
├── venv/           # Python virtual environment
```

## Prerequisites
- Python 3.x installed on your system.
- A package manager like `pip` to install dependencies.

## Setup Instructions
1. Clone the repository or download the source code.
2. Navigate to the project directory:
   ```bash
   cd Airline-Management-System
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Usage
1. Open a web browser and go to `http://127.0.0.1:5000` to access the application.
2. Use the provided login credentials or create a new account to start managing flights and bookings.

## Database
The project uses an SQLite database (`airline.db`). You can use tools like DB Browser for SQLite to view or modify the database.

## Contributing
Contributions are welcome! Please create a pull request with your proposed changes.

## License
This project is licensed under the MIT License.
