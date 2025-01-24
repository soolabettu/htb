#!/usr/bin/env python3

import subprocess
import sys

def execute_command(command):
    try:
        # Execute the command and capture the output
        output = subprocess.check_output(command, shell=True)

        # Decode the output from bytes to string
        output = output.decode('utf-8')

    
        # Compare the output to "HKB" (ignoring case)
        if "htb" in output.lower():
            print(output)
            print("Found 'HKB' in output. Exiting.")
            sys.exit(0)
        else:
            # Write output to file
            with open("output.log", "a") as f:
                f.write(output)

        # Print the output
        print(output)

    except subprocess.CalledProcessError as e:
        # Handle errors
        print(f"Error: {e}")

    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")

# Example usage:
command = "./stash"  # Replace with your command

while True:
    execute_command(command)
