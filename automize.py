import os
import random
import subprocess
import csv

NUM_SIMS       = 1
SEL_BLOCK      = 100      # change s every 100 sims
DEM_BLOCK      = 1000    # change demography every 1000 sims
SEED           = 42       # for reproducibility

SEL_FILE       = "selection.txt"
DEM_FILE       = "demography.txt"
OUTPUT_DIR     = "/home/tkeseli/Data/SELAM_results"
LOG_FILE       = os.path.join(OUTPUT_DIR, "run_log.csv")



random.seed(SEED)
os.makedirs(OUTPUT_DIR, exist_ok=True)
subprocess.run(["make"], check=True)


n_sel_blocks = 1 #NUM_SIMS // SEL_BLOCK
n_dem_blocks = 1 #NUM_SIMS // DEM_BLOCK

sel_coeffs = [random.uniform(0.005, 0.1) for _ in range(n_sel_blocks)]
dem_vals = [6 + 200*i for i in range(9)]

with open(LOG_FILE, "w", newline="") as logf:
    csv.writer(logf).writerow(["run", "sel_block", "s", "dem_block", "m"])

def update_selection(s: float):
    with open(SEL_FILE, 'r') as f:
        parts = f.read().strip().split()
    parts[-2] = f"{1 - s/2:.6f}"
    parts[-1] = f"{1 - s:.6f}"
    with open(SEL_FILE, 'w') as f:
        f.write("  ".join(parts) + "\n")

def update_demography(m: int):
    with open(DEM_FILE, 'r') as f:
        lines = f.readlines()
    fields = lines[0].strip().split()
    fields[-2] = str(m)
    fields[-1] = str(m + 1)
    lines[0] = "  ".join(fields) + "\n"
    with open(DEM_FILE, 'w') as f:
        f.writelines(lines)


        
#loops
for i in range(1, NUM_SIMS + 1):
    sel_block = (i - 1) // SEL_BLOCK
    dem_block = (i - 1) // DEM_BLOCK
    s = sel_coeffs[sel_block]
    m = dem_vals[dem_block]

    
    if (i - 1) % SEL_BLOCK == 0:
        update_selection(s)
    if (i - 1) % DEM_BLOCK == 0:
        update_demography(m)


    print(f"Run {i}/{NUM_SIMS}  |  sel_block={sel_block} (s={s:.6f})  |  dem_block={dem_block} (m={m})")


    gen_dir = os.path.join(OUTPUT_DIR, f"generation_{m}")
    os.makedirs(gen_dir, exist_ok=True)


    subprocess.run([
        "./SELAM",
        "-d", DEM_FILE,
        "-s", SEL_FILE,
        "-o", "output.txt",
        "-h",
        "-c", "1", "0.01"
    ], check=True)


    result = subprocess.run(
        ["./SELAM_STATS", "-i", "ss.txt", "-a", "0.00001"],
        capture_output=True, text=True, check=True
    )


    tag = f"s{sel_block:02d}_d{dem_block:02d}"
    fn  = f"result_{i:05d}_{tag}.txt"
    out_path = os.path.join(gen_dir, fn)
    with open(out_path, "w") as out_f:
        out_f.write(result.stdout)

    open("ss.txt", "w").close()