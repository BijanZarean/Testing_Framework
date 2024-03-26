import subprocess

class TestRunner3:
    def __init__(self, tags=None):
        self.tags = tags if tags else ""
        self.results_dir = "./TestResults"
    
    def run_tests(self):
        # Run Behave tests with specified tags
        subprocess.run(["behave", "--tags", self.tags])
    
    def generate_allure_report(self):
        # Generate Allure report from test results
        subprocess.run(["allure", "generate", self.results_dir, "-o", f"{self.results_dir}/allure-report"])
    
    def serve_allure_report(self):
        # Serve Allure report
        subprocess.run(["allure", "serve", f"{self.results_dir}/allure-report"])

# Example usage:
if __name__ == "__main__":
    # Specify Behave tags to run
    tags_to_run = "@regression"
    
    # Create TestRunner instance with specified tags
    test_runner = TestRunner3(tags=tags_to_run)
    
    # Run Behave tests
    test_runner.run_tests()
    
    # Generate Allure report
    test_runner.generate_allure_report()
    
    # Serve Allure report
    test_runner.serve_allure_report()
