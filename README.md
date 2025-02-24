# text-to-sql


## Overview
This project is a full-stack Text-to-SQL application that enables users to query datasets using natural language. The system generates valid SQL queries based on user input, executes them against a database, and displays the results.


## Requirements
- Python 3.8+
- FastAPI
- HTMX
- PostgreSQL
- Groq API Key


## Assumptions
This guide assumes that:
- You have already downloaded the [2015 Flight Delays and Cancellations dataset from Kaggle](https://www.kaggle.com/datasets/usdot/flight-delays).
- You have populated your PostgreSQL database with the data from this dataset.

If you haven't done so yet, you'll need to:
1. Download the dataset.
2. Import the data into your PostgreSQL database, ensuring the appropriate schema is created.


## Installation
### Step 1: Clone the Repository
```bash
git clone https://github.com/sunil-00/text-to-sql.git
```

### Step 2: Change Directory to the Project Folder
```bash
cd text-to-sql
```

### Step 3: Create a Virtual Environment
```bash
python3 -m venv venv
```

### Step 4: Activate the Virtual Environment
```bash
source venv/bin/activate
```

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 6: Copy `.env.sample` to `.env`
```bash
cp .env.sample .env
```

### Step 7: Set the Environment Variables
Edit the `.env` file with the following environment variables:

- `GROQ_API_KEY`: Your Groq API Key
- `MODEL`: Your LLM Model name (e.g. `text-to-sql`)
- `DATABASE_HOST`: Your PostgreSQL database host
- `DATABASE_PORT`: Your PostgreSQL database port
- `DATABASE_USER`: Your PostgreSQL database username
- `DATABASE_PASSWORD`: Your PostgreSQL database password
- `DATABASE_NAME`: Your PostgreSQL database name

### Step 8: Run the Application
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```


## Usage
### Step 1: Open the Application
Open a web browser and navigate to [http://localhost:8000/chat](http://localhost:8000/chat)

### Step 2: Enter a Query
Enter a natural language query in the input field *(e.g. "What is the total distance traveled by airline US in the first two months on Wednesday?")*

### Step 3: Execute the Query
Click the "Send" button to execute the query

### Step 4: View the Results
View the results in the chat container


## Notes
- The schema of the dataset is fed to the LLM, which allows the system to generate proper SQL queries based on natural language input. This should allow the system to work with other datasets as well.
- This project is for demonstration purposes only and should not be used in production without proper testing and validation.
