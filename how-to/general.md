# General References

General notes and references that don't yet warrant a separate file.

## Cheat Sheets

Shortcuts and syntax cheat sheets

### Pycharm

Pycharm references

#### Pycharm Shortcuts

See [pycharm keyboard shortcuts](https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html).

#### Pycharm Source Code Navigation

See [pycharm source code navigation](https://www.jetbrains.com/help/pycharm/navigating-through-the-source-code.html).

#### Pycharm Terminal PowerShell Execution Policy (Windows)

Run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted` in PowerShell

On Windows, Pycharm terminal may show a warning that running scripts is disabled due to system policy.

### Vimium Shortcuts

See [vimium shortcuts](https://github.com/philc/vimium/blob/master/README.md).

### Markdown Cheat Sheet

See [markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/).

## General Issues

General issues and solutions

### Monorepo Frontend+Backend Project Setup With Jetbrains IDEs

When prototyping Frontend+Backend projects, the backend might need to be placed in a subdirectory of the frontend, to
allow
for nextJS python serverless functions to import from the backend.

Having multiple '.idea' directories in the same project directory can cause issues with the IDEs.

The solution is to keep the backend's '.idea' outside of the 'frontend' directory, and to add the 'frontend/backend'
directory as a content root in the backend project.

See [stackoverflow answer](https://stackoverflow.com/questions/53592343/how-do-i-use-pycharm-and-webstorm-in-the-same-project-simultaneously)