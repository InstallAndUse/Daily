# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A


Keybindings
The following keybindings can be used to control Terminator:

C-S O  Split terminals Horizontally.
C-S E  Split terminals Vertically.
C-S Right  Move parent dragbar Right.
C-S Left   Move parent dragbar Left.
C-S Up  Move parent dragbar Up.
C-S Down  Move parent dragbar Down.
C-S S  Hide/Show Scrollbar.
C-S F  Search within terminal scrollback
C-S N or C-Tab
    Move to next terminal within the same tab, use Ctrl+PageDown to move to the next tab. If cycle_term_tab is False, cycle within the same tab will be disabled
C-S P or C-S Tab
    Move to previous terminal within the same tab, use Ctrl+PageUp to move to the previous tab. If cycle_term_tab is False, cycle within the same tab will be disabled
Alt+Up    Move to the terminal above the current one.
Alt+Down  Move to the terminal below the current one.
Alt+Left  Move to the terminal left of the current one.
Alt+Right Move to the terminal right of the current one.
C-S C  Copy selected text to clipboard
C-S V  Paste clipboard text
C-S W  Close the current terminal.
C-S Q  Quits Terminator
C-S X  Toggle between showing all terminals and only showing the current one (maximise).
C-S Z  Toggle between showing all terminals and only showing a scaled version of the current one (zoom).
C-Plus   Increase font size. Note: this may require you to press shift, depending on your keyboard
C-Minus  Decrease font size. Note: this may require you to press shift, depending on your keyboard
C-Zero (0) Restore font size to original setting.
F11 Toggle fullscreen
C-Su R  Reset terminal state
C-Su G  Reset terminal state and clear window
Su G Group all terminals so that any input sent to one of them, goes to all of them.
Su-S G  Remove grouping from all terminals.

= Tabs =

C-S T Open new tab
Ctrl+PageDown  Move to next Tab
Ctrl+PageUp  Move to previous Tab
C-S PageDown  Swap tab position with next Tab
C-S PageUp  Swap tab position with previous Tab

Super+t  Group all terminals in the current tab so input sent to one of them, goes to all terminals in the current tab.
Super+Shift+T  Remove grouping from all terminals in the current tab.
C-S I  Open a new window (note: unlike in previous releases, this window is part of the same Terminator process)
Super+i  Spawn a new Terminator process
