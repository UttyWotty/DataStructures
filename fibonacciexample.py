
class Example:
    def fib(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1

        answer = [0, 1]

        for i in range(2, n + 1):
            answer.append(answer[i - 1] + answer[i - 2])

        return answer[n]


# If we put it on a usage
solution = Example()
n = 31
print(f"The {n}-th Fibonacci number is: {solution.fib(n)}")






