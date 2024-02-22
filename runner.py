import subprocess

# Number of times to execute the command
num_executions = 10

for i in range(num_executions):
    print(f"Execution {i+1} of {num_executions}")
    # Construct the command as a list of arguments
    command = ["sl-python", "pytest", "--teststage", "pytest", "--cov-report",f"report-run-stage{i}.xml"]
    #command = ["sl-python", "pytest", "--teststage", "pytest"]
    # Execute the command
    subprocess.run(command)

    # Optionally, you can handle the output or errors here

print("Completed all executions.")
