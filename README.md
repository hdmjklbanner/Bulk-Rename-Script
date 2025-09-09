# Bulk Rename Script

This repository contains a Python script for bulk-renaming files in a folder. You can add a prefix, sequential numbering, or both to your filenames quickly and easily.

## Features

- Rename all files in a folder.
- Add a custom prefix to each file.
- Add sequential numbering to filenames.
- Combine prefix and numbering as needed.
- Preview changes with a dry-run mode.

## Usage

1. **Clone this repository** or download the script.

2. **Run the script:**

   ```bash
   python bulk_rename.py /path/to/folder [--prefix PREFIX] [--numbering] [--dry-run]
   ```

   - `--prefix PREFIX`: Add a prefix to each filename (optional).
   - `--numbering`: Add sequential numbering (optional).
   - `--dry-run`: Preview the changes without renaming files (optional).

### Examples

- Add prefix:

  ```bash
  python bulk_rename.py ./myfolder --prefix new_
  ```

- Add sequential numbering:

  ```bash
  python bulk_rename.py ./myfolder --numbering
  ```

- Add both prefix and numbering:

  ```bash
  python bulk_rename.py ./myfolder --prefix img_ --numbering
  ```

- Preview changes:

  ```bash
  python bulk_rename.py ./myfolder --prefix sample_ --dry-run
  ```

## License

This project is licensed under the MIT License.
