from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/about')
def about():

    about_text = """
    Mikayla's Git Project
    """
    return about_text



if __name__=='__main__':

    app.run(debug=True)
