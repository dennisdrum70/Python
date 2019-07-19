def igpay(pgword):

    vowels = ['a','e','i','o','u']
    vowel_append = 'way'
    const_append = 'ay'
    if pgword[0] not in vowels:
        #constant
        pig_latin_word = pgword[1:] + pgword[0] + const_append
        return pig_latin_word
    else:
        #vowel
        pgword = pgword + vowel_append
        return pgword


def numerus(RomanNumber):
    rndic={"i":1,"v":5,"x":10,"l":50,"c":100,"m":1000}
    
    print(RomanNumber)
    print (rndic["i"])

    lc=0
    total=0
    print(len(RomanNumber))

    while lc < len(RomanNumber):
#        if lc == len(RomanNumber):

        if lc == 0:
            print("first type around")
        else:
            prev = RomanNumber[lc-1]
            curr = RomanNumber[lc]
            print("next loop {0} and {1}".format(prev,curr))
            if rndic[prev] < rndic[curr]:
                print ("hello")
                total = total + (rndic[curr] - rndic[prev])
                lc = lc + 1
#            elif lc == len(RomanNumber): 
#                print("dealing with the last")
#                total = total + rnvalue[rnlist.index(curr)]
#                print (total)
            else: 
                total = total + rndic[prev]
                print(total)
            
        print(total)
        
        
        lc = lc + 1




testnum='xv'
final=numerus(testnum)
print (final)
testnum='mmxiv'
numerus(testnum)

#word = 'pig'
#word = igpay(word)
#print(word)