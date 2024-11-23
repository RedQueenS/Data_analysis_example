import csv

def load_data(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

# Load data
data = load_data('data/genes.csv')