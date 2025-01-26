#!/usr/bin/env python3

from pwn import * 

def run_test_cases(program_name, num_test_cases):
    # Create a subprocess to run the other program
    conn = remote('94.237.54.116', 52950)
    conn.recvuntil(b'Are you ready? (y/n)', drop=False)
    conn.send(b'y\n')
    data = conn.recvuntil(b'Ok then! Let\'s go!', drop=False)
    my_dict = {'GORGE' : 'STOP', 'FIRE' : 'ROLL', 'PHREAK' : 'DROP'}

    while True:
        data = conn.recv()
        data = data.decode("utf8")
        print(data)
        if 'GORGE' in data or 'FIRE' in data or 'PHREAK' in data:
            lines = data.split('\n')
            tokens = lines[0].split(',')
            response = []
            for token in tokens:
                t = token.strip()
                response.append(my_dict[t])

            res = '-'.join(response)
            res_bytes = res.encode('utf8')
            conn.send(res_bytes + b'\n')
        elif 'HTB' in data:
            print(data)
            break

run_test_cases('nc', 100)

