from flask import Flask, render_template, request
application = app = Flask(__name__)

#port = int(os.getenv("VCAP_APP_PORT"))
#port = os.getenv("VCAP_APP_PORT")

@app.route('/')
def home():
   return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)


    #app.run(host='0.0.0.0', port=port)

   #app.run(debug=True)

    #app.run(host='127.0.0.1', port=port)
