import os
import shutil
from concurrent.futures import ThreadPoolExecutor

NUM_FILES = 10
FILE_SIZE = 1024**3  # 1 GiB

SOURCE_FILE = "original_1GB.txt"

print("Creating files...")

# Create a sparse file (may not allocate physical disk space for zeros)
with open(SOURCE_FILE, "wb") as f:
    f.truncate(FILE_SIZE)

def create_copy(i):
    filename = f"copy_{i}.txt"
    shutil.copyfile(SOURCE_FILE, filename)
    return filename

# Copy files concurrently
with ThreadPoolExecutor(max_workers=4) as executor:
    for filename in executor.map(create_copy, range(1, NUM_FILES)):
        print(f"Created {filename}")

print(f"\nFinished creating {NUM_FILES} files.")
print(f"Logical total size: {NUM_FILES} GiB")
