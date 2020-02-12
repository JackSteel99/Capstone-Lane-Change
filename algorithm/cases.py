import threading

def case_checker():
    pass # which case is this

caseCheck = threading.Thread(target=case_checker, args=(ls, rs, fs)) # args for left, right, front sensors
caseCheck.daemon = True
caseCheck.start()

