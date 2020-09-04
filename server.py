import traceback
from http.server import SimpleHTTPRequestHandler

import settings
from custom_types import Endpoint
#from errors import MethodNotAllowed
from errors import NotFound
from utils import normalize_path
from utils import read_static
from utils import to_bytes
from utils import get_content_type
from utils import get_name_from_qs


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
            '/hello/': [self.handle_hello, []],
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

    def handle_hello(self):
        content = f"""
        <html>
        <head>
            <title>Hello Page</title>
            <link rel="stylesheet" type="text/css" href="/style">
        </head>
        <body>

        <h1>Hello world!</h1>
        <p>path: {self.path}</p>
        
        <form>
            <label for="xxx-id">Your name:</label>
            <input type="text" name="xxx" id="xxx-id">
            
            <label for="xxx-id">Your age:</label>
            <input type="<text></text>" name="yyy" id="yyy-id">
            <button type="submit">OK</button>
                
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

#    def handle_style(self):
#        css = read_static("styles/style.css")
#        self.respond(css, content_type="text/css")

    def handle_films(self):
        films = read_static("films.html")
        self.respond(films, content_type="text/html")


#    def handle_logo(self):
#         image = read_static("img/cloud.png")
#         self.respond(image, content_type="image/jpg")


    def respond(self, message, code=200, content_type="text/html"):
        payload = to_bytes(message)

        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.send_header("Content-length", str(len(payload)))
        self.send_header("Cache-control", f"max-age={settings.CACHE_AGE}")
        self.end_headers()
        self.wfile.write(payload)





