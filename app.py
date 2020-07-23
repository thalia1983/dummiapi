from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

tasks = [
    {
        "farmer_id": 1,
        "eventTime": "2019-05-10T10:45:30Z",
        "eventType": "EVENT_HARVESTING",
        "eventLocation": {
            "lat": 37.9833,
            "lng": 23.7333
        }
    },

    {
        "farmer_id": 2,
        "eventTime": "2019-05-10T10:45:30Z",
        "eventType": "EVENT_HARVESTING",
        "eventLocation": {
            "lat": 37.9833,
            "lng": 23.7333
        }
    },
    {
        "farmer_id": 3,
        "eventTime": "2019-05-10T10:45:30Z",
        "eventType": "EVENT_HARVESTING",
        "eventLocation": {
            "lat": 37.9833,
            "lng": 23.7333
        }
    },
    {
        "farmer_id": 4,
        "eventTime": "2019-05-10T10:45:30Z",
        "eventType": "EVENT_HARVESTING",
        "eventLocation": {
            "lat": 37.9833,
            "lng": 23.7333
        }
    },
    {
        "farmer_id": 5,
        "eventTime": "2019-05-10T10:45:30Z",
        "eventType": "EVENT_HARVESTING",
        "eventLocation": {
            "lat": 37.9833,
            "lng": 23.7333
        }
    }

]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == "__main__":
    app.run(debug=True)


@app.route('/todo/api/v1.0/tasks/<int:task_farmer_id>', methods=['GET'])
def get_task(task_farmer_id):
    task = [task for task in tasks if task['farmer_id'] == task_farmer_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
