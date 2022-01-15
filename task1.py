#1- Create a python function called tokenizer.
#2- The function takes in one parameter called raw_text.
#3- Then it splits the raw_text to a list of unique words.
#4- The list then passes through a filter to remove the following symbols: !"#$%&()*+,-./:;<=>?@[\\]^_{|}~\t\n`.
#5- Then create two dictionaries; index_word which assigns a unique number as key to each word, word_index which is the reverse of index_word (i.e., the word in the key and the number is the value).
#6- Return the two dictionaries.
def tokenizer(raw_text):
    file=open(raw_text,'r')
    read_file = file.read()
    lst = list(set(read_file.split()))
    symbols = '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~\t\n'
    filter_list1 = [filter(lambda x:x not in symbols ,str)for str in lst]
    filter_list2 = filter(lambda x:x !='' ,filter_list1)
    length = len(filter_list2)
    index_word = {i:filter_list2[i] for i in range(length)}
    word_index = dict(map(reversed, index_word.items()))
    return index_word,word_index
    
print(tokenizer('test.txt'))
