from flask import Flask, request
from flask_json import FlaskJSON, as_json
from flask import abort
from datetime import datetime

from app.const import url_send_message
from app.helper import send_message
from app.cache import cache_message, k_iter


class FlaskApp:
    def __init__(self):

        self.cache = {}
        self.last_date = datetime.now()

    def create_flask_app(self):
        app = Flask(__name__)
        app.config['JSON_AS_ASCII'] = False

        @as_json
        @app.route("/", methods=['POST'])
        def post():
            try:
                data = request.form if request.form else request.json
                if request.method == "POST":
                    chat_id = data['message']['chat']['id']
                    # раз в в 5 секунду чистим кэш
                    elapsed = datetime.now() - self.last_date

                    if divmod(elapsed.total_seconds(), 60)[0] > 0.05:
                        self.cache = {}
                        self.last_date = datetime.now()

                    if chat_id in self.cache:
                        if self.cache[chat_id] >= k_iter:
                            self.cache[chat_id] = 0
                        else:
                            self.cache[chat_id] = self.cache[chat_id] + 1
                    elif chat_id not in self.cache:
                        self.cache[chat_id] = 0

                    send_message(url_send_message, chat_id, cache_message[self.cache[chat_id]])
                    return "ok"

            except Exception as e:
                print(e)
                abort(404)

        @app.route("/health_status", methods=['GET'])
        def health():
            return "status ok"

        FlaskJSON(app)
        return app

    def run(self):
        app = self.create_flask_app()
        # app.run(host='0.0.0.0', port=80)
        return app
