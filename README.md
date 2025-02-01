# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and setup instructions for PyCharm.

## Technologies Used

- **Frontend**: Streamlit  
- **Backend**: FastAPI  
- **Database**: SQLite (or your configured database)  
- **Communication**: REST API  
- **Testing**: Pytest  

## Dependencies

The required dependencies are listed in `requirements.txt`. Below are the key packages:

```txt
fastapi
uvicorn
streamlit
requests
pydantic
sqlite3
pytest
pandas
```

## Setup in PyCharm

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/expense-management.git
cd expense-management
```

### 2. Open Project in PyCharm
Open **PyCharm** → Click **"Open"** → Select the project folder.

### 3. Set Up a Virtual Environment (Recommended)
Open **Terminal** in PyCharm and run:
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 4. Install Dependencies
```sh
pip install -r requirements.txt
```

### 5. Running the Backend Server
Navigate to the **backend/** directory in PyCharm.
Open **server.py**.
Run the following command in the terminal:
```sh
uvicorn backend.server:app --reload
```

### 6. Running the Frontend App
Navigate to the **frontend/** directory in PyCharm.
Open **app.py**.
Run the following command in the terminal:
```sh
streamlit run frontend/app.py
```

### 7. Running Tests
Navigate to the **tests/** directory.
Run all tests using:
```sh
pytest
```

## Notes
- Ensure your **backend server is running** before starting the frontend.
- If there are any module import errors, check the **Python interpreter settings** in PyCharm.
- If using a database, configure the correct connection details in `db_helper.py`.

---
This README provides structured setup instructions with code blocks for easy execution.

    