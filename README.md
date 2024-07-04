# Eastwantage-Assignment

This project implements a simple address book API using FastAPI, allowing users to manage addresses and query addresses within a specified distance.

# Setup Environment
# 1. Clone the Repository
'''bash
git clone <repository-url>
cd address_book'''

# 2. Set Up Virtual Environment
Create and activate a virtual environment (recommended):

'''bash
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`

# 3. Install Dependencies
Install required Python packages using pip:

'''python
pip install -r requirements.txt

# 4. Initialize the Database
Ensure the SQLite database is set up and ready for use:

# Initialize the database schema
'''python
python main.py

# Run the Application
1. Start the FastAPI Server
Run the FastAPI application using Uvicorn:
'''python
uvicorn main:app --reload

# Explore API Documentation
# Access Swagger UI
To explore and interact with the API endpoints, open the Swagger UI in your browser:
'''markdown
URL: http://127.0.0.1:8000/docs
