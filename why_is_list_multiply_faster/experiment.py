import timeit


def plus_way(nums):
    return nums + nums


def multiply_way(nums):
    return nums * 2


def run_test(size=100_000, loops=1000):
    nums = list(range(size))

    t_plus = timeit.timeit(
        stmt="plus_way(nums)",
        globals={"nums": nums, "plus_way": plus_way},
        number=loops,
    )

    t_mul = timeit.timeit(
        stmt="multiply_way(nums)",
        globals={"nums": nums, "multiply_way": multiply_way},
        number=loops,
    )

    return t_plus, t_mul


if __name__ == "__main__":
    t_plus, t_mul = run_test()
    print(f"nums + nums: {t_plus:.4f} seconds")
    print(f"nums * 2   : {t_mul:.4f} seconds")
