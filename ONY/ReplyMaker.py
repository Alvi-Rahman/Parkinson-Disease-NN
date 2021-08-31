import sqlite3
import wikipedia

conn = sqlite3.connect('QandA.db')

def cleanText(string):
    string = string.replace('?','')
    string = string.replace('??','')
    string = string.replace('???','')
    string = string.replace('????','')
    string = string.replace('.','')
    string = string.replace(':','')
    string = string.replace(';','')
    string = string.replace('/','')
    string = string.replace('\'','')
    string = string.replace('  ',' ')
    string = string.replace('   ',' ')
    string = string.replace('.','')
    string = string.replace('..','')
    string = string.replace('...','')
    string = string.replace('....','')
    string = string.replace('-','')
    string = string.replace('_','')
    string = string.lower()
    return string

def searchDB(ques):
    rows = conn.execute("SELECT * FROM questions WHERE question='"+ques+"'")
    string = '-1';
    for row in rows:
        string = row[1]
    return string

def getList(query):
    return wikipedia.search(query)
def searchWIKI(word):
    lst = getList(word)
    print('are you looking for one of this topics?')
    for i in range(len(lst)):
        print(str(i+1)+". "+lst[i])
    print('\n\n\n\n')
    print('printing information for: '+lst[0])
    print('=======================================')
    page = wikipedia.page(lst[0])
    lines = page.content.split('.')
    for line in range(10):
        print(lines[line],end='.')


def main(word):
    word = cleanText(word)
    if word[0:4] == 'wiki':
        try:
            ans = searchWIKI(word[5:])
            return ans
        except:
            return "There was an error trying to parse the output."
    ans = searchDB(word)
    if ans == '-1':
        ans = "I don't know the answer. Sorry."
    return ans