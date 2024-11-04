def digital_root(num):
    if num == 0:
        return 0
    else:
        return 1 + (num - 1) % 9

# input
num = int(input())

#output
print(digital_root(num))