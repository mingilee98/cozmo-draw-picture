from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/submit-image", methods=["POST"])
def run_script():
    drawing_data = request.form.get("drawing")
    encoded_string = drawing_data.split(",")[1]
    run_external_script(encoded_string)
    return "Drawing received successfully"


def run_external_script(input_data):
    try:
        cmd = ["python", "main.py", input_data]
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"


if __name__ == "__main__":
    app.run(port=5000)
