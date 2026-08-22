#!/usr/bin/env python3
import os

EXTENSIONS = {'.py', '.ts', '.tsx', '.js', '.jsx', '.json', '.yaml', '.yml', '.md', '.sql'}
EXCLUDED = {'.git', 'node_modules', 'dist', 'build', '.venv', '__pycache__'}

total_loc = 0
file_count = 0

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in EXCLUDED]
    for file in files:
        _, ext = os.path.splitext(file)
        if ext.lower() in EXTENSIONS:
            fp = os.path.join(root, file)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    total_loc += len(lines)
                    file_count += 1
            except Exception:
                pass

print(f"Total Scanned Files: {file_count}")
print(f"Total Lines of Code (LOC): {total_loc:,}")
if total_loc >= 100_000:
    print(f"SUCCESS: Project satisfies 100,000+ LOC goal! ({total_loc:,} lines)")
else:
    print(f"WARNING: Current LOC is {total_loc:,} lines.")
