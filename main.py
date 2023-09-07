from flask import Flask, request, jsonify
import datetime, pytz, json

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "name": "Ezekiel Okebule",
        "text": "first submission for HNGx backend track",
    }
    return json.dumps(data)


@app.route('/api', methods=['GET'])
def api(slack_name="11011", track="backend"):
    data = {
        "current_day": datetime.datetime.now().strftime("%A"),
        "utc_time": datetime.datetime.now(pytz.utc),
        "github_file_url": "https://github.com/",
        "github_repo_url": "https://github.com/",
        "status_code": 200,
    }
    extra1 = request.args.get('slack_name')
    extra2 = request.args.get('track')
    if extra1 and extra2:
        data["slack_name"] = slack_name
        data["track"] = track
    
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)