import os

strings = ["flower", "flow", "flight"]
prefix = os.path.commonprefix(strings)
print(prefix)  # Output: "fl"
