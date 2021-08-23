from flask import Flask, render_template, request
def create_app():


    app = Flask(__name__)

    @app.route('/', methods=['POST', 'GET'])
    def home():
        if request.method == 'POST':
            age = request.form.get('age')
            status_vac = request.form.get('status_vac')
            reason_test = request.form.get('reason_test')
            print(age, status_vac, reason_test)

        return render_template("home.html")
     
    return app