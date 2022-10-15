# How To?

My personal notes on how-to's, to avoid re-googling and re-reading docs for common issues.

## Usage

See [index](index.md) for a linked index.

### Updating `index.md`

The index is auto-generated using `scripts/index.py` from markdown files in the `how-to/how-to` subdirectory.

Run the following to update the index.

    python scripts/index.py

### Adding to Markdown files

Best practice is to use pycharm's auto-formatting. The `index.py` uses regexes to very roughly parse the files and makes
a few key assumptions.

In particular:

- There should be an empty line after each header
- The line immediately after this empty line is considered the `summary`
- Any special characters in the header **may** break the auto-generated hyperlinks.
