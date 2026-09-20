#create a dictionery of Hindi words where the values are their English translations.give the user look up words

words={"namasthe":"Hello",
       "danyavad":"Thankyou",
       "kya":"what"

}
search=words.get(input("Enter the word you want to get the english word :  "))
print("English Translated : "+ search)