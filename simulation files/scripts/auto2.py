import subprocess
import os

output_dir500 = "/mnt/c/Users/timur/Documents/500"
output_dir1000 = "/mnt/c/Users/timur/Documents/1000"
output_dir1500 = "/mnt/c/Users/timur/Documents/1500"
output_dir2000 = "/mnt/c/Users/timur/Documents/2000"

huh = "/mnt/c/Users/timur/Documents/reserve"

os.makedirs(huh, exist_ok=True)

subprocess.run(["make"])

#Run the simulation 2000 times
for i in range(1, 500):
    print(f"Run {i}/2000")

    # Run SELAM
    subprocess.run([
        "./SELAM",
        "-d", "demography500.txt",
        "-s", "selection1.txt",
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
    os.makedirs(output_dir500, exist_ok=True)

    output_path = os.path.join(output_dir500, f"result_{i}.txt")
    with open(output_path, "w") as f:
        f.write(result.stdout)

    open("ss.txt", "w").close()


    #log any errors
    if result.stderr:
        print(f"[Warning] Error in run {i}:")
        print(result.stderr)

for i in range(1, 500):
    print(f"Run {i}/2000")

    # Run SELAM
    subprocess.run([
        "./SELAM",
        "-d", "demography500.txt",
        "-s", "selection03.txt",
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
    os.makedirs(output_dir1000, exist_ok=True)

    output_path = os.path.join(output_dir1000, f"result_{i + 251}.txt")
    with open(output_path, "w") as f:
        f.write(result.stdout)

    open("ss.txt", "w").close()


    if result.stderr:
        print(f"[Warning] Error in run {i}:")
        print(result.stderr)

for i in range(1, 500):
    print(f"Run {i}/2000")

    # Run SELAM
    subprocess.run([
        "./SELAM",
        "-d", "demography1500.txt",
        "-s", "selection1.txt",
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
    os.makedirs(output_dir1500, exist_ok=True)

    output_path = os.path.join(output_dir1500, f"result_{i + 752}.txt")
    with open(output_path, "w") as f:
        f.write(result.stdout)

    open("ss.txt", "w").close()



    if result.stderr:
        print(f"[Warning] Error in run {i}:")
        print(result.stderr)

for i in range(1, 500):
    print(f"Run {i}/2000")

    # Run SELAM
    subprocess.run([
        "./SELAM",
        "-d", "demography2000.txt",
        "-s", "selection07.txt",
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
    os.makedirs(output_dir2000, exist_ok=True)

    output_path = os.path.join(output_dir2000, f"result_{i + 1003}.txt")
    with open(output_path, "w") as f:
        f.write(result.stdout)

    open("ss.txt", "w").close()


    if result.stderr:
        print(f"[Warning] Error in run {i}:")
        print(result.stderr)