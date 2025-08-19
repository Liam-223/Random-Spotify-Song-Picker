#!/usr/bin/env python3
import http.server, socketserver, webbrowser, threading, os, sys
PORT = 8000
ADDR = f"http://127.0.0.1:{PORT}/index.html"

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # keep console clean

def serve():
    with socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler) as httpd:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        print(f"Serving on {ADDR}  (Ctrl+C to stop)")
        httpd.serve_forever()

if __name__ == "__main__":
    threading.Timer(0.7, lambda: webbrowser.open(ADDR)).start()
    try:
        serve()
    except KeyboardInterrupt:
        print("\nBye!")
