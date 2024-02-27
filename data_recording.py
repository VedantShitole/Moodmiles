# data_recording.py

import csv

def record_data(*args):
    # Save the data to a CSV file
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(args)

# You can add more functions here for recording other types of data if needed