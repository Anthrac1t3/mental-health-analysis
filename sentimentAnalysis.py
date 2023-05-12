import matplotlib.pyplot as plt
import csv
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import threading
import time
import pandas as pd

threadLock = threading.Lock()

global status
status = {}

directory = 'results'


def display():
    time.sleep(4)
    #for thread, status in status.items():
    #    print(f"Status: {status}")
    while threading.active_count() > 2:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        for value in status.values():
            print(value)

    return


def sanitizeText(df):
    charactersToRemove = ['"', "'"]

    # Remove undefined Unicode characters from the specified column
    df.iloc[:, 2] = df.iloc[:, 2].apply(lambda x: ''.join([
        c for c in x if c.isprintable() and c not in charactersToRemove]))

    return df


def loadCSV(fileName):
    df = pd.read_csv(fileName, header=None, names=['time_stamp','tweet_id','content','author'], usecols=[0,1,2,3], encoding='utf-8')
    df['mood'] = ""

    return sanitizeText(df)


def processCSV(fileName):
    global status

    filePath = os.path.join(directory, fileName)

    with threadLock:
        status[threading.current_thread().ident] = "Loading " + str(filePath)

    fileOutPath = os.path.join(directory, "analyised-"+fileName)

    df = loadCSV(filePath)
    df = df.reset_index()

    for i in df.index:
        #Update current status
        if i % 100 == 0:
            with threadLock:
                status[threading.current_thread().ident] = "Row " + str(i) + " of file " + str(filePath)

        #Preform the sentiment analysis
        analysis = TextBlob(df.loc[i, 'content'])
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            df.loc[i, 'mood'] = "positive"# Append "positive" mood to the end of the row
        elif polarity < 0:
            df.loc[i, 'mood'] = "negative" # Append "negative" mood to the end of the row
        else:
            df.loc[i, 'mood'] = "neutral" # Append "neutral" mood to the end of the row

    with threadLock:
        status[threading.current_thread().ident] = "Writing to " + str(fileOutPath)

    df.to_csv(fileOutPath, encoding='utf-8', index=False)

    with threadLock:
        status[threading.current_thread().ident] = "Completed " + str(filePath)


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

#for fileName in os.listdir(directory):
    #generateImages(fileName)

print("I'm done!")