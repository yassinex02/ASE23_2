import subprocess
import sys

def test_output():
    result = subprocess.run(["python", "build.py"], capture_output=True, text=True)
    output = result.stdout.strip()
    
    if output == "6":
        print("Test passed: Output is 6")
    else:
        print("Test failed: Unexpected output") 
        sys.exit(1)

if __name__ == "__main__": test_output()