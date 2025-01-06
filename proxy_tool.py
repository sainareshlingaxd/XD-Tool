import sys
import threading
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog, QMessageBox
)
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from stem import Signal
from stem.control import Controller
import re
import requests


# Proxy Handler
class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.server.gui.log(f"Intercepted Request: {self.path}")

        # Analyze URL for vulnerabilities
        self.server.gui.analyze_request(self.path)

        # Send mock response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Request intercepted by the proxy tool.")

    def do_POST(self):
        self.do_GET()


# Proxy Server Thread
class ProxyServerThread(threading.Thread):
    def __init__(self, port, gui):
        super().__init__(daemon=True)
        self.port = port
        self.gui = gui

    def run(self):
        server = HTTPServer(('0.0.0.0', self.port), ProxyHandler)
        server.gui = self.gui
        self.gui.log(f"Proxy running on port {self.port}")
        server.serve_forever()


# Tor Controller
def connect_to_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_password")
        controller.signal(Signal.NEWNYM)


# Vulnerability Scanner
def analyze_url(url):
    vulnerabilities = []
    if "redirect" in url or "url=" in url:
        vulnerabilities.append("Potential Open Redirect detected.")
    if re.search(r"(select|union|insert|delete|update)[%20\+\(]", url, re.IGNORECASE):
        vulnerabilities.append("SQL Injection pattern found.")
    if re.search(r"api[key|secret]|password", url, re.IGNORECASE):
        vulnerabilities.append("Sensitive information leak in URL.")
    return vulnerabilities


# GUI Class
class ProxyToolGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pentesting Proxy Tool")

        # GUI Elements
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.start_proxy_btn = QPushButton("Start Proxy", self)
        self.connect_tor_btn = QPushButton("Connect to Tor", self)
        self.request_replay_btn = QPushButton("Replay Request", self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Proxy Logs"))
        layout.addWidget(self.text_area)
        layout.addWidget(self.start_proxy_btn)
        layout.addWidget(self.connect_tor_btn)
        layout.addWidget(self.request_replay_btn)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Button Actions
        self.start_proxy_btn.clicked.connect(self.start_proxy)
        self.connect_tor_btn.clicked.connect(self.connect_tor)
        self.request_replay_btn.clicked.connect(self.replay_request)

    def log(self, message):
        self.text_area.append(message)

    def start_proxy(self):
        self.proxy_thread = ProxyServerThread(port=8080, gui=self)
        self.proxy_thread.start()

    def connect_tor(self):
        try:
            connect_to_tor()
            self.log("Connected to Tor successfully!")
        except Exception as e:
            self.log(f"Failed to connect to Tor: {e}")

    def analyze_request(self, url):
        vulnerabilities = analyze_url(url)
        if vulnerabilities:
            self.log("Vulnerabilities detected:")
            for vuln in vulnerabilities:
                self.log(f"- {vuln}")

    def replay_request(self):
        try:
            url, ok = self.get_text_input("Replay Request", "Enter the URL to replay:")
            if ok:
                response = requests.get(url)
                QMessageBox.information(self, "Request Replayed", f"Response Code: {response.status_code}")
        except Exception as e:
            self.log(f"Error replaying request: {e}")

    @staticmethod
    def get_text_input(title, prompt):
        dialog = QDialog()
        dialog.setWindowTitle(title)
        layout = QVBoxLayout(dialog)
        label = QLabel(prompt, dialog)
        layout.addWidget(label)
        text_input = QLineEdit(dialog)
        layout.addWidget(text_input)
        button = QPushButton("OK", dialog)
        layout.addWidget(button)

        def accept():
            dialog.done(1)

        button.clicked.connect(accept)
        dialog.exec_()
        return text_input.text(), bool(dialog.result())


# Main Function
def main():
    app = QApplication(sys.argv)
    gui = ProxyToolGUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
