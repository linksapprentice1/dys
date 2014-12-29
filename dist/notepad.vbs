Set Shell = WScript.CreateObject("WScript.Shell")
Shell.Run "notepad.exe " & WScript.Arguments.Item(0), 4, True