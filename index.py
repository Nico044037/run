import os
import shutil
import secrets
import string
from concurrent.futures import ThreadPoolExecutor

# Configuration
NUM_FILES = 10
FILE_SIZE = 1024**3  # 1 GiB
CHUNK_SIZE = 4 * 1024 * 1024  # 4 MiB
NUM_WORKERS = 4


def random_name(length=20):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


# Create a folder with a completely random name
folder = random_name(20)
os.makedirs(folder)


# Generate random filenames
filenames = [random_name(24) + ".txt" for _ in range(NUM_FILES)]

# Create the original file
source_path = os.path.join(folder, filenames[0])


chunk = b"0" * CHUNK_SIZE

with open(source_path, "wb") as f:
    remaining = FILE_SIZE

    while remaining > 0:
        size = min(CHUNK_SIZE, remaining)
        f.write(chunk[:size])
        remaining -= size


# Copy the original file using multiple threads
def create_copy(filename):
    destination = os.path.join(folder, filename)
    shutil.copyfile(source_path, destination)
    return filename


with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    for filename in executor.map(create_copy, filenames[1:]):
        print("")

