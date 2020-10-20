class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.end=False
        self.word=[]

class Trie:
    def __init__(self):
        self.root=TrieNode()


def insert(root,key):
    cur=root
    for i in range(len(key)):
        if key[i].islower():
            continue
        
        idx=ord(key[i])-ord('A')
        
        if cur.children[idx]==None:
            cur.children[idx]=TrieNode()

        cur=cur.children[idx]
    cur.end=True        
    cur.word.append(key)

def display(root):
    if root.end:
        root.word.sort()
        for i in root.word:
            print(i,end=' ')

    for i in range(26):
        if root.children[i]:
            display(root.children[i])        


def search(root, key):
    cur=root
    for i in key:
        pos=ord(i)-ord('A')
        if cur.children[pos]==None:
            print('No match found',end=' ')
            return
        cur=cur.children[pos]
    display(cur)

def printAllWords(arr,pattern):
    t=Trie() 
    for i in arr:
        insert(t.root,i)
    search(t.root,pattern)

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        pattern=input()
        printAllWords(arr,pattern)
        print()