# Basic Flask CRUD API with SQLite

This project is a simple CRUD (Create, Read, Update, Delete) API built with Flask and SQLAlchemy, using SQLite as the database. The application is containerized using Docker and Docker Compose.

## Project Structure

- `app.py`: The main application file containing the Flask API logic.
- `Dockerfile`: Defines the Docker image for the Flask application.
- `docker-compose.yml`: Configures the Docker services and volumes.
- `requirements.txt`: Lists the Python dependencies for the project.

## Features

- **Create**: Add new products.
- **Read**: List all products and get details of a specific product.
- **Update**: Modify existing products.
- **Delete**: Remove products from the database.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Running the Application

1. **Clone the Repository**

   ```bash
   git clone https://github.com/lisazevedo/basic-crud-api
   cd basic-crud-api
2. **Build and Start the Containers**

   ```bash
   docker compose up --build
   ```

   This command will:
   - Build the Docker image for the Flask application.
   - Start a `busybox` container to handle the SQLite volume.
   - Start the Flask application container, linking it with the SQLite volume.

3. **Access the API**

   The Flask API will be available at `http://localhost:5000`.

### API Endpoints

- **Create Product**

  `POST /product`

  Request Body (JSON):
  ```json
  {
    "name": "Sample Product",
    "price": 19.99
  }
  ```

  Response (JSON):
  ```json
  {
    "message": "Product created successfully",
    "product": {
      "id": 1,
      "name": "Sample Product",
      "price": 19.99
    }
  }
  ```

- **Get All Products**

  `GET /products`

  Response (JSON):
  ```json
  [
    {
      "id": 1,
      "name": "Sample Product",
      "price": 19.99
    }
  ]
  ```

- **Get Product by ID**

  `GET /product/<id>`

  Response (JSON):
  ```json
  {
    "id": 1,
    "name": "Sample Product",
    "price": 19.99
  }
  ```

- **Update Product by ID**

  `PUT /product/<id>`

  Request Body (JSON):
  ```json
  {
    "name": "Updated Product",
    "price": 24.99
  }
  ```

  Response (JSON):
  ```json
  {
    "message": "Product updated successfully",
    "product": {
      "id": 1,
      "name": "Updated Product",
      "price": 24.99
    }
  }
  ```

- **Delete Product by ID**

  `DELETE /product/<id>`

  Response (JSON):
  ```json
  {
    "message": "Product deleted successfully"
  }
  ```

## Development

To make changes to the Flask application:

1. **Modify `app.py`**: Update the application logic as needed.
2. **Rebuild the Docker Image**: Run `docker compose build` to apply the changes.
3. **Restart the Containers**: Use `docker compose up` to restart the application.

## Troubleshooting

- **Database Table Not Found**: Ensure that `db.create_all()` is called before handling requests. Check the Docker Compose volume mount to ensure the SQLite database file is correctly shared.
