import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import plot_confusion_matrix
%matplotlib inline
import csv
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load CSV file, change the file path
csv_file_path = "C:/Users/lappu/Downloads/alone.csv"
tweets = []
with open(csv_file_path, "r", encoding="utf-8") as csvfile:  # Specify encoding as utf-8
    reader = csv.reader(csvfile)
    rows = []
    tweet_text = ''
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
        tweet_text += tweet + ' '  # Concatenate all tweet texts for word cloud
    csvfile.close()
# Write results to the same CSV file
'''with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:  # Specify encoding as utf-8
    writer = csv.writer(csvfile)
    for row in rows:
        writer.writerow(row)'''

print("Sentiment analysis completed. Results saved to", csv_file_path)

# Data visualization - Bar chart for sentiment analysis results
sentiment_count = {"positive": 0, "negative": 0, "neutral": 0}
for row in rows:
    sentiment = row[-1]  # Get the sentiment from the last column of the row
    sentiment_count[sentiment] += 1

sentiment_labels = list(sentiment_count.keys())
sentiment_values = list(sentiment_count.values())

plt.bar(sentiment_labels, sentiment_values)
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Analysis Results')
plt.show()

# Data visualization - Word Cloud for tweet text
wordcloud = WordCloud(width=800, height=400, max_words=150).generate(tweet_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Tweet Text')
plt.show()