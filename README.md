# XD Pentesting Proxy Tool

This is a versatile GUI-based proxy tool designed for penetration testing purposes. It combines proxy functionalities with additional features like vulnerability scanning, Tor routing, and request replay. The tool can intercept and analyze HTTP/HTTPS requests, replay requests, and evaluate potential security vulnerabilities.

---

## Features

1. **Intercept HTTP Requests and Responses**
   - Logs all intercepted requests in a user-friendly GUI.
   - Provides a mock response for demonstration purposes.

2. **Basic Vulnerability Scanning**
   - Detects potential open redirects.
   - Identifies SQL injection patterns.
   - Alerts on sensitive information leaks (e.g., API keys, passwords).

3. **Request Replayer**
   - Replay any HTTP request directly from the GUI.

4. **Tor Integration**
   - Option to route all requests through the Tor network.

5. **Expandable Framework**
   - The codebase can be extended to add custom modules for specific pentesting tasks.

6. **HTTP Header Analysis** *(Coming Soon)*
   - Future enhancement to evaluate the security of HTTP headers.

---

## Installation Guide

### Requirements
- **System Requirements**:
  - Python 3.x
  - A Linux distribution or Windows (Linux recommended for Tor support)
  - Administrator/root privileges for installing dependencies

- **Dependencies**:
  - `PyQt5` for GUI
  - `stem` for Tor control
  - `requests` for HTTP handling

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/sainareshlingaxd/XD-Tool.git
   cd pentesting-proxy-tool
   ```

2. Run the setup script:
   ```bash
   ./setup.sh
   ```

   This script:
   - Installs the necessary Python packages.
   - Configures Tor for proxying requests.
   - Starts the application.

3. Launch the tool:
   ```bash
   python3 proxy_tool.py
   ```

---

## Usage Instructions

1. **Starting the Proxy**
   - Click the `Start Proxy` button in the GUI to launch the HTTP server.
   - Set your browser or testing tool to route traffic through `http://localhost:8080`.

2. **Intercept Requests**
   - As HTTP requests pass through, they are displayed in the GUI.

3. **Analyze Vulnerabilities**
   - Each intercepted request is scanned for vulnerabilities such as open redirects, SQL injection patterns, and sensitive data leakage.

4. **Replay Requests**
   - Click `Replay Request` to enter a URL and replay the HTTP request. The response code is displayed in a dialog box.

5. **Use Tor for Anonymity**
   - Click `Connect to Tor` to route requests through the Tor network.

---

## Use Cases

1. **Penetration Testing**
   - Evaluate web applications for common vulnerabilities using built-in scanning features.

2. **Web Development Debugging**
   - Intercept requests during development to analyze and debug API calls.

3. **Anonymized Browsing and Testing**
   - Use Tor integration to anonymize HTTP requests for privacy and testing purposes.

4. **HTTP Request Replay**
   - Modify and replay captured HTTP requests to evaluate server responses and test business logic.

---

## Potential Improvements

- **Save Logs**: Implement the ability to export logs to a file for later analysis.
- **Custom Exploits**: Add modules for detecting more complex vulnerabilities.
- **HTTPS Support**: Expand support for HTTPS traffic interception and decryption.
- **Multi-Threading**: Improve server responsiveness by handling requests concurrently.

---

## Notes
- Use this tool responsibly and only for authorized testing purposes.
- Ensure compliance with legal and ethical guidelines while performing penetration testing.

---

For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/yourusername/pentesting-proxy-tool).

---

### Developer: Your Name
- **Email**: sainareshlinga@gmail.com
- **License**: MIT

