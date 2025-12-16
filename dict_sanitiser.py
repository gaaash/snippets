import arabic_reshaper
from bidi.algorithm import get_display



with open("C:\\Users\\Nikan\\Downloads\\persian_dict_19k.csv", 'r', encoding='UTF-8') as file :
    line = file.readlines()
for l in line:
    reshaped_text = arabic_reshaper.reshape(l)  
    new_l = get_display(reshaped_text)
    
    new_l.replace("\n","")
    
    with open("C:\\Users\\Nikan\\Downloads\\persian_dict_19k (1).csv", 'a', encoding='UTF-8') as file :
        file.write(new_l)


