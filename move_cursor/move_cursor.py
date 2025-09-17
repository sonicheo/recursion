import pyautogui
import time

# Delay between movements (in seconds)
interval = 5 * 60  # 5 minutes

# Movement offset in pixels
move_offset = -10  # Move 10 pixels left

print("Mouse mover started. Press Ctrl+C to stop.")

try:
    while True:
        # Get current mouse position
        x, y = pyautogui.position()
        
        # Move left
        pyautogui.moveTo(x + move_offset, y, duration=0.1)

        # Optional short delay
        time.sleep(0.5)

        # Move back to original position
        pyautogui.moveTo(x, y, duration=0.1)

        print(f"Moved mouse at {time.strftime('%H:%M:%S')}")

        # Wait for the next cycle
        time.sleep(interval)

except KeyboardInterrupt:
    print("\nMouse mover stopped.")
