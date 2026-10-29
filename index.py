import shutil

# Number of 1 GB files to create, including the original
NUM_FILES = 10

# File size: 1 GiB
CHUNK_SIZE = 1024 * 1024  # 1 MiB
NUM_CHUNKS = 1024

SOURCE_FILE = "original_1GB.txt"

print("Creating the original 1 GB text file...")

# Create the original file filled with zeros
chunk = "0" * CHUNK_SIZE

with open(SOURCE_FILE, "w", encoding="ascii") as f:
    for _ in range(NUM_CHUNKS):
        f.write(chunk)

print("Original file created!")

# Copy the original file as many times as requested
for i in range(1, NUM_FILES):
    filename = f"copy_{i}.txt"
    shutil.copyfile(SOURCE_FILE, filename)
    print(f"Created {filename}")

print(f"\nFinished! Created {NUM_FILES} files.")
print(f"Total disk space required: approximately {NUM_FILES} GiB.")
