import subprocess


def start():
    print("Starting tests with pytest:")
    print("------------------------------------------------------------")
    test_process = subprocess.Popen(["pytest", "--cov=perfed", "./tests"])
    test_exit_code = test_process.wait()
    exit(test_exit_code)
