f = [0] * (N+1)
        if N == 0:
            return 0

        elif N == 1:
            return 1

        else:
            f[0] = 0
            f[1] = 1
            for i in range(2, N+1):
                f[i] = f[i-1] + f[i-2]
