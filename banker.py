from typing import List, Tuple


def input_int(prompt: str, min_value: int = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Nhập số >= {min_value}")
                continue
            return value
        except:
            print("Nhập sai, hãy nhập số nguyên.")


def input_vector(m: int, prompt: str) -> List[int]:
    while True:
        try:
            arr = list(map(int, input(prompt).split()))
            if len(arr) != m:
                print(f"Phải nhập {m} số")
                continue
            if any(x < 0 for x in arr):
                print("Không được âm")
                continue
            return arr
        except:
            print("Sai định dạng")


def input_matrix(n: int, m: int, name: str) -> List[List[int]]:
    print(f"\nNhập {name}:")
    matrix = []
    for i in range(n):
        row = input_vector(m, f"P{i}: ")
        matrix.append(row)
    return matrix


class Banker:
    def __init__(self, available, max_need, allocation):
        self.available = available
        self.max_need = max_need
        self.allocation = allocation
        self.n = len(allocation)
        self.m = len(available)
        self.need = self.calc_need()

    def calc_need(self):
        need = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                if self.allocation[i][j] > self.max_need[i][j]:
                    raise ValueError("Allocation > Max")
                row.append(self.max_need[i][j] - self.allocation[i][j])
            need.append(row)
        return need

    def is_safe(self) -> Tuple[bool, List[int]]:
        work = self.available[:]
        finish = [False] * self.n
        seq = []

        while len(seq) < self.n:
            found = False
            for i in range(self.n):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(self.m)):
                    for j in range(self.m):
                        work[j] += self.allocation[i][j]
                    finish[i] = True
                    seq.append(i)
                    found = True
            if not found:
                return False, []
        return True, seq

    def request(self, pid, req):
        for j in range(self.m):
            if req[j] > self.need[pid][j]:
                print("Vượt quá Need")
                return False
            if req[j] > self.available[j]:
                print("Không đủ tài nguyên")
                return False

        # thử cấp
        for j in range(self.m):
            self.available[j] -= req[j]
            self.allocation[pid][j] += req[j]
            self.need[pid][j] -= req[j]

        safe, seq = self.is_safe()

        if safe:
            print("Cấp phát OK")
            print("Chuỗi an toàn:", seq)
            return True
        else:
            # rollback
            for j in range(self.m):
                self.available[j] += req[j]
                self.allocation[pid][j] -= req[j]
                self.need[pid][j] += req[j]
            print("Không an toàn → từ chối")
            return False

    def show(self):
        print("\nAvailable:", self.available)
        print("Allocation:")
        for i in range(self.n):
            print(f"P{i}: {self.allocation[i]}")
        print("Max:")
        for i in range(self.n):
            print(f"P{i}: {self.max_need[i]}")
        print("Need:")
        for i in range(self.n):
            print(f"P{i}: {self.need[i]}")


def main():
    print("=== BANKER ===")
    n = input_int("Số tiến trình: ", 1)
    m = input_int("Số tài nguyên: ", 1)

    available = input_vector(m, "Available: ")
    allocation = input_matrix(n, m, "Allocation")
    max_need = input_matrix(n, m, "Max")

    banker = Banker(available, max_need, allocation)
    banker.show()

    safe, seq = banker.is_safe()
    if safe:
        print("Hệ thống AN TOÀN")
        print("Chuỗi:", seq)
    else:
        print("KHÔNG AN TOÀN")

    while True:
        print("\n1. Request")
        print("0. Thoát")
        ch = input("Chọn: ")

        if ch == "0":
            break
        elif ch == "1":
            pid = input_int("PID: ", 0)
            req = input_vector(m, "Request: ")
            banker.request(pid, req)
            banker.show()


if __name__ == "__main__":
    main()