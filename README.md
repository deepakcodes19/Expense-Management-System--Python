# Expense Management System

## Project Overview

The **Expense Management System** is a full-stack application designed to help users track and manage their personal or business expenses. This system features a frontend built with **Streamlit** for easy interaction, and a backend powered by **FastAPI** to process requests and manage data. The backend runs locally on port 8000, and the frontend communicates with the backend via API requests. The application helps users categorize, add, view, and manage their expenses effectively.

## Features

- **Frontend**: User-friendly web interface built using Streamlit to interact with the system.
- **Backend**: FastAPI-based backend for handling requests and managing data.
- **Expense Tracking**: Users can input, view, and categorize various types of expenses (e.g., food, utilities, entertainment, etc.).
- **Real-time Updates**: Expenses are displayed and updated in real-time on the frontend.
- **Local Hosting**: The backend is deployed locally on port 8000.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Web Server**: Uvicorn (for FastAPI)
- **Database**: MySQL (or another database for the backend)
- **Python Version**: 3.7 or higher

## Screenshots

Here are some screenshots of the application:

1. **Expense Analytics**
   ![Expense Analytics](https://github.com/deepakcodes19/Expense-Management-System--Python/blob/main/Expense%20Analytics.png)

2. **Expense Management**
   ![Expense Management](https://github.com/deepakcodes19/Expense-Management-System--Python/blob/main/Expense%20management.png)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Streamlit
- FastAPI
- Uvicorn
- MySQL (or another database for the backend)

## Installation

Follow the steps below to set up the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/expense-management-system.git
cd expense-management-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This will install all the necessary dependencies for the project.

### 4. Run the FastAPI backend

The backend is powered by FastAPI, which will run on **localhost**:

```bash
uvicorn backend.server:app --reload
```

The backend will be available at `http://localhost:8000`.

### 5. Run the Streamlit frontend

To launch the frontend, run the following command:

```bash
streamlit run frontend/app.py
```

This will open the frontend in your browser at `http://localhost:8501`.

## API Endpoints

Here are some example API endpoints you can interact with:

- `GET /expenses` - Fetches all expense records.
- `POST /expenses` - Adds a new expense record.
- `PUT /expenses/{id}` - Updates an existing expense record.
- `DELETE /expenses/{id}` - Deletes an expense record by its ID.

You can interact with these endpoints using the frontend or directly via API testing tools (e.g., Postman).

## Project Structure

Here is an overview of the project structure:

```
expense-management-system/
├── .idea/                  # IDE-specific files (e.g., for PyCharm)
├── .pytest_cache/          # Pytest cache files
├── backend/                # Backend-related files
│   ├── db_helper.py        # Database helper functions
│   ├── logging_setup.py    # Logging configuration and setup
│   └── server.py           # FastAPI backend server logic
│   └── server.log          # Backend server log file
│
├── frontend/               # Frontend-related files
│   ├── add_update_ui.py    # Streamlit UI for adding/updating expenses
│   ├── analytics_ui.py     # Streamlit UI for analytics and reports
│   └── app.py              # Main Streamlit application logic
│
├── test/                   # Test files
│   ├── backend/            # Backend tests
│   │   ├── .pytest_cache/  # Pytest cache for backend tests
│   │   └── test_db_helper.py  # Test cases for database helper functions
│   └── frontend/           # Frontend tests
│       └── conftest.py     # Test setup for frontend
│
├── log_file                # General log file for app activities
├── README.md               # Project documentation
├── requirements.txt        # Project dependencies
└── server.log              # Server log file for troubleshooting
```

- **backend/**: Contains the backend-related files, including server logic (`server.py`), database helpers (`db_helper.py`), and logging setup (`logging_setup.py`).
- **frontend/**: Contains the Streamlit frontend logic for adding and updating expenses (`add_update_ui.py`, `analytics_ui.py`) as well as the main app (`app.py`).
- **test/**: Contains test cases for the backend (`test_db_helper.py`) and frontend (`conftest.py`).
- **log_file**: A log file to track app activities.

## Troubleshooting

If you encounter any issues, here are a few common solutions:

- **Backend connection issues**: Ensure the FastAPI backend is running (`uvicorn backend.server:app --reload`) and accessible at `http://localhost:8000`.
- **Module import errors**: Make sure all dependencies are correctly installed. If issues persist, try reinstalling dependencies with `pip install -r requirements.txt`.

## Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and create a pull request.

Please ensure your code follows the existing code style and includes appropriate tests for any new functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- **Streamlit**: For providing an easy and efficient way to build interactive web applications.
- **FastAPI**: For enabling the creation of high-performance APIs with ease.
- **Uvicorn**: For serving the FastAPI application.
- **MySQL**: For providing a powerful, scalable database solution for this project.

## Contact

For any questions or feedback, please feel free to contact me on [LinkedIn](https://www.linkedin.com/in/deepakyadav19/).
