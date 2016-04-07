from flask import Flask
app = Flask(__name__)  # Note the double underscores on each side!

@app.route("/")

def index():
	template = 'index.html'
	return render_template(template)

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)

    
