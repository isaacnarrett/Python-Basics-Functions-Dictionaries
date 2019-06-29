def strip_punctuation(str1):
    #function to take out punctuation specified in list given
    for c in punctuation_chars:
        if c in str1:
            str1 = str1.replace(c,"")
    return str1

def get_pos(str2):
    #count positive words in tweet based on text file
    count_pos = 0
    str3 = strip_punctuation(str2)
    new_lst = str3.split(" ")
    for wrd in new_lst:
        if wrd in positive_words:
            count_pos += 1
            
    return count_pos

def get_neg(str2):
    #count negative words in tweet based on text file
    count_neg = 0
    str3 = strip_punctuation(str2)
    new_lst = str3.split(" ")
    for wrd in new_lst:
        if wrd in negative_words:
            count_neg += 1
            
    return count_neg
 
def get_retweet_counts(new_lst):
    #count retweets
    retweet_lst = []
    for tweet in new_lst:
        if tweet[-6] == ",":
            nes = (tweet[-5] + tweet[-4])
            retweet_lst.append(nes)
        else:
            retweet_lst.append(tweet[-4])
    return retweet_lst

def get_reply_counts(new_lst):
    #count replies
    reply_lst = []
    for tweet in new_lst:
        reply_lst.append(tweet[-2])
    return reply_lst


#part to open and read tweets into a list for management
fileref = open("project_twitter_data.csv", "r")
new_lst = fileref.readlines()
fileref.close()
new_lst.remove(new_lst[0])

# lists of words to use
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#call counting functions
retweets = get_retweet_counts(new_lst)
reply = get_reply_counts(new_lst)

#create lists to keep track of word, sentiment count, and reply/retweets
pos_count = []
neg_count = []
net = []
counted = 0
for tweet in new_lst:
    stripped = strip_punctuation(tweet)
    x = get_pos(stripped)
    pos_count.append(x)
    neg_count.append(get_neg(stripped))
    net_val = pos_count[counted] - neg_count[counted]
    net.append(net_val)
    counted += 1

#create file to write to with final data
outfile = open("resulting_data.csv","w")
# output the header row
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
# output each of the rows:
x = 0
for tweet in new_lst:
    row_string = '{},{},{},{},{}'.format(retweets[x], reply[x], pos_count[x],neg_count[x],net[x])
    outfile.write(row_string)
    outfile.write('\n')
    x += 1
outfile.close()
