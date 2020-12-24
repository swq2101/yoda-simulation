from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('yodaForm.html')

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)