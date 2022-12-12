import tkinter as tk
from tkinter import messagebox
import requests

# Create the main window
window = tk.Tk()
window.title("Proxy Checker")

# Create a function to check if a proxy is working
def check_proxy(proxy):
    try:
        # Use the requests library to send a request to a website using the proxy
        response = requests.get('http://www.example.com', proxies={'http': proxy, 'https': proxy})

        # If the request was successful, the proxy is working
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        # If there was an error, the proxy is not working
        return False

# Create a function to check the proxy when the "Check" button is clicked
def on_check():
    # Get the proxy entered by the user
    proxy = entry.get()

    # Check if the proxy is working
    if check_proxy(proxy):
        # If the proxy is working, show a success message
        messagebox.showinfo("Success", "The proxy is working!")
    else:
        # If the proxy is not working, show an error message
        messagebox.showerror("Error", "The proxy is not working.")

# Create a text entry field for the user to enter a proxy
entry = tk.Entry(window)
entry.pack()

# Create a button to check the proxy
check_button = tk.Button(window, text="Check", command=on_check)
check_button.pack()

# Start the main event loop
window.mainloop()
