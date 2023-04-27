import matplotlib.pyplot as plt
import csv
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import threading
import time

threadLock = threading.Lock()

global status
status = {}

directory = 'data'


def display():
    #for thread, status in status.items():
    #    print(f"Status: {status}")
    while threading.active_count() > 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        for value in status.values():
            print(value)
        time.sleep(1)

    return


def processCSV(fileName):
    global status
    
    filePath = os.path.join(directory, fileName)

    with open(filePath, "r", encoding="utf-8") as csvfile:  # Specify encoding as utf-8
        reader = csv.reader(csvfile)
        rows = []
        for i, row in enumerate(reader):
            with threadLock:
                status[threading.current_thread().ident] = "Row " + str(i) + " of file " + str(filePath)
            if i == 0:
                row.append("mood")
                rows.append(row)
            else:
                analysis = TextBlob(row[2])
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
    with open(filePath, "w", newline="", encoding="utf-8") as csvfile:  # Specify encoding as utf-8
        writer = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)


def generateImages(fileName):
    tweet_list = []

    filePath = os.path.join(directory, fileName)

    with open(filePath, "r", encoding="utf-8") as csvfile:  # Specify encoding as utf-8
        reader = csv.reader(csvfile)

        # Data visualization - Bar chart for sentiment analysis results
        sentiment_count = {"positive": 0, "negative": 0, "neutral": 0}
        for i, row in enumerate(reader):
            if i > 0:
                if i%1000 == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Processing line {i} of {filePath}")

                sentiment_count[row[-1]] += 1
                tweet_list.append(row[2])

    tweet_text = " ".join(tweet_list)

    sentiment_labels = list(sentiment_count.keys())
    sentiment_values = list(sentiment_count.values())

    png_file_path = filePath + "-sentiment-graph.png"

    print("Generating bar graph...")

    plt.bar(sentiment_labels, sentiment_values)
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Analysis Results')
    plt.savefig(png_file_path)

    png_file_path = filePath + "-wordcloud.png"

    print("Bar graph generation complete!")

    print("Generating word cloud...")

    # Data visualization - Word Cloud for tweet text
    wordcloud = WordCloud(width=800, height=400, max_words=150).generate(tweet_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Tweet Text')
    plt.savefig(png_file_path)

    print("Word cloud generation complete!")

    plt.cla()
    plt.clf()


### MAIN BODY ###


threads = []

for fileName in os.listdir(directory):
    thread = threading.Thread(target=processCSV, args=(fileName,))
    threads.append(thread)
    thread.start()

displayThread = threading.Thread(target=display)
displayThread.start()

for thread in threads:
    thread.join()

displayThread.join()

for fileName in os.listdir(directory):
    generateImages(fileName)

print("I'm done!")