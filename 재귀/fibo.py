def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)


# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fibo(i))