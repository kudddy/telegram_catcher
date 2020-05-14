from flask import Flask, request
from flask_json import FlaskJSON, as_json
from flask import send_from_directory, abort


class FlaskApp:
    def __init__(self):

        pass

    def create_flask_app(self):
        app = Flask(__name__)
        app.config['JSON_AS_ASCII'] = False

        @as_json
        @app.route("/", methods=['POST'])
        def post():

            try:
                data = request.form if request.form else request.json
                if request.method == "POST":
                    print(data)
                    return "ok"

            except Exception as e:
                print(e)
                abort(404)

        @app.route("/health_status", methods=['GET'])
        def health():
            return "status ok"

        FlaskJSON(app)
        return app

    def run(self, host='127.0.0.1', port=5001):
        app = self.create_flask_app()
        # app.run(host='0.0.0.0', port=80)
        return app
