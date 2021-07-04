class TrieNode:

    def __init__(self,data):

        self.data = data
        self.next = [0] * 26
        self.wordEnd = 0
        self.suggest = []

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getIndex(self,char):
        return ord(char) - ord('a')

    def getNode(self,data=""):
        return TrieNode(data)

    def insertKey(self,key):
        child = self.root

        for char in key:
            ind = self.getIndex(char)

            if not child.next[ind]:
                child.next[ind] = self.getNode(char)


            child = child.next[ind]
            child.suggest.append(key)

        child.wordEnd = True

    def searchKey(self,key):

        child = self.root
        for char in key:
            ind = self.getIndex(char)

            if child.next[ind]:
                child = child.next[ind]
            else:
                return False
        if child.wordEnd == True:
            return True
        else:
            return False

    def searchSuggestion(self,key):
        child = self.root

        for char in key:
            ind = self.getIndex(char)

            if child.next[ind]:
                child = child.next[ind]
                child.suggest.sort()
                print(child.suggest[0:3])
            else:
                print([])
                return False




def main():

    tri = Trie()

    string = ["hey", "height", "home", "hope", "hoping", "hoppp"]

    # list = string.split()
    for i in string:
        tri.insertKey(i)

    print(tri.searchKey('hey'))
    print(tri.searchKey('home'))
    print(tri.searchKey('homee'))
    print(tri.searchKey('hoping'))
    print(tri.searchKey('hopinge'))
    print(tri.searchKey('hoppp'))
    tri.searchSuggestion("hope")


main()