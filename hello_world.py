from flask import Flask

app = Flask(__name__)
#change

@app.route('/')
def hello_world():
    print("Hello world!")

if __name__ == '__main__':
    app.run()