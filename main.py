import re
import tkinter as tk
from tkinter import messagebox
import threading

def clean_transcript(transcript):
    # Remove HTML tags
    clean_text = re.sub('<[^<]+?>', '', transcript)
    # Ensure there is a space after each sentence
    clean_text = re.sub(r'(?<=[.!?])\s*(?=[A-Za-z])', ' ', clean_text)
    # Replace multiple spaces with a single space
    clean_text = re.sub('\s+', ' ', clean_text).strip()
    return clean_text

def save_cleaned_transcript_thread():
    # Get the text from the input box and start the cleaning and saving in a new thread
    transcript_content = text_input.get("1.0", "end-1c")
    threading.Thread(target=clean_and_save, args=(transcript_content, on_save_complete)).start()

def clear_input():
    # Clear the input text box
    text_input.delete('1.0', tk.END)

def on_save_complete():
    # This function will be called in the main thread after the cleaning and saving is done
    clear_input()
    messagebox.showinfo("Success", "The cleaned transcript has been saved!")

def clean_and_save(transcript_content, callback):
    cleaned_transcript = clean_transcript(transcript_content)
    with open('cleaned_transcript.txt', 'w') as f:
        f.write(cleaned_transcript)
    # Schedule the callback to run in the main thread
    root.after(0, callback)

# Set up the GUI
root = tk.Tk()
root.title("Transcript Cleaner")

text_input = tk.Text(root, height=25, width=60)
text_input.pack()

save_button = tk.Button(root, text="Clean and Save Text", command=save_cleaned_transcript_thread, height=2, width=20, padx=7, pady=5)
save_button.pack()

root.mainloop()
