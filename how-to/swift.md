# Swift References

Swift and SwiftUI references

## Xcode

General useful resources for xCode

### Xcode Shortcuts

[Keyboard shortcuts for Xcode](https://swifteducation.github.io/assets/pdfs/XcodeKeyboardShortcuts.pdf)

| Function         | Shortcut             | Notes                             |
|------------------|----------------------|-----------------------------------|
| Auto-format      | `Ctrl + I`           | Formats currently selected code   |
| Build            | `Cmd + B`            | Build                             |
| Show/Hide Canvas | `Opt + Cmd + Enter`  | Toggle preview                    |
| Add doc comment  | `Opt + Cmd + /`      | Adds documentation comment        |
| Open Quickly     | `Cmd + Shift + O`    | Search files, types, etc and open |

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

## SwiftUI

SwiftUI references

### List Selection

Add the `selection: $selection_state` parameter into `List`.
See [link](https://www.hackingwithswift.com/quick-start/swiftui/how-to-allow-row-selection-in-a-list).

Example:

    @State var selection = Set<String>()
    let values = [
        "Tiger",
        "Lion",
        "Cheetah",
        "Leopard"
    ]
    
    var body: some View {
        NavigationView {
            List(values, id: \.self, selction: $selection) {
                Text($0)
            }
            // Canmanually set the editmode w/o a button
            .environment(\.editMode, .constant(.active))
            .toolbar {
                // or use a EditButton
                // Editmode needs to be on for selection to be activated
                EditButton()
            }
        }
    }

### Searchable

Use `.searchable(text: $searchText)` to add a search bar to any view in a `NavigationView`.
See [link](https://www.hackingwithswift.com/quick-start/swiftui/how-to-add-a-search-bar-to-filter-your-data).

Use the `.onSubmit(of: .search)` or the text state directly to interact with the search bar.
For details, see [link](https://sarunw.com/posts/searchable-in-swiftui/#onsubmit).

### List Row Seperator Insets

In iOS 16, lists have different seperator behavior. Adjust this using new alignment: `listRowSeperatorLeading` and
`listRowSeperatorTrailing`.

See [link](https://sarunw.com/posts/swiftui-list-row-separator-insets/).

Example::

    List(items) {
        HStack {
            Image("someImage")
            Text("some text")
        }
        // overrides default list separator behavior
        .alignmentGuide(.listRowSeperatorLeading) { viewDimensions in
            // custom value, 0 starts from leading edge
            return 0
        }
    }
    