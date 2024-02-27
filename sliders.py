# sliders.py

import tkinter as tk

def create_running_distance_slider(parent):
    # Slider for running distance
    running_distance_slider = tk.Scale(parent, from_=0, to=100, orient="horizontal", label="Running Distance")
    running_distance_slider.pack(pady=5)
    return running_distance_slider

def create_mood_slider(parent):
    # Slider for mood
    mood_slider = tk.Scale(parent, from_=0, to=100, orient="horizontal", label="Mood")
    mood_slider.pack(pady=5)
    return mood_slider

def create_happiness_slider(parent):
    # Slider for happiness
    happiness_slider = tk.Scale(parent, from_=0, to=100, orient="horizontal", label="Happiness")
    happiness_slider.pack(pady=5)
    return happiness_slider

def create_satisfaction_slider(parent):
    # Slider for satisfaction
    satisfaction_slider = tk.Scale(parent, from_=0, to=100, orient="horizontal", label="Satisfaction")
    satisfaction_slider.pack(pady=5)
    return satisfaction_slider

def create_lithium_toxicity_slider(parent):
    # Slider for lithium toxicity
    lithium_toxicity_slider = tk.Scale(parent, from_=0, to=100, orient="horizontal", label="Lithium Toxicity")
    lithium_toxicity_slider.pack(pady=5)
    return lithium_toxicity_slider

def create_tremors_slider(parent):
    # Slider for tremors
    tremors_slider = tk.Scale(parent, from_=0, to=100, orient="horizontal", label="Tremors")
    tremors_slider.pack(pady=5)
    return tremors_slider
