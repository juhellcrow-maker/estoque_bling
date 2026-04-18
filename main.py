from flask import Flask
import time
import threading

app = Flask(__name__)

@app.route("/")
def health():
    return "ESTOQUE BLING - OK"

def loop_sync():
    while True:
        print("Executando loop de teste de estoque...")
        time.sleep(900)  # 15 minutos

if __name__ == "__main__":
    threading.Thread(target=loop_sync, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)