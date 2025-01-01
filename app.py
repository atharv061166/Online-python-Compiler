import requests
from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

# URL for the Judge0 API
JUDGE0_API_URL = "https://judge0-ce.p.rapidapi.com/submissions?base64_encoded=false&wait=true"

# Your RapidAPI Key (replace this with your actual RapidAPI Key)
RAPIDAPI_KEY = "e0c38d10edmshb01903d571b4052p159165jsnb5703f9ebc93"

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com",
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    # Pass 'time' to the template so it can be used in index.html
    return render_template("index.html", time=int(time.time()))  # Convert time to an integer

@app.route("/run", methods=["POST"])
def run_code():
    try:
        # Get the code from the frontend
        code = request.json.get("code", "")
        if not code.strip():
            return jsonify({"error": "No code provided"}), 400

        # Prepare the payload for the Judge0 API
        payload = {
            "source_code": code,
            "language_id": 71,  # 71 is the language ID for Python (3.x) in Judge0
            "stdin": "",
            "cpu_time_limit": 2,
            "memory_limit": 128000,
            "block_suspended": False
        }

        # Send the request to Judge0 API
        response = requests.post(JUDGE0_API_URL, json=payload, headers=headers)

        # Debugging: Log the response status and content
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.text)

        if response.status_code != 200:
            return jsonify({"error": "Error calling Judge0 API", "details": response.text}), 500

        # Get the result from Judge0 API
        result = response.json()
        output = result.get("stdout", "")
        error = result.get("stderr", "")

        # Return the output or error
        return jsonify({"output": output, "error": error}), 200

    except Exception as e:
        # Log the exception error
        print("Error during code execution:", e)
        return jsonify({"error": "Internal Server Error: " + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)
