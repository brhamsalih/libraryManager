# Changelog

All notable changes to this project will be documented in this file.  
This project follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] - 2026-01-27

### Added

- `LibraryManager` class: first full release for file & directory management.
- Backup & Restore system (snapshot-style) for directories.
- Filesystem tools included:
  - `make_dir(path)` – create directories recursively
  - `remove_dir(path)` – remove directories recursively
  - `copy_file_to(src, dst)` – copy single file
  - `copy_dir_to(src, dst)` – copy directories recursively
  - `list_files(path)` – list all files in a directory
  - `get_filename(path)` – extract file name from path
  - `get_name(path)` – extract name without extension
- Exception handling:
  - `BackupError`
  - `RestoreError`
  - `LibraryManagerError`

### Changed

- Refactored `LibraryManager` to include all FS utilities in one interface.

### Fixed

- Improved internal path handling for both Windows and Unix.
