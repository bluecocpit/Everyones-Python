import time

input("Press Enter, and count for 10 secs inside your mind")
start = time.time()

input("Press Enter after 10 secs")
end = time.time()

et = end - start
print("Real time:", et, "secs")
print("Time differences:", abs(et-10), "secs")
