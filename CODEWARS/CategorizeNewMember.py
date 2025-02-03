def open_or_senior(data):
    i = 0 
    output = []
    
    for i in data:  #looping through the list to pick every person's data
        if i[0] >= 55 and i[1]> 7: #simple condition to find every person's category 
            output.append("Senior")
        else: 
            output.append("Open")
    return output 

                              
                              
open_or_senior([])
