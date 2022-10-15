"""
Generate a formatted index.md for all markdown files in a directory.
"""
import os
import re
from collections import namedtuple
from pathlib import Path

Header = namedtuple("Header", ["level", "name", "first_line"])


def get_md_in(directory: Path | str) -> [Path]:
    """
    Given path to some directory, returns list of all markdown files within


    :param directory: Some folder
    :type directory: Path | str
    :return: List of markdown files
    :rtype: list
    """
    if type(directory) is str:
        directory = Path(directory)

    if not (directory.exists() and directory.is_dir()):
        raise AttributeError(f"Provided path `{directory}` does not exist or is not a folder")

    markdown_files: [Path] = []
    for path in os.listdir(directory):
        if str(path).split(".")[1] == "md":
            markdown_files.append(os.path.join(directory, path))

    return markdown_files


def get_headers_from(file: Path | str) -> [Header]:
    """
    Grab headers from markdown file


    :param file: Path to markdown file
    :type file: Path
    :return: List of headers
    :rtype: list
    """
    headers: list[Header] = []

    markdown: [str] = open(file).read()

    # capture 1 or more `#` at the very start of the file, or right after a newline
    # capture the line of text immediately following the `#`s
    # optionally capture the two lines after
    if matches := re.findall(r"(^|\n)(#+)(.*)(\n\n[^#\n\r]*)?", markdown):
        for match in matches:
            # find header level
            level = match[1].count("#")

            # if the two lines after were found, save.
            if len(match) > 3:
                summary = match[3].strip()
            else:
                summary = None
            headers.append(Header(level, match[2].strip(), summary))
    return headers


def main():
    markdown_files = get_md_in(os.path.join("..", "how-to"))

    headers: dict[Path, list[Header]] = {}
    for file in markdown_files:
        headers[file] = get_headers_from(file)

    print(headers)


if __name__ == '__main__':
    main()
