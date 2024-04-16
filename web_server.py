

from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys


class CORSRequestHandler(SimpleHTTPRequestHandler):
	def end_headers(self):
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Access-Control-Allow-Methods', '*')
		self.send_header('Access-Control-Allow-Headers', '*')
		self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
		self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
		self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
		return super(CORSRequestHandler, self).end_headers()

	def do_OPTIONS(self):
		self.send_response(200)
		self.end_headers()

host = "localhost"
port = int(sys.argv[len(sys.argv)-1]) if len(sys.argv) > 1 else 8080

print("Listening on http://localhost:{}".format(port))
httpd = HTTPServer((host, port), CORSRequestHandler)
httpd.serve_forever()

