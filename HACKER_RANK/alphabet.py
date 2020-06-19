import string

def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    L = ["-".join(alpha[i:size][::-1] + alpha[i:size][1:]).center(width, "-") for i in range(size)]
    print("\n".join(L[::-1] + L[1:]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
