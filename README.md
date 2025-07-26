# Backend Assignment: KPA Form Data API

This project is an implementation of a backend service for the KPA Form Data assignment. It provides two APIs for managing wheel specification forms, built with Python (FastAPI) and connected to a PostgreSQL database.

## Technologies and Tech Stack

- **Backend Framework:** Python 3.9 with FastAPI
- **Database:** PostgreSQL
- **Data Validation:** Pydantic
- **Database ORM:** SQLAlchemy
- **Containerization:** Docker
- **Environment Configuration:** python-dotenv

## Implemented APIs

The following two API endpoints have been implemented:

1. **`POST /api/forms/wheel-specifications`**
   - **Description:** Creates and saves a new wheel specification form. The request body must match the structure defined in the Postman collection. It returns a success message and a summary of the saved data.
   - **Request Body:** See `KPA_form data_LOCAL.postman_collection.json`.
   - **Response (201 Created):**
     ```json
     {
       "success": true,
       "message": "Wheel specification submitted successfully.",
       "data": {
         "formNumber": "WHEEL-2025-001",
         "submittedBy": "user_id_123",
         "submittedDate": "2025-07-03",
         "status": "Saved"
       }
     }
     ```

2. **`GET /api/forms/wheel-specifications`**
   - **Description:** Retrieves a list of wheel specification forms. It supports filtering by `formNumber`, `submittedBy`, and `submittedDate` through query parameters.
   - **Query Parameters:** `formNumber` (string), `submittedBy` (string), `submittedDate` (string)
   - **Response (200 OK):**
     ```json
     {
       "success": true,
       "message": "Filtered wheel specification forms fetched successfully.",
       "data": [
         {
           "formNumber": "WHEEL-2025-001",
           "submittedBy": "user_id_123",
           "submittedDate": "2025-07-03",
           "fields": {
             "treadDiameterNew": "915 (900-1000)",
             "lastShopIssueSize": "837 (800-900)",
             "condemningDia": "825 (800-900)",
             "wheelGauge": "1600 (+2,-1)",
             "variationSameAxle": "0.5",
             "variationSameBogie": "5",
             "variationSameCoach": "13",
             "wheelProfile": "29.4 Flange Thickness",
             "intermediateWWP": "20 TO 28",
             "bearingSeatDiameter": "130.043 TO 130.068",
             "rollerBearingOuterDia": "280 (+0.0/-0.035)",
             "rollerBearingBoreDia": "130 (+0.0/-0.025)",
             "rollerBearingWidth": "93 (+0/-0.250)",
             "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
             "wheelDiscWidth": "127 (+4/-0)"
           }
         }
       ]
     }
     ```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd kpa_backend_assignment
   ```

2. **Create and configure the environment file:**
   - Update the `.env` file with your PostgreSQL connection string.
   - Example: `DATABASE_URL=postgresql://username:password@localhost:5432/kpa_db`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

5. **Run with Docker Compose (Recommended):**
   ```bash
   docker-compose up --build
   ```
   The API will be available at `http://localhost:8000`.

6. **Alternative: Run with Docker (Manual):**
   - Build the Docker image:
     ```bash
     docker build -t kpa-api .
     ```
   - Run the Docker container:
     ```bash
     docker run -d --name kpa-container -p 8000:8000 kpa-api
     ```

## API Documentation

Once the application is running, you can access the interactive API documentation at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Quick Setup

For quick setup, you can use the provided setup scripts:

**Windows:**
```batch
setup.bat
```

**Linux/macOS:**
```bash
chmod +x setup.sh
./setup.sh
```

These scripts will install dependencies and set up the environment file.

## Testing

Use the provided Postman collection (`KPA_form data_LOCAL.postman_collection.json`) to test the APIs. The collection is configured to use environment variables:

1. **Import the collection** into Postman
2. **Create a new environment** in Postman with the variable:
   - Variable name: `baseUrl`
   - Value: `http://127.0.0.1:8000` (for both local and Docker setups)
3. **Select the environment** before running the requests

The collection includes examples for:
- Creating wheel specifications (POST)
- Retrieving wheel specifications with filters (GET)
- Health check endpoint
- API documentation endpoint

## Database Setup

**Option 1: Using Docker Compose (Recommended)**
No manual database setup required. Docker Compose will automatically:
- Start a PostgreSQL container
- Create the database and user
- Connect the API to the database

**Option 2: Manual PostgreSQL Setup**
If running the API locally without Docker, ensure you have PostgreSQL installed and create a database:

```sql
CREATE DATABASE kpa_db;
CREATE USER kpa_user WITH PASSWORD 'kpa_password';
GRANT ALL PRIVILEGES ON DATABASE kpa_db TO kpa_user;
```

Then update your `.env` file with the correct database URL.

## Project Structure

```
/kpa_backend_assignment
|-- app/
|   |-- __init__.py
|   |-- main.py             # FastAPI application, endpoints
|   |-- models.py           # Pydantic models for request/response validation
|   |-- database.py         # Database session and engine setup
|   |-- crud.py             # Functions for database operations (Create, Read)
|-- .env                    # Environment variables for configuration
|-- .env.example            # Environment variables template
|-- docker-compose.yml      # Docker Compose configuration
|-- Dockerfile              # Docker configuration
|-- setup.bat               # Windows setup script
|-- setup.sh                # Linux/macOS setup script
|-- run_server.py           # Local development server script
|-- KPA_form data_LOCAL.postman_collection.json  # Updated Postman collection
|-- README.md               # Project documentation
|-- requirements.txt        # Python dependencies
```

## Limitations and Assumptions

- The database connection is assumed to be available at the URL specified in the `.env` file.
- The `submittedDate` is stored as a string as per the provided API specification.
- Error handling is basic; it returns standard HTTP status codes for not found (404) or bad requests (400).
- Input validation is implemented using Pydantic models to ensure data integrity.
- The application creates database tables automatically on startup using SQLAlchemy.
