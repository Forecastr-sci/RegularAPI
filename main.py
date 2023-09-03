from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

# An example of a GET route
@app.route("/usr/<user_id>")
def get_user(user_id):
    user_data = {"id": user_id, "name": "Mordecai", "species": "Bluejay", "hobby": "chilling"}

    # Checks if request had argument "extra", like this: "/usr/<user_id>?extra=whatever"
    extra = request.args.get("extra")
    # If argument was actually passed its value will be added to user data at key "extra"
    if extra:
        user_data["extra"] = extra

    response = {"status_code": 200, "result": user_data}
    # return jsonified user data together with 200 - a status code for successful response
    return jsonify(response)

# an example of a POST route
@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.get_json()
    # Here we would ideally have writing the data to the database, but this is only a demo
    response = {"status_code": 201, "result": data}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)