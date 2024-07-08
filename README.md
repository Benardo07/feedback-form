# Feedback Form

A web application to collect feedback through forms, built with FastAPI for the backend and a modern frontend stack.

## Features

- Create and manage feedback questions
- Submit feedback with ratings
- View all submitted feedbacks

## Tech Stack

### Backend
- **FastAPI**: Web framework for building APIs with Python 3.7+
- **SQLAlchemy**: SQL toolkit and ORM
- **PostgreSQL**: Relational database
- **HTTPX**: HTTP client for testing
- **Alembic**: database migration tool for SQLAlchemy
- **Pydantic": data validation 

### Frontend
- **Vue js**: JavaScript library for building user interfaces


## How to Run Locally

### Prerequisites

- Python 3.7+
- Node.js and npm
- PostgreSQL

### Backend

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Benardo07/feedback-form.git
    cd feedback-form/backend
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the `backend` directory and add the following:
    ```env
    DATABASE_URL = postgresql+asyncpg://avnadmin:AVNS_naBaRsjsU2acdla9JSG@pg-7f676dd-benardo188.c.aivencloud.com:20799/feedback-form
    ```

5. **Run the database migrations**:
    ```bash
    alembic upgrade head
    ```

6. **Start the FastAPI server**:
    ```bash
    uvicorn app.main:app --reload
    ```

### Frontend

1. **Navigate to the frontend directory**:
    ```bash
    cd ../frontend
    ```

2. **Install dependencies**:
    ```bash
    npm install
    ```


4. **Start the development server**:
    ```bash
    npm run dev
    ```

### Accessing the Application

This website can be accesed online at (https://feedback-form-pi.vercel.app/)

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License.
