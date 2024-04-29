import tkinter as tk

class EmotionApp:
    def __init__(self, master):
        self.master = master
        master.title("Emotion to Emoji")
        master.geometry("400x350")  # Set window size

        # Create label for emoji
        self.label = tk.Label(master, text="", font=("Segoe UI Emoji", 60), bg="#f0f0f0", fg="black")
        self.label.pack(expand=True, fill="both")  # Expand label to fill the window

        # Create entry for emotion input
        self.entry = tk.Entry(master, font=("Arial", 20), bg="#f0f0f0", justify="center")
        self.entry.pack(pady=10, padx=20, fill="x")  # Add padding and fill horizontally

        # Create label for error messages
        self.error_label = tk.Label(master, text="", font=("Arial", 12), fg="red", bg="#f0f0f0")
        self.error_label.pack()

        # Bind Enter key to show emoji
        self.entry.bind("<Return>", self.show_emoji)

    def show_emoji(self, event=None):
        emotion = self.entry.get().strip().lower()
        if emotion:
            emoji = self.get_emoji(emotion)
            if emoji:
                self.label.config(text=emoji)
                self.error_label.config(text="")
            else:
                self.error_label.config(text="Emoji not found for this emotion.")
        else:
            self.error_label.config(text="Please enter an emotion.")

    def get_emoji(self, emotion):
        emojis = {
            'happy': '😊',
            'sad': '😢',
            'angry': '😠',
            'love': '❤',
            'surprise': '😮',
            'neutral': '😐',
            'birthday': '🥳'
        }
        return emojis.get(emotion, "")

def main():
    root = tk.Tk()
    app = EmotionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
