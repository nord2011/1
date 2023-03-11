
#def is_Polid(word):
    #for index in range(len(word)//2):
        #if word[index] != word[-index- 1]:
            #return False
    #return True
    
#word = input("Палиндрой")
  
  

#is_Polid(word)
      


#if is_Polid(word) == True:
    #print("запалиндролил")
#elif is_Polid(word) == False:
    #print("нет \n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!")

def polid(word,index):
    
    if index > len(word)//2:
        return("это полиндром")
    elif word[index] != word[-index-1]:
        return("не полидром")
    elif word[index] == word[-index-1]:
        return(polid(word,index+1))




word = input("введите слово чтобы заполиндроить\n")

print (polid(word,0))






