def count(n):
    if n==0:
        return

    count(n-1)
    print(n)

count(5)