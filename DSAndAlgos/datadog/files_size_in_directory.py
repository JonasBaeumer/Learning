#!/bin/python3

"""
Problem:
--------

You are given a representation of a filesystem as nested Directory/File objects.
Each entry is either:

- Directory(name, [children])
- File(name, size)

You must implement:

    total_size(root, path)

This should return the total size of all files under the given path.

Rules:
------
- "/" refers to the entire filesystem
- A path may refer to:
      - a directory  → return total size of all files under it
      - a file       → return its size
      - a full path with trailing "/" or without
- If the path does not exist → return 0

Examples:
---------
total_size(root, "/")                → 8675777
total_size(root, "/home")            → 5264404
total_size(root, "/bin")             → 680768
total_size(root, "var/")             → 2730605
total_size(root, "/home/me/")        → 351040
total_size(root, "/var/log/wifi.log")→ 924818
"""


# ---------------------------------------------------------
# The classes below are provided. DO NOT MODIFY.
# ---------------------------------------------------------

class FSEntry:
    def __init__(self, name):
        self.name = name


class Directory(FSEntry):
    def __init__(self, name, *children):
        super().__init__(name)
        self.children = list(children)


class File(FSEntry):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size


# ---------------------------------------------------------
# TODO: Implement this function
# ---------------------------------------------------------
def total_size(root, path):

    def dfs(node, path_parts, onpath):
        # Case 1: file
        if isinstance(node, File):
            return node.size if onpath else 0
        
        total = 0
        for child in node.children:
            if onpath:
                total += dfs(child, path_parts, True)
            
            else:
                # Only match next path component if it exists
                if path_parts and child.name == path_parts[0]:
                    total += dfs(child, path_parts[1:], True)

        return total

    # Normalize root-only case
    if path == "/":
        return dfs(root, [], True)

    # Split and filter empty segments
    path_parts = [p for p in path.split("/") if p]

    return dfs(root, path_parts, False)


# ---------------------------------------------------------
# Input Handling (HackerRank style)
# ---------------------------------------------------------
# The real HackerRank version would construct the filesystem
# from input. For practice, we manually build the example FS.
# ---------------------------------------------------------

def build_sample_fs():
    return Directory(
        "",
        Directory(
            "home",
            Directory(
                "me",
                File("foo.txt", 416),
                File("metrics.txt", 5892),
                Directory(
                    "src",
                    File("site.html", 6051),
                    File("site.css", 5892),
                    File("data.csv", 332789)
                )
            ),
            Directory(
                "you",
                File("dict.json", 4913364)
            )
        ),
        Directory(
            "bin",
            File("bash", 618416),
            File("cat", 23648),
            File("ls", 38704)
        ),
        Directory(
            "var",
            Directory(
                "log",
                File("dmesg", 1783894),
                File("wifi.log", 924818),
                Directory(
                    "httpd",
                    File("access.log", 17881),
                    File("access.log.0.gz", 4012)
                )
            )
        )
    )


if __name__ == '__main__':
    root = build_sample_fs()

    q = int(input().strip())       # number of queries
    for _ in range(q):
        query_path = input().strip()
        print(total_size(root, query_path))
