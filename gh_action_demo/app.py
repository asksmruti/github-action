from flask import Flask, render_template
import geocoder
import os


app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', task="Meet GP-1")


@app.route('/test')
def test():
    geo_data = geocoder.ip('me').geojson
    return geo_data


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
