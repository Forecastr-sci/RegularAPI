from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

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

if __name__ == "__main__":
    app.run(debug=True)