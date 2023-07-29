from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
    return 'Welcome to ITIL exam'

modules_list = ["FCN", "DevOps", "SecurityConcepts", "NDC", "COSA"]

@app.route('/modules')
def get_modules():
    modules_str = ", ".join(modules_list)
    return f"Ditiss modules names: {modules_str}."

@app.route('/me')
def get_my_info():
    my_info = {
        "name": "Chaitali Dalal",
        "prn": "230344223013",
        "phone_number": "9845654789"
    }
    return my_info 

if __name__ == '__main__':
    app.run(port=4000, host="0.0.0.0",debug=True)

