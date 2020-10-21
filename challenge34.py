# challenge 34

def myFunc(e):
    return e['r']


def main():
    x = int(input("How many sentences do you want in the list : "))

    sentences = []

    print("Enter the sentences : ")

    for i in range(0, x):
        s = input().lower()
        sentences.append(s)

    query = input("Enter query : ").lower()

    relevenceList = []  # [{s = "sentance",r = relevance}]

    qlist = query.split()
   
    for sentence in sentences:
        relevance = 0
        for word in sentence.split():
            if word in qlist:
                relevance += 1

        obj = {}
        obj['s'] = sentence
        obj['r'] = relevance

        relevenceList.append(obj)

    relevenceList.sort(reverse=True, key=myFunc)

    index = 1

    for i in relevenceList:
        print(index, i['s'])
        index += 1


if __name__ == "__main__":
    main()
