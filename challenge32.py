#challenge 32

def main():

    score =0
    name1 = input("Enter first name : ")
    name2 = input("Enter second name : ")
    names = name1+name2

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    restcharacters = ''
    for char in alphabets:
        if char not in 'aeiou' and char not in 'friends':
            restcharacters = char + restcharacters

    for char in names:
        if char in 'aeiou':
            score+=5
        if char in 'friends':
            score+=10
        if char in restcharacters:
            score+=1
    

    if score>100    :
        print("Congratulations you are a best friend, Score = ",score)
    else:
        print("Your friendship score : ",score  )




if __name__ == "__main__":
    main()
