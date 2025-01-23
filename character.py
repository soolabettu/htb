#!/usr/bin/env python3



import subprocess

def launch_program(program_name, arg1, arg2):
    try:
        # Launch the program
        process = subprocess.Popen([program_name, arg1, arg2], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        i = 0
        ans_list = []
        # Interact with the program
        while i < 104:
            process.stdin.write(str(i).encode() + b'\n')
            process.stdin.flush()
            output = process.stdout.readline().decode()
            process.stdout.flush()
            tokens = output.split(":")
            ans = tokens[2].strip()
            ans_list.append(ans)
            i += 1

        ans_str = "".join(ans_list)
        print(ans_str)
    except Exception as e:
        print(f"An error occurred: {e}")



# Example usage:
program_name = "nc"  # Replace with the name of the program you want to launch
arg1 = "83.136.250.92"
arg2 = "36076"
launch_program(program_name, arg1, arg2)

