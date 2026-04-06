from typing import List, Tuple


def input_int(prompt: str, min_value: int = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Nhập >= {min_value}")
                continue
            return value
        except:
            print("Sai, nhập số nguyên")


def input_vector(m: int, prompt: str) -> List[int]:
    while True:
        try:
            arr = list(map(int, input(prompt).split()))
            if len(arr) != m:
                print(f"Cần {m} số")
                continue
            return arr
        except:
            print("Sai định dạng")


def input_matrix(n: int, m: int, name: str) -> List[List[int]]:
    print(f"\nNhập {name}:")
    matrix = []
    for i in range(n):
        matrix.append(input_vector(m, f"P{i}: "))
    return matrix


class Deadlock:
    def __init__(self, available, allocation, request):
        self.available = available
        self.allocation = allocation
        self.request = request
        self.n = len(allocation)
        self.m = len(available)

    def detect(self) -> Tuple[bool, List[int]]:
        work = self.available[:]
        finish = [False] * self.n

        for i in range(self.n):
            if all(x == 0 for x in self.allocation[i]):
                finish[i] = True

        while True:
            found = False
            for i in range(self.n):
                if not finish[i] and all(self.request[i][j] <= work[j] for j in range(self.m)):
                    for j in range(self.m):
                        work[j] += self.allocation[i][j]
                    finish[i] = True
                    found = True
            if not found:
                break

        dead = [i for i in range(self.n) if not finish[i]]
        return len(dead) > 0, dead

    def show(self):
        print("\nAvailable:", self.available)
        print("Allocation:")
        for i in range(self.n):
            print(f"P{i}: {self.allocation[i]}")
        print("Request:")
        for i in range(self.n):
            print(f"P{i}: {self.request[i]}")


def main():
    print("=== DEADLOCK DETECTION ===")
    n = input_int("Số tiến trình: ", 1)
    m = input_int("Số tài nguyên: ", 1)

    available = input_vector(m, "Available: ")
    allocation = input_matrix(n, m, "Allocation")
    request = input_matrix(n, m, "Request")

    dl = Deadlock(available, allocation, request)
    dl.show()

    is_dead, dead_list = dl.detect()

    if is_dead:
        print("BẾ TẮC!")
        print("Các tiến trình:", dead_list)
    else:
        print("Không có bế tắc")


if __name__ == "__main__":
    main()