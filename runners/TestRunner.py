# runner.py
import subprocess
import sys

def run_behave_tests():
    # Execute the Behave tests normally
    result = subprocess.run(['behave'], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Tests failed")
        sys.exit(result.returncode)

if __name__ == "__main__":
    run_behave_tests()
