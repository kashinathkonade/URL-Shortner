from flask import Flask, render_template, request, redirect

app = Flask(__name__)

url_database = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('longUrl')
    short_url = generate_short_url()
    url_database[short_url] = long_url
    return {'shortUrl': f'http://localhost:5000/{short_url}'}

@app.route('/<short_url>')
def redirect_to_original(short_url):
    long_url = url_database.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return 'URL not found', 404

def generate_short_url():
    return 'short_' + str(len(url_database) + 1)

if __name__ == '__main__':
    app.run(debug=True)
