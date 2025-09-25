import time
import sys

print("Stopwatch started! Press Ctrl+C to stop.")
start = time.time()
try:
    while True:
        elapsed = int(time.time() - start)
        mins, secs = divmod(elapsed, 60)

        print(f"\r Elapsed time: {mins:02d}:{secs:02d}", 
              end="")
        
        time.sleep(1)
except KeyboardInterrupt:
    print(f"\n Stopwatch stopped at {mins:02d}:{secs:02d}")
    sys.exit()  # This ensures the program terminates completely