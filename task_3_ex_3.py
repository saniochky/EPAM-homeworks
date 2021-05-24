"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
import argparse
import fnmatch
import stat as st
from os import walk, stat


def finder(path, pattern):
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    founded_files = []

    for info in walk(path):
        for file in info[2]:
            if fnmatch.fnmatch(file, pattern):
                founded_files.append((info[0] + f"/{file}").replace('\\', '/'))

    return founded_files


def display_result(file_paths):
    """Displays founded file paths and file's permissions."""
    counter = 0

    for file_path in file_paths:
        print(file_path, st.filemode(stat(file_path).st_mode))
        counter += 1

    print(f'Found {counter} file(s).')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    parser.add_argument('-p', type=str)

    args = parser.parse_args()
    display_result(finder(args.path, args.p))


if __name__ == '__main__':
    main()
