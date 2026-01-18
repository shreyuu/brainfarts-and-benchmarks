# How long until all dice match?

This project explores a simple but surprisingly non-intuitive probability question:

> If you roll multiple dice repeatedly,  
> how long does it take **until all dice show the same value**?

The experiment is intentionally brute-force and heavily logged to expose how
randomness behaves over repeated trials.

---

## 🔍 The Question

Suppose you roll `n` fair six-sided dice:

- Each die shows a value from 1 to 6
- Every roll is independent
- You repeat rolls **until all dice show the same number**

Questions that naturally arise:

- How many iterations does this usually take?
- How much does it vary between runs?
- How quickly does it become “rare” as the number of dice increases?
- Do we ever get lucky very early?

---

## 🧪 What This Script Does

For a chosen number of dice and simulations:

1. Rolls all dice repeatedly
2. Logs **every iteration** of every simulation
3. Stops a simulation once all dice match
4. Repeats this process many times
5. Computes summary statistics:
   - average iterations
   - minimum iterations
   - maximum iterations

Each run is fully reproducible in the sense that:

- all rolls are logged
- results can be re-parsed later for analysis

---

## ▶️ Core Logic (Conceptual)

At each iteration:

```python
rolls = [random.randint(1, 6) for _ in range(num_dice)]
```

A match occurs when:

```python
len(set(rolls)) == 1
```

That is:

- all dice landed on the same face

Once this happens, the simulation stops and reports how many iterations it took.

---

## 📁 Log Files

Every execution generates a uniquely named log file:

```
{num_dice}die_{num_runs}sim_{date_time}.txt
```

Example:

```
3die_100sim_18-01-26_12-39-32.txt
```

Each log file contains:

- simulation metadata
- every roll of every iteration
- the exact iteration where a match occurred

This makes the experiment:

- auditable
- debuggable
- analyzable after the fact

---

## 📊 Post-Processing & Visualization (`charts.ipynb`)

The accompanying Jupyter notebook:

- parses log files using regex
- converts results into a Pandas DataFrame
- visualizes behavior using multiple plots

### Included analyses:

- **Histogram** → how long matches usually take
- **Line plot** → volatility from run to run
- **Boxplot** → skewness and outliers
- **Cap-hit scatter** → how often iterations exceed a chosen threshold

This separates:

- **data generation** (Python script)
- **analysis & intuition building** (notebook)

---

## 📐 Probability Intuition (Why this grows fast)

For `n` dice:

- Probability all dice match in **one roll**:

$$
P = 6 \times \left(\frac{1}{6}\right)^n = \frac{1}{6^{n-1}}
$$

Expected number of iterations:

$$
E[\text{iterations}] = 6^{n-1}
$$

So roughly:

| Dice | Expected Iterations |
| ---- | ------------------- |
| 1    | 1                   |
| 2    | 6                   |
| 3    | 36                  |
| 4    | 216                 |
| 5    | 1296                |
| 10   | ~10 million         |

This explains why:

- small dice counts finish quickly
- larger counts explode in runtime
- extreme variance appears between runs

---

## 🧠 Why Results Vary So Much

This is a **geometric distribution**:

- Most runs finish “around” the expected value
- Some finish extremely early (lucky streaks)
- Some take far longer than average

This leads to:

- long right-tailed distributions
- large max/min gaps
- unstable averages for small sample sizes

---

## ⏱️ Time & Space Complexity (Big-O)

Let:

- `n` = number of dice
- `k` = iterations until match

### Time Complexity

- Each iteration rolls `n` dice → `O(n)`
- Total time → `O(n × k)`
- Since `k` grows exponentially, runtime grows very fast with `n`

### Space Complexity

- Active memory per iteration → `O(n)`
- Log file size → `O(n × k)` (unbounded growth)

This script prioritizes **observability**, not efficiency.

---

## ❌ What This Experiment Is NOT

- ❌ Not an optimized probability solver
- ❌ Not suitable for large dice counts
- ❌ Not bounded-memory
- ❌ Not meant for production use

It is intentionally **inefficient but transparent**.

---

## ✅ Why This Experiment Exists

This project exists to:

- build intuition about randomness
- observe exponential probability effects
- visualize variance and outliers
- practice logging and post-analysis
- answer a “what if?” question honestly

It’s not about speed — it’s about **seeing randomness in action**.

---

## ▶️ How to Run

From the project folder:

```bash
python main.py
```

Then analyze results using:

```bash
jupyter notebook charts.ipynb
```

---

## 🧠 Final Takeaway

> Even simple random processes can behave wildly.

> Expected value ≠ typical experience.

> Probability intuition is best learned by **watching randomness fail expectations**.
