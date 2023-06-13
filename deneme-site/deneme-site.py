from urllib.parse import parse_qs
from pymongo import MongoClient
import http.server
import socketserver
import os

# MongoDB configuration
mongo_uri = 'mongodb://mongo:27017/'
mongo_db = os.environ['MONGODB_DB']
mongo_collection = os.environ['MONGODB_C']

# MongoDB bağlantısını oluştur
mongo_client = MongoClient(mongo_uri)
mongo_db = mongo_client[mongo_db]
collection = mongo_db[mongo_collection]

PORT = os.environ['PORT']
INDEX_FILE = 'index.html'


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open(INDEX_FILE, 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)
        veri = data.get('veri', [''])[0]

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        print(f"Gönderilen veri: {veri}")
        # Veriyi MongoDB'ye kaydet
        collection.insert_one({"veri": veri})

        with open(INDEX_FILE, 'rb') as file:
            self.wfile.write(file.read())


Handler = MyHandler

with socketserver.TCPServer(("", int(PORT)), Handler) as httpd:
    print(f"Web sunucusu http://localhost:{PORT} adresinde çalışıyor.")
    httpd.serve_forever()
