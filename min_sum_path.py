#!/usr/bin/env python3

import subprocess
import numpy as  np

def solve(my_array, r, c):
    dp = [[0 for _ in range(c+1)] for _ in range(r+1)]
    dp[0][0] = my_array[0][0]
    for i in range(1, r+1):
        dp[i][0] = dp[i-1][0] + my_array[i][0]
    for j in range(1, c+1):
        dp[0][j] = dp[0][j-1] + my_array[0][j]
    for i in range(1, r+1):
        for j in range(1, c+1):
            dp[i][j] = my_array[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[r][c]
    

def run_test_cases(program_name, num_test_cases):
    # Create a subprocess to run the other program
    process = subprocess.Popen([program_name, '83.136.250.116', '32418'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
    idx = 0
    while True:
        input_data = process.stdout.readline().strip()
        if 'Test 1/100' not in input_data:
            continue
        input_data = process.stdout.readline().strip()
        r, c = map(int, input_data.split())
        input_data = process.stdout.readline().strip()
        grid = [int(x) for x in input_data.split()]
        my_array = np.array(grid).reshape(r, c, order='C')
        output = solve(my_array, r-1, c-1)
        print('tc: {} output'.format(idx), str(output))
        process.stdin.writelines(str(output) + '\n')
        process.stdin.flush()
        break


    # Run test cases
    idx = 1
    for i in range(num_test_cases - 1):
        input_data = process.stdout.readline().strip()
        input_data = process.stdout.readline().strip()
        input_data = process.stdout.readline().strip()
        r, c = map(int, input_data.split())
        input_data = process.stdout.readline().strip()
        grid = [int(x) for x in input_data.split()]
        my_array = np.array(grid).reshape(r, c, order='C')
        output = solve(my_array, r-1, c-1)
        print('tc: {} output'.format(idx), str(output))
        process.stdin.writelines(str(output) + '\n')
        process.stdin.flush()
        idx += 1


    # Close the subprocess
    input_data = process.stdout.readline().strip()    
    print(input_data)
    process.stdin.close()


run_test_cases('nc', 100)

