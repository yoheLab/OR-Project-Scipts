import time
def print_progress(x, y):
    print(f"Aligning query {x} out of {y}", end="\r", flush=True)

# Example usage:
total_steps = 100
for step in range(1, total_steps + 1):
    print_progress(step, total_steps)
    # Simulate some processing time
    time.sleep(0.05)

# Print a newline character after completing the progress
print()