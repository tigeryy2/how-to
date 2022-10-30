# Swift References

Swift and SwiftUI references

## Xcode

General useful resources for xCode

### Xcode Shortcuts

[Keyboard shortcuts for Xcode](https://swifteducation.github.io/assets/pdfs/XcodeKeyboardShortcuts.pdf)

| Function    | Shortcut   | Notes                           |
|-------------|------------|---------------------------------|
| Auto-format | `Ctrl + I` | Formats currently selected code |
| Build       | `Cmd + B`  | Build                           |

## General Resources

General useful resources for Swift and SwiftUI

### `hackingwithswift.com`

Homepage: [`hackingwithswift.com`](https://www.hackingwithswift.com/).
Hacking With Swift homepage.
See also: [`100 days of swiftui`](https://www.hackingwithswift.com/100/swiftui)

### SwiftLint

Linting tool for `Swift` and `SwiftUI`.
See [how to use swiftlint](https://medium.com/developerinsider/how-to-use-swiftlint-with-xcode-to-enforce-swift-style-and-conventions-368e49e910)

For xCode integration:

1. Go to Project>Target
2. Click `Build Phases`
3. Add `Run Script Phase` using the `+` in the top left
4. Paste the following script into the box. SwiftLint should then run automatically.

Script:

    # optionally add "bin" locations to path
    export PATH="$PATH:/usr/local/bin/usr/local/bin"
    if which swiftlint >/dev/null; then
    swiftlint
    else
    echo "warning: SwiftLint not installed, download from https://github.com/realm/SwiftLint"
    fi
