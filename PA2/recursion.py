def howManyGroups(n,m):
    if n == 0:
        return 1 # if there's no groups, the
    if m == 0 or n<0:
        return 0
    return howManyGroups(n, m-1) + howManyGroups(n-m,m)
