import random
from datetime import datetime
from pathlib import Path
from tqdm import tqdm  # progress bar


def iterations_to_match(num_dice, log_file, run_number, columns=10, verbose=True):
    """
    Roll dice until all show the same value.
    Log rolls in rows of fixed column size.
    Rows grow dynamically until a match occurs.
    """
    if verbose:
        print(f"\n>>> Simulation {run_number} started")

    iterations = 0
    row_buffer = []

    with tqdm(
        desc=f"Simulation {run_number}",
        unit="iteration",
        ascii=True,
        dynamic_ncols=True,
    ) as pbar:
        while True:
            iterations += 1
            rolls = [random.randint(1, 6) for _ in range(num_dice)]
            row_buffer.append(rolls)

            # Flush row buffer if full
            if len(row_buffer) == columns:
                log_file.write(" ".join(str(r) for r in row_buffer) + "\n")
                row_buffer.clear()

            # Update tqdm with singular/plural iteration text
            pbar.set_postfix_str(
                f"{iterations} iteration{'s' if iterations != 1 else ''}"
            )
            pbar.update(1)

            # Stop when match occurs
            if len(set(rolls)) == 1:
                break

    # Flush any remaining rolls
    if row_buffer:
        log_file.write(" ".join(str(r) for r in row_buffer) + "\n")

    log_file.write(
        f"\nMatch achieved with value {rolls[0]} in {iterations} iterations.\n"
    )

    if verbose:
        print(f">>> Simulation {run_number} finished after {iterations} iterations")

    return iterations


def main():
    num_dice = int(input("Enter number of dice: "))
    num_runs = int(input("Enter number of simulations to run: "))

    results = []

    base_dir = Path(__file__).parent
    logs_dir = base_dir / "logs"
    logs_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%d-%m-%y_%H-%M-%S")
    filename = logs_dir / f"{num_dice}die_{num_runs}sim_{timestamp}.txt"

    with open(filename, "w") as log_file:
        log_file.write("Dice Matching Simulation Log\n")
        log_file.write(f"Number of dice: {num_dice}\n")
        log_file.write("Columns per row: 10\n")
        log_file.write(f"Simulations: {num_runs}\n\n")

        for run in range(1, num_runs + 1):
            iterations = iterations_to_match(num_dice, log_file, run)
            results.append((run, iterations))

    # Calculate statistics
    iteration_counts = [it for _, it in results]
    average_iterations = sum(iteration_counts) / len(iteration_counts)

    min_run, min_iterations = min(results, key=lambda x: x[1])
    max_run, max_iterations = max(results, key=lambda x: x[1])

    print("\n--- Simulation Results ---")
    print(f"Dice count: {num_dice}")
    print(f"Simulations: {num_runs}")
    print(f"Average iterations: {average_iterations:.2f}")
    print(f"Min iterations: {min_iterations} (Simulation {min_run})")
    print(f"Max iterations: {max_iterations} (Simulation {max_run})")
    print(f"\nLog file saved as: {filename}")


if __name__ == "__main__":
    main()
