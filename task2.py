# What is Tokenization in NLP? Tokenization is one of the most common tasks when it comes to working with text data. Tokenization is essentially splitting a phrase, sentence, paragraph, or an entire text document into smaller units, such as individual words or terms. Each of these smaller units are called tokens then we can use the tokenizer to convert text to vector of integer numbers.
# In this week's assignment we will create a tokenizer using Python by following the instructions below:	
# 1- Create a Python class called Tokenizer.
# 2- The class construction (__init__) takes in one parameter called raw_text which is the text corpus. Use the text corpus to create two dictionaries .... .
# 3- Create a class method that return two dictionaries index_word which assigns a unique number as key to each word, word_index which is the reverse of index_word (i.e., the word in the key and the number is the value).
# 4- Create a class method called tokenize to that takes a parameter text and converts it to list of integers using the word_index dictionary.
# 5- Create a class method called reverse_tokenize to that takes a parameter vector and converts it to a string using the index_word dictionary.



class Tokenizer:
    def __init__(self,raw_text):
        self._raw_text = raw_text
    def dictionaries(self):
        file=open(self._raw_text,'r')
        read_file = file.read()
        lst = list(set(read_file.split()))
        symbols = '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~\t\n.'
        filter_list1 = [filter(lambda x:x not in symbols ,str)for str in lst]
        filter_list2 = filter(lambda x:x !='' ,filter_list1)
        length = len(filter_list2)
        index_word = {i:filter_list2[i] for i in range(length)}
        word_index = dict(map(reversed, index_word.items()))
        return index_word,word_index

def tokenize(text):
    file=open(text,'r')
    read_file = file.read()
    lst = list(set(read_file.split()))    
    symbols = '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~\t\n.'
    filter_list1 = [filter(lambda x:x not in symbols ,str)for str in lst]
    filter_list2 = filter(lambda x:x !='' ,filter_list1)
    length = len(filter_list2)
    index_word = {i:filter_list2[i] for i in range(length)}
    print(list(map(int, index_word)))

def reverse_tokenize(vector):
    file=open(vector,'r')
    read_file = file.read()
    lst = list(set(read_file.split()))    
    symbols = '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~\t\n.'
    filter_list1 = [filter(lambda x:x not in symbols ,str)for str in lst]
    filter_list2 = filter(lambda x:x !='' ,filter_list1)
    length = len(filter_list2)
    index_word = {i:filter_list2[i] for i in range(length)}
    word_index = (tuple(index_word.values()))
    print(set(word_index))

def main():
    Dict = Tokenizer('test.txt')
    print(Dict.dictionaries())
    tokenize('test.txt')
    reverse_tokenize('test.txt')
main()
