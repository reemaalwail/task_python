# What is Tokenization in NLP? Tokenization is one of the most common tasks when it comes to working with text data. Tokenization is essentially splitting a phrase, sentence, paragraph, or an entire text document into smaller units, such as individual words or terms. Each of these smaller units are called tokens then we can use the tokenizer to convert text to vector of integer numbers.
# In this week's assignment we will create a tokenizer using Python by following the instructions below:
# 1- Create a Python class called Tokenizer.
# 2- The class construction (__init__) takes in one parameter called raw_text which is the text corpus. Use the text corpus to create two dictionaries .... .
# 3- Create a class method that return two dictionaries index_word which assigns a unique number as key to each word, word_index which is the reverse of index_word (i.e., the word in the key and the number is the value).
# 4- Create a class method called tokenize to that takes a parameter text and converts it to list of integers using the word_index dictionary.
# 5-Create a class method called reverse_tokenize to that takes a parameter vector and converts it to a string using the index_word dictionary.


with open('test.txt', 'r') as f:
    row_text=f.read()
class Tokenizer:
    def __init__(self,row_text,filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'):
        self.row_text = row_text
        self.filters = filters
    def clean_text(self, text):
        self.text = text
        self.text = self.row_text
        text = (self.text).lower()
        symbols = self.filters
        for i in text:
            if i in symbols:
                text= text.replace(i,' ')
        return text  # return the clean text

    def tokenizer(self, text):
        word_index = {}
        index_word = {}
        self.text = text
        text_list=(self.text).split()
        unique=list(set(text_list))
        for index in range(len(unique)):
            word_index[unique[index]]=index
            index_word[index]=unique[index]

        return (word_index, index_word)
        
    def tokenize(self, text):
        self.text = text
        self.text = self.row_text
        vector = []
        text = (self.text).lower()
        symbols = self.filters
        for i in text:
            if i in symbols:
                text= text.replace(i,' ')
        text_list=(text).split()
        unique=list(set(text_list))
        filter_list1 = [filter(lambda x:x not in symbols ,str)for str in unique]
        filter_list2 = filter(lambda x:x !='' ,filter_list1)
        length = len(filter_list2)
        index_word = {i:filter_list2[i] for i in range(length)}
        vector.append(index_word.keys())

        return vector

    def reverse_tokenize(self, vector):        
        self.vector = vector
        text = self.vector
        word_list = []
        self.text = text
        self.text = self.row_text
        text = (self.text).lower()
        symbols = self.filters
        for i in text:
            if i in symbols:
                text= text.replace(i,' ')
        text_list=(text).split()
        unique=list(set(text_list))
        filter_list1 = [filter(lambda x:x not in symbols ,str)for str in unique]
        filter_list2 = filter(lambda x:x !='' ,filter_list1)
        length = len(filter_list2)
        index_word = {i:filter_list2[i] for i in range(length)}
        word_index = dict(map(reversed, index_word.items()))
        word_list.append(word_index.keys())

        return text

tokenizer = Tokenizer(row_text)
# print(tokenizer.tokenizer(row_text))
print(tokenizer.tokenize(row_text))
print(tokenizer.reverse_tokenize(row_text))

