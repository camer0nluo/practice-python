import random


def bit_test():
    keep_going = True
    while keep_going:
        rand_num = random.randint(0, 0xFF)
        bits = bin(rand_num)
        correct = False
        attempts = 1
        while not correct:
            answer = input(f"What is {bits.replace('0b', '').rjust(8, '0')} in decimal? ")
            attempts += 1
            if int(answer) == rand_num:
                print('*** Correct! ***')
                correct = True
            elif attempts > 3:
                print(f'The answer is: {rand_num}')
                correct = True
            else:
                print('Try again.')


def main():
    bit_test()

if __name__ == '__main__':
    main()
