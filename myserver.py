import ssl
from pathlib import Path

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Welcome to Shay's web server</h1><hr><iframe src="https://giphy.com/embed/YqnomYZSfJO5glyPkM" width="480" height="336" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/command-and-conquer-remaster-tiberian-sun-YqnomYZSfJO5glyPkM">via GIPHY</a></p>
    """

def main():
    CERTS = Path(".")
    print(f"Using {CERTS.absolute()} as pats")
    ssl_context = ssl.SSLContext()
    ssl_context.load_verify_locations(cafile=CERTS/'ca.crt')
    ssl_context.load_cert_chain(CERTS/'cert.crt', CERTS/'cert.key')
    print("Listening...")
    app.run(host='127.0.0.1', port=443, ssl_context=ssl_context)

if __name__ == "__main__":
    main()