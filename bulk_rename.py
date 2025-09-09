import os
import sys

def bulk_rename(folder_path, prefix=None, use_numbering=False, dry_run=True):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort()  # sort alphabetically for deterministic numbering

    for idx, filename in enumerate(files, 1):
        name, ext = os.path.splitext(filename)
        if prefix and use_numbering:
            new_name = f"{prefix}{idx}{ext}"
        elif prefix:
            new_name = f"{prefix}{filename}"
        elif use_numbering:
            new_name = f"{idx}{ext}"
        else:
            continue  # Do nothing if neither is set

        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        print(f"Renaming: '{filename}' -> '{new_name}'")
        if not dry_run:
            os.rename(src, dst)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Bulk rename files in a folder with a prefix or sequential numbering.")
    parser.add_argument("folder", help="Path to the folder containing files")
    parser.add_argument("--prefix", help="Prefix to add to each file name", default=None)
    parser.add_argument("--numbering", action="store_true", help="Add sequential numbering to file names")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without renaming files")

    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print("The specified folder does not exist.")
        sys.exit(1)

    bulk_rename(args.folder, prefix=args.prefix, use_numbering=args.numbering, dry_run=args.dry_run)
