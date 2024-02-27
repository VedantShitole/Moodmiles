# gui.py

import tkinter as tk
from tkinter import ttk
import data_processing
import analysis
from sliders import *
from data_recording import record_data  # Importing the record_data function

def show_main_window():
    # GUI code to create and display the main window
    root = tk.Tk()
    root.title("Mood Tracker")
    root.geometry("400x300")
    
    # Create a canvas
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar
    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the widgets
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')
    label = tk.Label(root, text="Mood Tracker", font=("Helvetica", 16))
    label.pack(pady=10)

    # Create sliders
    running_distance_slider = create_running_distance_slider(root)
    mood_slider = create_mood_slider(root)
    happiness_slider = create_happiness_slider(root)
    satisfaction_slider = create_satisfaction_slider(root)
    lithium_toxicity_slider = create_lithium_toxicity_slider(root)
    tremors_slider = create_tremors_slider(root)

    # Button to record data
    record_button = tk.Button(root, text="Record Data", command=lambda: record_data(
    running_distance_slider.get(),
    mood_slider.get(),
    happiness_slider.get(),
    satisfaction_slider.get(),
    lithium_toxicity_slider.get(),
    tremors_slider.get()
    ))
    record_button.pack(pady=10)

    
    # Update the canvas scroll region
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Button to open analysis window
    analysis_button = tk.Button(root, text="Open Analysis", command=show_analysis_window)
    analysis_button.pack(pady=5)

    root.mainloop()

def show_analysis_window():
    # Function to create and display the analysis window
    analysis_window = tk.Toplevel()
    analysis_window.title("Analysis")
    analysis_window.geometry("400x300")

    # Add widgets for analysis (you can customize this part)
    analysis_label = tk.Label(analysis_window, text="Analysis Window")
    analysis_label.pack(pady=10)

    # Example: Button to close the analysis window
    close_button = tk.Button(analysis_window, text="Close", command=analysis_window.destroy)
    close_button.pack(pady=5)
    # Perform analysis or visualization with the recorded data here

    analysis_window.mainloop()