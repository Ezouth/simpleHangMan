 def hangMan():
    x = int(input('Pease enter an integer between 1 and 10: '))
    if x == 1:
        x = 'dog'
    if x == 2:
        x = 'funny'
    if x == 3:
        x = 'enjoyable'
    if x == 4:
        x = 'regrettably'
    if x == 5:
        x = 'however'
    if x == 6:
        x = 'unfortunate'
    if x == 7:
        x = 'morbid'
    if x == 8:
        x = 'deliberate'
    if x == 9:
        x = 'decisions'
    if x == 10:
        x = 'wonderful'
    print('Great! I have chosen your word! You will now be able to guess letters!')
    word = x
    turns = 10
    guesses = ''
    while turns > 0:         
        failed = 0
        for char in word:      
            if char in guesses:    
                print(char, end = '')    
            else:
                print("  _", end = '')     
                failed += 1    
        if failed == 0:        
            print()
            print("You won") 
            break              
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            printed = guesses
            print('Wrong')
            print("You have", + turns, 'more incorrect guesses! Choose carefully!')
            print("your guesses so far include: " + printed)
            turns -= 1        
             
        if turns == 0:           
            print("You Lose")
            break
        
        
hangMan()