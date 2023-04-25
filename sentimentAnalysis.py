import csv
from textblob import TextBlob

# Load CSV file
csv_file_path = "results/test.csv"  # Replace with your CSV file path
tweets = []
with open(csv_file_path, "r") as csvfile:
    reader = csv.reader(csvfile)
    rows = []
    for row in reader:
        tweet = row[2]  # Extract content from the 3rd column (index 2)
        analysis = TextBlob(tweet)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            row.append("positive")  # Append "positive" mood to the end of the row
        elif polarity < 0:
            row.append("negative")  # Append "negative" mood to the end of the row
        else:
            row.append("neutral")  # Append "neutral" mood to the end of the row
        rows.append(row)
    csvfile.close()

# Write results to the same CSV file
with open(csv_file_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        writer.writerow(row)

print("Sentiment analysis completed. Results saved to", csv_file_path)
