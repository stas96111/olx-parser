import csv

def save_to_csv(data, filename = "output.csv"):
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(('Title', 'Price', 'Date', 'Location', 'Url'))
        writer.writerows(data)
    