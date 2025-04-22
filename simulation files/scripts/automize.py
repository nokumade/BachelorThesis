import subprocess
import os

output_dir = "/mnt/c/Users/timur/Documents/SELAM_results"
os.makedirs(output_dir, exist_ok=True)

subprocess.run(["make"])

# Run the simulation 1000 times
for i in range(1, 1000):
    print(f"Run {i}/1000")

    # Run SELAM
    subprocess.run([
        "./SELAM",
        "-d", "demography500.txt",
        "-s", "selection.txt",
        "-o", "output.txt",
        "-h",
        "-c", "1", "0.01"
    ])

    # Run SELAM_STATS
    result = subprocess.run(
        ["./SELAM_STATS", "-i", "ss.txt", "-a", "0.00001"],
        capture_output=True,
        text=True
    )

    output_path = os.path.join(output_dir, f"result_{i}.txt")
    with open(output_path, "w") as f:
        f.write(result.stdout)

    open("ss.txt", "w").close()


    if result.stderr:
        print(f"[Warning] Error in run {i}:")
        print(result.stderr)