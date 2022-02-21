import numpy as np


def create_n_numbers_with_sum_s(n: int, s: float):
    nums = []
    r_n = np.random.rand()
    nums.append(r_n * s)
    for _ in range(n - 2):
        r_n = np.random.rand()
        nums.append((s - sum(nums)) * r_n)
    nums.append(s - sum(nums))
    np.random.shuffle(nums)
    return nums


if __name__ == "__main__":
    print(" --- Check functions --- ")
    print(create_n_numbers_with_sum_s(5, 10))
