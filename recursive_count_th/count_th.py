'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
#     count = 0

    # Edge case 1
    # if len(word) == 0:
    #     return count

    # # Edge case 2
    # if len(word) == 2:
        # if word[0] == "t" and word[1] == "h":
    #         count += 1
    #         # return count
    #     # If last two are not "th" return count
    #     else: 
    #         return count
    
    # # Else if check if t and h is the first 2 letters
    # elif word[0] == "t" and word[1] == "h":
    #     count += 1
    #     # print("THAT IS")
    #     return count_th(word[1:])
    # # Else cut the first letter and check the next two.
    # else: 
    #     return count_th(word[1:])

def count_th(word):
    # If word length is less than 2 than return 0 
    if len(word) < 2:
        return 0
    
    # if t and h in word, then add it to count
    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[2:])
    # else take first word away and keep going.
    else:
        return count_th(word[1:])
    
    
word = "abthc"

print(count_th(word))