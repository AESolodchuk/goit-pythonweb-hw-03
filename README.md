# Python Web Application

This project is a Python web application that serves static files, saves data to a JSON file, and renders log data using a Jinja2 template. The application is containerized using Docker.

## Project Structure

```sh
/goit-pythonweb-hw-03
├── Dockerfile
├── main.py
├── requirements.txt
├── storage
│   └── data.json
└── templates
    └── log.html
```

## Running the Project

### Build the Docker image

To build the Docker image, run the following command:

```sh
docker build -t my-python-app .
```

Run the Docker container
To run the Docker container, use the following command:

```sh
docker run -p 3000:3000 my-python-app
```

Access the application
Open your web browser and navigate to:

```sh
http://localhost:3000
```
