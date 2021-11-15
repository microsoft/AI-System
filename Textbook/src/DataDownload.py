from urllib.request import urlretrieve
import time
import tarfile

# TODO
URL_path = r""
filename = r"Data.tar.gz"

print("Please input the local folder path:")
local = input()
from_path = URL_path + "/" + filename
to_path = local + "/" + filename

print("Downloading...")
try:
    urlretrieve(from_path, to_path)
    print("Done.")
    print("Extracting...")
    try:
        with tarfile.open(to_path) as file:
            file.extractall(path = local)
        print("Done.")
        print("All Work Finished!")
    except:
        print("Failed Extraction!")
except:
    print("Invalid Path!")
    
print("Exit in 3 seconds...")
time.sleep(3)