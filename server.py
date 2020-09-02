import traceback
from http.server import SimpleHTTPRequestHandler

import settings
#from errors import MethodNotAllowed
from errors import NotFound
from utils import normalize_path
from utils import read_static
from utils import to_bytes
from utils import get_name_from_qs
#from custom_types import Endpoint


class MyHttp(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = normalize_path(self.path)
      #  endpoint = Endpoint.from_path(self.path)
        handlers = {
            "/": self.handle_root,
            "/hello/": self.handle_hello,
            "/style/": self.handle_style, 
         #   "/img/": self.handle_logo, 
        }

        try:
            handler = handlers[path]
            handler()
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
            <button type="submit">OK</button>
            
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

    def handle_style(self):
        css = read_static("styles/style.css")
        self.respond(css, content_type="text/css")    


    # def handle_logo(self):
    #     image = read_static("img/cloud.png")
    #     self.respond(image, content_type="image/png")        


    def respond(self, message, code=200, content_type="text/html"):
        payload = to_bytes(message)

        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.send_header("Content-length", str(len(payload)))
        self.send_header("Cache-control", f"max-age={settings.CACHE_AGE}")
        self.end_headers()
        self.wfile.write(payload)





