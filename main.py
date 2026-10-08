#!/usr/bin/env python3
"""
CLI tool to display statistics of a directory: number of files, subdirectories,
and total size of all files. Uses only the standard library.
"""

import argparse
from pathlib import Path
import sys

def get_stats(path: Path):
    files = dirs = 0
    total_bytes = 0
    for p in path.rglob("*"):
        if p.is_file():
            files += 1
            total_bytes += p.stat().st_size
        elif p.is_dir():
            dirs += 1
    return files, dirs, total_bytes

def main():
    parser = argparse.ArgumentParser(description="Directory statistics")
    parser.add_argument("directory", nargs="?", default=".", help="Target directory")
    args = parser.parse_args()
    target = Path(args.directory).expanduser()
    if not target.exists():
        print(f"Error: {target} does not exist", file=sys.stderr)
        sys.exit(1)
    if not target.is_dir():
        print(f"Error: {target} is not a directory", file=sys.stderr)
        sys.exit(1)
    files, dirs, total = get_stats(target)
    print(f"Directory: {target.resolve()}")
    print(f"  Files: {files}")
    print(f"  Subdirectories: {dirs}")
    print(f"  Total file size: {total:,} bytes")

if __name__ == "__main__":
    main()