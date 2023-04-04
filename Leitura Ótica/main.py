while True:
    try:
        N = int(input())
        A = 0
        B = 0
        C = 0
        D = 0
        E = 0
        for i in range(N):
            A, B, C, D, E = [int(x) for x in input().split()]

            if (A <= 127 and B > 127 and C > 127 and D > 127 and E > 127):
                print("A")
            elif (A > 127 and B <= 127 and C > 127 and D > 127 and E > 127):
                print("B")
            elif (A > 127 and B > 127 and C <= 127 and D > 127 and E > 127):
                print("C")
            elif (A > 127 and B > 127 and C > 127 and D <= 127 and E > 127):
                print("D")
            elif (A > 127 and B > 127 and C > 127 and D > 127 and E <= 127):
                print("E")
            else:
                print("*")
    except EOFError:
        break



