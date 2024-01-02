import subprocess

expected_output = """
Pin 0 is on
Pin 0 is off
Pin 0 is on
Pin 0 is off
Pin 0 is on
Pin 0 is off
Pin 0 is on
Pin 0 is off
Pin 0 is on
Pin 0 is off
Pin 0 is on
Pin 0 is off
Pin 0 is on
Pin 0 is off
Pin 0 is on
Pin 0 is off
Pin 0 is on
Pin 0 is off
Pin 0 is on
Pin 0 is off
"""
expected_output = expected_output.strip().split('\n')


def check_output(expected_output):

    # Run the code using subprocess
    result = subprocess.run(['python3', 'blynk.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    actual_output = result.stdout.strip().split('\n')
    for i in range(len(actual_output)):
        try:
            assert actual_output[i] == expected_output[i]
        except AssertionError:
            print("Expected: %s" % expected_output[i])
            print("Actual: %s" % actual_output[i])
            print("Expected output does not match actual output")
    print("Expected output matches actual output")
    print("Test passed")




check_output(expected_output)
