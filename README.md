# libraryManager

Comprehensive library manager for Python projects.  
Supports **directory backup & restore**, and **filesystem tools** like create/remove folders, copy files/directories, list files, and get file names.

---

## Installation

```bash
pip install libraryManager
```

## Importing

```bash
from libraryManager import LibraryManager, BackupError, RestoreError
```

# Initialize library manager for a target directory

```bash
lm = LibraryManager(target_dir="services", backup_root=".backup")
```

# ---------- Backup & Restore ----------

# Check if backup exists

```bash
if lm.has_backup():
    print("Backup is available")
```

# Clear backup

```bash
lm.clear_backup()
```

# Create a snapshot backup

```bash
try:
    lm.backup()
except BackupError as e:
    print("Backup failed:", e)
```

# Restore from backup

```bash
try:
    lm.restore()
except RestoreError as e:
    print("Restore failed:", e)
```

# ---------- Filesystem Tools ----------

# Make directory (including parents)

```bash
lm.make_dir("services/new_folder")
```

# Remove directory recursively

```bash
lm.remove_dir("services/old_folder")
```

# Copy single file to a directory

```bash
lm.copy_file_to("example.txt", "services/new_folder")
```

# Copy entire directory

```bash
lm.copy_dir_to("services/source", "services/destination")
```

# List files in a directory

```bash
files = lm.list_files("services")
print(files)
```

# Get filename from path

```bash
filename = lm.get_filename("/home/user/file.txt")
print(filename)  # "file.txt"
```

# Get name without extension

```bash
name = lm.get_name("/home/user/file.txt")
print(name)  # "file"
```

## Exceptions

- BackupError → Raised when backup fails

- RestoreError → Raised when restore fails

- LibraryManagerError → Base exception for library manager

## Documentation Summary

| Method                                                  | Description                            |
| ------------------------------------------------------- | -------------------------------------- |
| `__init__(target_dir, root="/", backup_root=".backup")` | Initialize LibraryManager              |
| `has_backup()`                                          | Returns True if backup exists          |
| `clear_backup()`                                        | Clears backup directory                |
| `backup()`                                              | Create snapshot backup                 |
| `restore()`                                             | Restore snapshot                       |
| `make_dir(path)`                                        | Create folder recursively              |
| `remove_dir(path)`                                      | Remove folder recursively              |
| `copy_file_to(src, dst)`                                | Copy file to destination folder        |
| `copy_dir_to(src, dst)`                                 | Copy folder recursively                |
| `list_files(path)`                                      | List files in folder                   |
| `get_filename(path)`                                    | Get file name from path                |
| `get_name(path)`                                        | Get file/folder name without extension |
