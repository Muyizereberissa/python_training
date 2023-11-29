sentence = "The quick brown fox jumps over the lazy dog"

word_list = sentence.split()

result = ""


for word in word_list:

 if len(word) % 2 == 0:
     result += word.upper() + " "

 else:

    result += word.lower() + " "
    print(result.strip()),                                                                          0