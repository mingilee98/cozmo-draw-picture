from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/submit-shape", methods=["POST"])
def submit_shape():
    drawing_data = request.form.get("drawing")
    encoded_string = drawing_data.split(",")[1]
    run_external_script("shape_main.py", encoded_string)
    return "Drawing received successfully"


@app.route("/submit-path", methods=["POST"])
def submit_path():
    drawing_data = request.form.get("drawing")
    encoded_string = drawing_data.split(",")[1]
    run_external_script("path_main.py", encoded_string)
    return "Drawing received successfully"


def run_external_script(file_path, input_data):
    try:
        cmd = ["python", file_path, input_data]
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"


if __name__ == "__main__":
    app.run(port=5000)
