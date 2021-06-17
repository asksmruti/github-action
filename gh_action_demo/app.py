from flask import Flask, render_template
import geocoder


app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', task="Meet Smruti")


@app.route('/test')
def test():
    geo_data = geocoder.ip('me').geojson
    return geo_data


if __name__ == "__main__":
    app.run()
