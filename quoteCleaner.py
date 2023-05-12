import pandas as pd
import os
import csv
import random


def remove_undefined_unicode_and_quotes(input_file, output_file):
    charactersToRemove = ['"', "'"]

    # Read input .csv file using pandas
    df = pd.read_csv(input_file, header=0, encoding='utf-8')
    # Remove undefined Unicode characters from the specified column
    df.iloc[:, 2] = df.iloc[:, 2].apply(lambda x: ''.join([
        c for c in x if c.isprintable() and c not in charactersToRemove]))

    # Write cleaned data to output .csv file
    df.to_csv(output_file, encoding='utf-8', index=False)

    print("Quotes removed from column 3. Updated data written to", output_file)


def remove_first_column(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = [row[1:] for row in reader]

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Successfully removed the first column and saved the modified data in {output_file}.")


def replace_tweet_id(input_file, output_file):
    used_ids = set()
    rows = []

    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            original_tweet_id = row['tweet_id']
            while True:
                random_number = random.randint(10000, 99999999)
                if random_number not in used_ids:
                    used_ids.add(random_number)
                    row['tweet_id'] = str(random_number)
                    rows.append(row)
                    break

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Successfully replaced the 'tweet_id' column with unique random numbers and saved the modified data in {output_file}.")


filesToClean = ["analyised-aloner_clean"]

# Create the upload directory if it does not exist
if not os.path.exists('upload'):
    os.makedirs('upload')

for file in filesToClean:
    # Input and output file paths
    inputFile = 'upload/' + file + '.csv'
    outputFile = 'upload/' + file + '_mod.csv'

    # Call the function to remove undefined Unicode characters and double quotes
    #remove_undefined_unicode_and_quotes(inputFile, outputFile)
    #remove_first_column(inputFile, outputFile)
    replace_tweet_id(inputFile, outputFile)
