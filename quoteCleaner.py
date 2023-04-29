import pandas as pd
import os

def remove_undefined_unicode_and_quotes(input_file, output_file):
    charactersToRemove = ['"', "'"]

    # Read input .csv file using pandas
    df = pd.read_csv(input_file, encoding='utf-8')
    # Remove undefined Unicode characters from the specified column
    df.iloc[:, 2] = df.iloc[:, 2].apply(lambda x: ''.join([
        c for c in x if c.isprintable() and c not in charactersToRemove]))

    # Write cleaned data to output .csv file
    df.to_csv(output_file, encoding='utf-8', index=False)

filesToClean = ["depressed"]

# Create the upload directory if it does not exist
if not os.path.exists('upload'):
    os.makedirs('upload')

for file in filesToClean:
    # Input and output file paths
    inputFile = 'results/' + file + '.csv'
    outputFile = 'upload/' + file + '_clean.csv'

    # Call the function to remove undefined Unicode characters and double quotes
    remove_undefined_unicode_and_quotes(inputFile, outputFile)

    print("Quotes removed from column 3. Updated data written to", outputFile)
