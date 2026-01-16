# why_is_list_multiply_faster/tests/test_main.py

from __future__ import annotations

import sys
import time
from typing import List, Tuple

import pytest

from why_is_list_multiply_faster.experiment import plus_way, multiply_way

"""
Time + Space Complexity (Big-O)

Let n = len(nums).

plus_way(nums)      -> nums + nums
- Time:  O(n)
- Space: O(n)   (new list of size 2n)

multiply_way(nums)  -> nums * 2
- Time:  O(n)
- Space: O(n)   (new list of size 2n)

Both are O(n). Any speed difference comes from constant factors,
not asymptotic complexity.
"""

# ---------------- configuration ----------------

# Total cases: 0..100
ALL_SIZES = list(range(0, 101))

# Visible (LeetCode-style shown cases)
VISIBLE_SIZES = {0, 1, 2, 5, 10, 50, 100}

# Timing config
TIMING_REPEATS = 5000

# Store timing results only for visible cases
BENCH: List[Tuple[int, float, float, str]] = []


# ---------------- helpers ----------------


def _avg_time_us(fn, nums, repeats=TIMING_REPEATS) -> float:
    start = time.perf_counter()
    for _ in range(repeats):
        fn(nums)
    end = time.perf_counter()
    return ((end - start) / repeats) * 1e6


def _record_visible(n: int, plus_us: float, mul_us: float) -> None:
    winner = "mul" if mul_us < plus_us else "plus"
    BENCH.append((n, plus_us, mul_us, winner))


def teardown_module(module):
    """Print LeetCode-style summary for visible cases only."""
    if not BENCH:
        return

    print("\n--- visible test case summary (avg µs per call) ---")
    print(f"repeats per measurement: {TIMING_REPEATS}")
    print("n    plus_us     mul_us   winner")
    print("--------------------------------------")

    for n, plus_us, mul_us, winner in BENCH:
        print(f"{n:<4} {plus_us:>9.3f} {mul_us:>9.3f}   {winner}")

    print("--------------------------------------")
    print(f"visible cases shown: {len(BENCH)}")
    print("hidden cases passed silently ✔")


# ---------------- tests ----------------


@pytest.mark.parametrize("n", ALL_SIZES)
def test_same_output_for_sizes_0_to_100(n: int):
    nums = list(range(n))

    out_plus = plus_way(nums)
    out_mul = multiply_way(nums)

    # correctness (all cases)
    assert out_plus == out_mul

    # timing only for visible cases
    if n in VISIBLE_SIZES:
        plus_us = _avg_time_us(plus_way, nums)
        mul_us = _avg_time_us(multiply_way, nums)
        _record_visible(n, plus_us, mul_us)


@pytest.mark.parametrize("n", ALL_SIZES)
def test_length_doubles_for_all_sizes(n: int):
    nums = list(range(n))
    out = multiply_way(nums)
    assert len(out) == 2 * len(nums)


@pytest.mark.parametrize(
    "nums",
    [
        [],  # empty
        [42],  # single element
        [1, 2, 3],  # simple
        [0, 0, 0, 0],  # repeated values
        [-3, -2, -1, 0, 1],  # negatives
        list(range(10))[::-1],  # reversed
    ],
)
def test_order_is_preserved(nums):
    out = multiply_way(nums)
    assert out == nums + nums
    assert out[: len(nums)] == nums
    assert out[len(nums) :] == nums


@pytest.mark.parametrize("n", [0, 1, 5, 10, 50, 100])
def test_original_list_not_modified(n: int):
    nums = list(range(n))
    before = nums[:]

    plus_way(nums)
    multiply_way(nums)

    assert nums == before


@pytest.mark.parametrize("n", [0, 1, 5, 10, 50, 100])
def test_space_container_grows(n: int):
    """
    Space sanity check (container only).
    True space complexity is O(n) extra for the new list.
    """
    nums = list(range(n))
    out = multiply_way(nums)

    assert sys.getsizeof(out) >= sys.getsizeof(nums)
