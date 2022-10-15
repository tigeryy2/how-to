"""
Generate a formatted index.md for all markdown files in a directory.
"""
import os
import re
from collections import namedtuple
from pathlib import Path

Header = namedtuple("Header", ["level", "name", "summary"])


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


def generate_index(markdown_directory: Path, destination_path: Path):
    markdown_files = get_md_in(markdown_directory)

    headers: dict[Path, list[Header]] = {}
    for file in markdown_files:
        relative_file_path = Path(os.path.relpath(file, start=destination_path.parent))
        headers[relative_file_path] = get_headers_from(file)

    print(headers)


def main():
    markdown_folder = Path(os.path.join("..", "how-to"))
    destination_path = Path(os.path.join("..", "index.md"))
    generate_index(markdown_folder, destination_path)


if __name__ == '__main__':
    main()
