from jinja2 import Environment, FileSystemLoader, Template
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import mimetypes
import json
import pathlib
import urllib.parse
import logging


FILE_PATH = "storage/data.json"
ENV = Environment(loader=FileSystemLoader("./"))
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


class HttpHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        logging.debug("HttpHandler initialized")
        super().__init__(*args, **kwargs)

    def do_POST(self):
        logging.debug("Handling POST request")
        data = self.rfile.read(int(self.headers["Content-Length"]))

        data_parse = urllib.parse.unquote_plus(data.decode())

        data_dict = {
            key: value for key, value in [el.split("=") for el in data_parse.split("&")]
        }
        print({str(datetime.now()): data_dict})
        self.save_to_file({str(datetime.now()): data_dict})
        self.send_response(302)
        self.send_header("Location", "/")
        self.end_headers()

    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        path = pathlib.Path(pr_url.path).stem
        logging.debug(
            f"Handling GET request for path: {pr_url.path} (normalized: {path})"
        )
        if path == "":
            self.send_html_file("index.html")
        elif path == "message":
            self.send_html_file("message.html")
        elif path == "log":
            self.render_log_template()
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            else:
                self.send_html_file("error.html", 404)

    def send_html_file(self, filename, status=200):
        logging.debug(f"Sending HTML file: {filename} with status: {status}")
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        logging.debug(f"Sending static file: {self.path}")
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()
        with open(f".{self.path}", "rb") as file:
            self.wfile.write(file.read())

    def save_to_file(self, data: dict) -> None:
        logging.debug(f"Saving data to file: {FILE_PATH}")
        with open(FILE_PATH, mode="r+", encoding="utf-8") as file:
            try:
                content = json.load(file)
            except:
                content = {}
            content.update(data)
            file.seek(0)
            json.dump(content, file, indent=4)

    def render_log_template(self):
        logging.debug("Rendering log template")
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                content = json.load(file)
        except json.JSONDecodeError:
            content = {}
        template = ENV.get_template("log.html")
        rendered_content = template.render(log=content)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(rendered_content.encode("utf-8"))


def run(server_class=HTTPServer, handler_class=HttpHandler):
    logging.debug("Starting server")
    server_address = ("0.0.0.0", 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        logging.debug("Stopping server")
        http.server_close()


if __name__ == "__main__":
    run()
