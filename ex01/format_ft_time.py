from time import time, strftime, localtime

time_epoch = time()
print(f"Seconds since January 1, 1970: {time_epoch:,.4f} or {time_epoch:.2e} in scientific notation")
print(strftime("%b %d %Y", localtime()))
