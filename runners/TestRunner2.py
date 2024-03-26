import subprocess
from pathlib import Path

# Define the options for the test runner
options = [
    "behave",
    "--tags=@regression",   # Specify the suite of test cases you'd like to run
    "--no-capture",
    "--no-color",
    "--show-skipped",
    "--stop",
    "--no-skipped",
    "--no-summary",
    "--no-junit",
]

# Run the tests with the specified options
subprocess.run(options)
