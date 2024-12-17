def happy_new_year(seg: int): 
    print(" " * (seg) + "<>" + " " * (seg)) 
    for i in range(2, seg + 2): 
      for j in range(i): 
        spaces = seg - j 
        if j == i - 1: 
          print(" " * spaces + "/" + "_" * (2 * j) + "\\" + " " * spaces) 
        else: 
          print(" " * spaces + "/" + " " * (2 * j) + "\\" + " " * spaces) 
    print(" " * (seg) + "||" + " " * (seg)) 
 
 
happy_new_year(4)
