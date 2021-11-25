import sys
import math
import random

acc2 = 0
acc1 = 0
stack = []
current_color = None

colors = [
    "RED",
    "BLUE",
    "PURPLE",
    "GREEN",
    "YELLOW",
    "CYAN",
    "BLACK",
    "WHITE",
    "BROWN",
    "LIME",
    "PINK",
    "ORANGE",
]

if len(sys.argv) <= 1:
    print("Among us interpreter V1")
    exit(0)
else:
    file_name = sys.argv[1]
    tokens = list(filter(
        lambda x: x != '',
        open(file_name)
        .read()
        .replace('\n', ' ')
        .split(' ')
    ))

    ip = 0
    last_who_ip = None
    user_input = ''

    while ip < len(tokens):
        command = tokens[ip]

        if command == 'VENTED':
            acc2 += 10
        elif command == 'SUSSY':
            acc2 -= 1
        elif command == 'ELECTRICAL':
            acc2 = 0
        elif command == 'WHO' or command == 'WHO?':
            last_who_ip = ip
            if stack[-1] == acc2:
                while tokens[ip] != 'WHERE' and tokens[ip] != 'WHERE?':
                    ip += 1
        elif command == 'WHERE' or command == 'WHERE?':
            if stack[-1] != acc2:
                ip = last_who_ip
        elif command in colors:
            current_color = command
        elif command == 'SUS':
            if current_color == 'RED':
                acc1 += 1
            elif current_color == 'BLUE':
                stack.append(acc1)
            elif current_color == 'PURPLE':
                stack.pop()
            elif current_color == 'GREEN':
                print(chr(stack[-1]), end='')
            elif current_color == 'YELLOW':
                while user_input == '':
                    user_input = input()
                character = user_input[0]
                user_input = user_input[1:]
                stack.append(ord(character))
            elif current_color == 'CYAN':
                for i in range(math.floor(random.random() * acc1)):
                    stack.pop()
            elif current_color == 'BLACK':
                print(stack[-1], end='')
            elif current_color == 'WHITE':
                acc1 -= 1
            elif current_color == 'BROWN':
                acc1 = stack[-1]
            elif current_color == 'LIME':
                a = stack.pop()
                stack.append(a + a)
            elif current_color == 'PINK':
                acc1 = 0
            elif current_color == 'ORANGE':
                acc1 += 10
            else:
                print(f"ERROR: unknown color: '{current_color}'")
                exit(1)
        else:
            print(f"ERROR: unknown command: '{command}'")
            exit(1)

        ip += 1
