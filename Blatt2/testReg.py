def increment(array, index):
    if index == len(array):
        return
    if array[index] == 0:
        array[index] = 1
    else:
        array[index] = 0
        increment(array, index + 1)


def main():
    reg = [0, 0, 0, 0]
    for run in range(16):
        reg_start = reg.copy()
        count = 0
        while True:
            count += 1
            tmp = reg.copy()
            reg[0] = (reg[0] + reg[1] + reg[3]) % 2
            reg[1] = tmp[0]
            reg[2] = tmp[1]
            reg[3] = tmp[2]
            if reg == reg_start:
                break

        print(reg_start)
        print("Period length: %d" % count)
        increment(reg, 0)


if __name__ == '__main__':
    main()
