import tkinter as tk
from threading import Thread
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.seconds = 0
        self.running = False
        self.display_var = tk.StringVar()
        self.display_var.set("00:00:00")
        self.display = tk.Label(root, textvariable=self.display_var, font=("Arial", 20))
        self.display.pack(pady=20)
        self.start_button = tk.Button(root, text="Start", command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_stopwatch)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_stopwatch)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        self.update_display()

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.stopwatch_thread = Thread(target=self.update_stopwatch)
            self.stopwatch_thread.start()

    def pause_stopwatch(self):
        self.running = False

    def stop_stopwatch(self):
        self.running = False
        self.seconds = 0
        self.update_display()

    def update_stopwatch(self):
        while self.running:
            time.sleep(1)
            self.seconds += 1
            self.update_display()

    def update_display(self):
        formatted_time = self.format_time()
        self.display_var.set(formatted_time)

    def format_time(self):
        minutes, seconds = divmod(self.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()


''' HELLO WORLD '''
