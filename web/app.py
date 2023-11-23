from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the main page
    return render_template('index.html', data=your_analyzed_data)

if __name__ == '__main__':
    app.run(debug=True)
