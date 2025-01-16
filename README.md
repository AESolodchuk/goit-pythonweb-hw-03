# Python Web Application

This project is a Python web application that serves static files, saves data to a JSON file, and renders log data using a Jinja2 template. The application is containerized using Docker.

## Project Structure

/goit-pythonweb-hw-03-python-web
├── app
│ ├── **init**.py
│ ├── routes.py
│ ├── storage.py
│ └── templates
│ └── log.html
├── Dockerfile
├── main.py
├── requirements.txt
└── storage
└── data.json

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
