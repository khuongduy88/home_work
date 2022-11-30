def translate_eng_vn(dictionary_data,word):
    for item in dictionary_data:
        if item == word:
            print(item, ":" ,dictionary_data[item])
#        else:
#            print(word," is not exits")

def find_word(dictionary_data,word):
    find = False
    for item in dictionary_data:
        if item == word:
            find = True
    return find


dictionary_data ={'mother':'me',
                 'father':'bo',
                 'son':'con trai'}
input_word = input("input your word : ")

if find_word(dictionary_data,input_word):
    translate_eng_vn(dictionary_data,input_word)
else:
    print(input_word," is not exits")