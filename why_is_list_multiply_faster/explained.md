# Why is `list * 2` sometimes faster than `list + list`?

This project explores a small but interesting Python behavior:

> If both `nums + nums` and `nums * 2` produce the same list,  
> why does one often run faster than the other?

This is a curiosity-driven experiment focused on **behavior, not premature optimization**.

---

## 🔍 The Question

Given a list:

```python
nums = [1, 2, 3]
```

Both of the following produce the same result:

```python
nums + nums   # [1, 2, 3, 1, 2, 3]
nums * 2      # [1, 2, 3, 1, 2, 3]
```

So naturally:

- Are they equally fast?
- If not, why?
- Is the difference real or just noise?

---

## 🧪 What Was Tested

Two simple functions were defined:

```python
def plus_way(nums):
    return nums + nums

def multiply_way(nums):
    return nums * 2
```

We tested them across **101 input sizes**:

- `n = 0` through `n = 100`
- Each test checks **correctness**
- Timing is measured but **never asserted** (tests never fail due to speed)

Only **7 visible cases** are shown (like LeetCode sample tests):

```
n = 0, 1, 2, 5, 10, 50, 100
```

The rest run silently as hidden test cases.

---

## ✅ Correctness Guarantees

Every test ensures:

- Both methods return identical output
- Output length is exactly `2 × len(nums)`
- Element order is preserved
- The original list is **not modified**
- Edge cases behave correctly:

  - empty list
  - single element
  - repeated values
  - negative numbers
  - reversed lists

---

## ⏱️ How Timing Is Measured (Important)

Timing is done **carefully** to reduce noise:

- Each method is executed **5,000 times**
- Average time per call is reported (in microseconds)
- Only **visible test cases** are timed and printed
- No assertions are made on timing (environment-dependent)

This avoids common benchmarking mistakes like:

- timing a single call
- asserting one method must always be faster

---

## 📊 Sample Output

When running:

```bash
pytest -q -s
```

You’ll see something like:

```
--- visible test case summary (avg µs per call) ---
repeats per measurement: 5000
n    plus_us     mul_us   winner
--------------------------------------
0        0.040     0.050   plus
1        0.050     0.062   plus
2        0.057     0.069   plus
5        0.072     0.075   plus
10       0.086     0.082   mul
50       0.256     0.213   mul
100      0.409     0.304   mul
--------------------------------------
visible cases shown: 7
hidden cases passed silently ✔
```

---

## 🧠 Why Small Inputs Look Weird

For very small lists (`n = 0..5`):

- Timing is dominated by:

  - Python function call overhead
  - loop overhead
  - CPU scheduling noise

So results may flip randomly.

For **larger inputs**, the actual list-copy cost dominates, and `list * 2` usually pulls ahead.

---

## 📐 Time & Space Complexity (Big-O)

Let `n = len(nums)`.

### `nums + nums`

- **Time:** `O(n)`
- **Space:** `O(n)` (new list of size `2n`)

### `nums * 2`

- **Time:** `O(n)`
- **Space:** `O(n)` (new list of size `2n`)

⚠️ Both are `O(n)`.
The difference is **constant factors**, not asymptotic complexity.

---

## 🧩 Why `list * 2` Is Often Faster

Internally (CPython):

- `list * 2`:

  - knows the final size upfront
  - allocates memory once
  - copies references in a tight loop

- `list + list`:

  - still linear
  - but involves slightly more overhead in how the result is built

This makes multiplication **often faster**, but not guaranteed in every scenario.

---

## 🧪 Space Measurement Notes

The tests include a **space sanity check** using:

```python
sys.getsizeof(list)
```

Important caveat:

- `getsizeof` measures only the list container (array of references)
- It does **not** include memory used by the elements themselves
- This check only verifies that output grows with input

True space complexity reasoning is conceptual (`O(n)`), not exact byte counting.

---

## ❌ What This Experiment Is NOT

- ❌ Not a rule to always use `list * 2`
- ❌ Not production performance advice
- ❌ Not a guarantee across Python versions
- ❌ Not a replacement for real profiling

---

## ✅ Why This Experiment Exists

This project exists to:

- build intuition about Python internals
- understand how identical results can have different costs
- practice writing **robust tests**
- experiment safely without overengineering

It’s a **brainfart worth writing down**.

---

## ▶️ How to Run

From the repo root:

```bash
pytest -q -s
```

For verbose per-test output:

```bash
pytest -vv -s
```

---

## 🧠 Final Takeaway

> Same result ≠ same cost

> Big-O ≠ real-world performance

> Measure, don’t assume.
