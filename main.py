from app.engine import FlaskApp


app = FlaskApp()

app = app.run().run(host='0.0.0.0', port=80)

