Overview
The Python Code Runner is a simple yet powerful web-based tool designed to execute Python scripts directly from your browser.
This project is built using Flask for the backend and a dynamic HTML interface for the frontend, offering an intuitive and responsive user experience.
It's an excellent solution for running and testing Python code quickly without needing to set up a local development environment.

Features
Code Execution: Execute Python code directly in the browser with instant results.
Error Handling: Displays errors if the submitted code contains any issues, making debugging easier.
Interactive UI: A clean, modern interface with a code editor, output display, and error logs.
Backend Integration: Uses Flask for handling requests and running Python scripts securely.
Real-Time Updates: Outputs and errors are displayed in real-time as the code is executed.

Use of Judge0 API in the Python Code Runner
The Judge0 API is a versatile and efficient API used for compiling and running code in various programming languages. 
In this project, the Judge0 API has been integrated to execute Python code and provide the output or errors directly on the web interface.

Purpose of Judge0 API
Judge0 API is used to:

Execute Python Code: The submitted Python script is sent to the Judge0 API for execution.
Retrieve Output or Errors: After execution, the API returns the program's output or any errors encountered during runtime.
Handle Resource Constraints: The API ensures that the code execution adheres to CPU time and memory limits, preventing excessive resource usage.

Project Structure:
python-code-compiler/
│
├── app.py                # Backend logic using Flask
├── templates/
│   └── index.html        # Frontend HTML file
├── static/
│   └── styles.css        # Optional CSS styling
└── requirements.txt      # List of dependencies


Prerequisites
Python 3.6+ installed on your system.
Flask library installed.


Installation:
Clone the repository:git clone https://github.com/atharv061166/online-python-compiler.git
cd python-code-runner

Install dependencies:pip install -r requirements.txt

Usage:
Start the server:python app.py
Open your browser and visit:http://127.0.0.1:5000
Write your Python code, click Run, and view the output.

File Descriptions
app.py: Flask backend that handles code execution.
templates/index.html: User interface for writing and running Python code.
static/styles.css: Styling for the webpage.
requirements.txt: Contains project dependencies (Flask==2.2.3).

Example
Input:print("Hello, Python!")
Output:Hello, Python!

Contribution
Fork the repository and submit pull requests for enhancements.
Report issues to help improve the project.

License
This project is open-source under the MIT License.
