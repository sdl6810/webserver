import http.server
import socketserver

ser_port = 8000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",ser_port), Handler) as httpd:
	print("Starting at port", ser_port)
	httpd.serve_forever()