from pathlib import Path

file_extension = input("What filetype to search for (ignore '.'): ").replace(".", "")
directory_to_search = input("What directory to search in (from root): ")

file_names = []

for path in Path(f"/{directory_to_search}").rglob(f"*.{file_extension}"):
    file_names.append(path.name)

print(f"Files with .{file_extension} extension: \n{file_names}")