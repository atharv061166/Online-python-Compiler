document.getElementById("run-btn").addEventListener("click", function() {
    const code = document.getElementById("code-input").value;
    
    if (!code.trim()) {
        alert("Please enter some code to run!");
        return;
    }

    // Disable the button while running the code
    const runButton = document.getElementById("run-btn");
    runButton.disabled = true;
    runButton.innerHTML = "Running...";

    // Send the code to the server for execution
    fetch("/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        runButton.disabled = false;
        runButton.innerHTML = "Run Code";

        // Display output or error
        const outputBox = document.getElementById("output");
        const errorBox = document.getElementById("error");

        outputBox.classList.remove("hidden");
        errorBox.classList.remove("hidden");

        if (data.output) {
            outputBox.textContent = data.output;
        } else {
            outputBox.classList.add("hidden");
        }

        if (data.error) {
            errorBox.textContent = data.error;
        } else {
            errorBox.classList.add("hidden");
        }
    })
    .catch(error => {
        runButton.disabled = false;
        runButton.innerHTML = "Run Code";
        console.error('Error:', error);
    });
});
