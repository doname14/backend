# Running the Project with Docker

This section provides instructions to build and run the project using Docker and Docker Compose.

## Prerequisites

- Ensure Docker and Docker Compose are installed on your system.
- Python version 3.11 is used in the Dockerfiles.

## Environment Variables

- No specific environment variables are required to be set manually; all configurations are handled within the Dockerfiles and Compose file.

## Build and Run Instructions

1. Clone the repository and navigate to the project root directory.
2. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Access the application services:
   - Main service: [http://localhost:8000](http://localhost:8000)

## Exposed Ports

- Main service: 8000
- Auth service: 8000
- Backend service: 8000
- WebSocket service: 8000

## Notes

- The `requirements.txt` file is used to install Python dependencies.
- The `Dockerfile` for each service specifies the necessary dependencies and configurations.

For further details, refer to the individual Dockerfiles and the `docker-compose.yml` file.