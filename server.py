import traceback
from http.server import SimpleHTTPRequestHandler

import settings
from custom_types import Endpoint
#from errors import MethodNotAllowed
from datetime import datetime
from errors import NotFound
from utils import read_static
from utils import to_bytes
from utils import get_content_type
from utils import get_user_data


class MyHttp(SimpleHTTPRequestHandler):
    def do_GET(self):
        endpoint = Endpoint.from_path(self.path)
        content_type = get_content_type(endpoint.file_name)

        endpoints = {
            #"/": self.handle_root,
            #"/hello/": self.handle_hello,
            #"/style/": self.handle_style,
            #"/img/": self.handle_logo,
            #"/films/": self.handle_films,
            '/': [self.handle_static, ['index.html', 'text/html']],
            '/hello/': [self.handle_hello, [endpoint]],
            '/img/': [self.handle_static, [f'img/{endpoint.file_name}', content_type]],
            '/style/': [self.handle_static, [f'styles/{endpoint.file_name}', content_type]],
            '/films/': [self.handle_static, [f'films.html', content_type]],
        }

        try:
            handler, args = endpoints[endpoint.normal]
            handler(*args)
        except(NotFound, KeyError):
            self.handle_404()

        # if path == "/":
        #     self.handle_root()
        # elif path == "/hello/":
        #     self.handle_hello()
        # elif path == "/style/":
        #     self.handle_style()    
        # else:
        #     self.handle_404()


    def handle_root(self):
        return super().do_GET()

    def handle_hello(self, endpoint):
        user = get_user_data(endpoint.query_string)
        year = datetime.now().year - user.age


        content = f"""
        <html>
        <head>
            <title>Hello Page</title>
            <link rel="stylesheet" type="text/css" href="/style">
        </head>
        <body>

        <h1>Hello {user.name}!</h1>
        <h1>You was born at {year}</h1>
        <p>path: {self.path}</p>
        
        <form>
            <label for="name-id">Your name:</label>
            <input type="text" name="name" id="name-id" value="{user.name}">
            
            <label for="age-id">Your age:</label>
            <input type="text" name="age" id="age-id" value="{user.age}">

            <button type="submit" id="greet-button-id">OK</button>
                
        </form>

        </body>
        </html>
        """

        self.respond(content)



    def handle_404(self):
        msg = """NOT FOUND!!!!!!!!"""
        self.respond(msg, code=404, content_type="text/plain")


    def handle_static(self, file_path, content_type):
        content = read_static(file_path)
        self.respond(content, content_type=content_type)


    def handle_films(self):
        films = read_static("films.html")
        self.respond(films, content_type="text/html")


    def respond(self, message, code=200, content_type="text/html"):
        payload = to_bytes(message)

        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.send_header("Content-length", str(len(payload)))
        self.send_header("Cache-control", f"max-age={settings.CACHE_AGE}")
        self.end_headers()
        self.wfile.write(payload)





