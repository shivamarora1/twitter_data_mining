import json
import data_extract
import preprocess
import matplotlib.pyplot as plt
import numpy as np

FILE_NAME = 'data.json'

def process_result_list(list_1):
    list_x=[]
    list_y=[]
    for element in list_1:
        list_x.append(element[0])
        list_y.append(element[1])
    return list_x,list_y

def plot_graphs(word_counter,hashtags_counter,mentions_counter):
    plt.rcdefaults()
    fig_1,ax_1 = plt.subplots()
    fig_1,ax_2 = plt.subplots()
    fig_1,ax_3 = plt.subplots()

    # Displaying the Output Graph
    word_graph_x, word_graph_y = process_result_list(word_counter)
    hashtags_graph_x, hashtags_graph_y = process_result_list(hashtags_counter)
    mentions_graph_x, mentions_graph_y = process_result_list(mentions_counter)

    ax_1.barh(word_graph_x, word_graph_y, align='center',color='green', ecolor='black')
    ax_2.barh(hashtags_graph_x, hashtags_graph_y, align='center',color='green', ecolor='black')
    ax_3.barh(mentions_graph_x, mentions_graph_y, align='center',color='green', ecolor='black')

    ax_1.set_xlabel('Twitter Word Frequency')
    ax_1.set_ylabel('Words')

    ax_2.set_xlabel('Twitter Word Frequency')
    ax_2.set_ylabel('#HashTags')

    ax_3.set_ylabel('@Mentions')
    ax_3.set_xlabel('Twitter Word Frequency')

    plt.show()


# 1. Extract the data with particular keyword
data_extract.retrieve_keyword_tweet('#python') #Extract data with #python keyword

# 2. After extracting data to the data.json file then perform preprocessing and plot the graphs
# word_counter,hashtags_counter,mentions_counter = preprocess.count_frequency(FILE_NAME)
# plot_graphs(word_counter,hashtags_counter,mentions_counter)
