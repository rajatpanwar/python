def print_formatted(n):
    for i in range(1, n+1):
        print('{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}'.format(i, w=len(bin(n))-2))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
