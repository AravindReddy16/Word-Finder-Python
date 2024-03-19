words=[
    ['a','l','o','b','p','i','a'],
    ['n','r','g','l','m','y','f'],
    ['e','z','a','n','a','k','l'],
    ['y','i','l','o','n','d','o'],
    ['p','a','n','i','r','m','g'],
    ['r','k','o','e','x','a','o'],
    ['e','n','u','b','l','n','e']
]
list=['dog','animal','aeroplane','king','lion','ball','fun','monkey','zebra','proxy']
wrdlst=[]
rowlst=[]
collst=[]
score=0
while True:
    try:
        if score!=10:
            print(f'Your Score: {score}')
            for row in words:
                print(row)
            print(list)
            wordind=int(input('Enter index of Word: '))-1
            for lenth in range(len(list[wordind])):
                rowind=int(input(f'Enter {lenth+1} row of Word: '))
                rowlst.append(rowind)
                colind=int(input(f'Enter {lenth+1} column of Word: '))
                collst.append(colind)
                wrdlst.append(words[rowind][colind])
            word=''.join(wrdlst)
            if word==list[wordind]:
                score+=1
                for itm in range(len(rowlst)):
                    words[rowlst[itm]][collst[itm]]='_'
                rowlst.clear()
                collst.clear()
                wrdlst.clear()
                list.remove(list[wordind])
            else:
                wrdlst.clear()
        else:
            print('You won the Game')
            print('Game Over')
            break
    except:
        print('Invalid Input...')