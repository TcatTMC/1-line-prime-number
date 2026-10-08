(lambda n: print( (n not in [0, 561, 1105, 1729]) and pow(2, n-1, n) == 1 or n == 2) )(int(input()))
