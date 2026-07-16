# Notify - Take Your Notes

A simple, fast, and asynchronous web application to create, store, and view your notes. Built using Python's **FastAPI** framework, styled with **Bootstrap 5**, and powered by a cloud-hosted **MongoDB Atlas** database.

## Features

- **Asynchronous Architecture:** Fast and lightweight operation powered by FastAPI.
- **Dynamic Frontend:** Server-side rendering using Jinja2 templates.
- **Responsive Design:** Beautiful, mobile-friendly interface built with Bootstrap 5.
- **NoSQL Database:** Persistent cloud storage using MongoDB via PyMongo.

## Tech Stack

- **Backend:** FastAPI, Uvicorn, Jinja2, PyMongo, python-multipart
- **Frontend:** HTML5, Bootstrap 5

## Project Structure

```text
├── main.py            # Main application script with routes
├── static/            # Static assets (CSS, JS, Images)
├── templates/         # Jinja2 HTML templates
│   └── index.html     # Main user interface
└── .gitignore         # Prevents committing virtual environments
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- A MongoDB Atlas account and cluster URI string

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd fastapi-notes-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install fastapi uvicorn pymongo python-multipart jinja2
   ```

4. **Database Configuration:**
   Open `main.py` and replace the `MongoClient` string with your personal connection details if necessary:
   ```python
   conn = MongoClient("your-mongodb-connection-string")
   ```

### Running the Application

Start the local development server using Uvicorn:

```bash
uvicorn main:app --reload
```

Open your browser and navigate to **`http://127.0.0.1:8000`** to start saving notes!
