#!/usr/bin/env python3
"""Minimal static server for the portfolio — avoids os.getcwd() at startup."""
import http.server
import socketserver

PORT = 3001
DIRECTORY = "/Users/frank/Projects/Portfolio"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, fmt, *args):
        print(fmt % args, flush=True)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Portfolio running on http://localhost:{PORT}", flush=True)
    httpd.serve_forever()
