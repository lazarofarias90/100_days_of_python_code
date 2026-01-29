# def calculate_love_score(name1, name2):
    
#     score1 = 0
#     score2 = 0
    
#     name1_len = len(name1)
#     name2_len = len(name2)
    
#     for index in range(name1_len):
#         if "t" or "r" or "u" or "e" in name1:
#             score1 += 1
    
#     for index in range(name2_len):
#         if "t" or "r" or "u" or "e" in name2:
#             score1 += 1
    
#     for index in range(name1_len):
#         if "l" or "o" or "v" or "e" in name1:
#             score2 += 1
            
#     for index in range(name2_len):
#         if "l" or "o" or "v" or "e" in name2:
#             score2 += 1
    
#     total_score = "score1" + "score2"
#     print(total_score)
    
# calculate_love_score("Kanye West", "Kim Kardashian")

def calculate_love_score(name1, name2):
    
    combined_names = (name1 + name2).lower()
    
    score1 = 0
    score2 = 0
    
    for char in "true":
        score1 += combined_names.count(char)
    
    for char in "love":
        score2 += combined_names.count(char)
    
    love_score = str(score1) + str(score2)
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")