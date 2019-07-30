from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
  name = "who"
  # return "Hello World"
  return render_template('hello.html', title='hello', name=name)

if __name__ == "__main__":
  app.run(debug=True, port=8888, threaded=True)
