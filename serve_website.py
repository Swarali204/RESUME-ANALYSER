import http.server
import socketserver
import os
import webbrowser
from threading import Thread
import time

# Change to the directory containing the HTML files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow requests from any origin
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🌐 Website server running at: http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"🔗 Open: http://localhost:{PORT}/advanced-index.html")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()

if __name__ == "__main__":
    print("🚀 Starting Website Server...")
    
    # Open browser automatically after a short delay
    def open_browser():
        time.sleep(2)
        webbrowser.open(f'http://localhost:{PORT}/advanced-index.html')
    
    Thread(target=open_browser).start()
    
    try:
        start_server()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.") 