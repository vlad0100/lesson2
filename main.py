#var = 10
#array = [2, "info", True, "General Culture"]
#array.append(3.14) #array.appeand se foloseste pentru a adauga ceva
#print(array)




#array = ["ion"]
#print(array)





#int_array = [1, 2, 3, 4, 5, 6]
#float_array = [1.3, -2, 3.14, 5.002]
#bool_array = [True, True, False, True]
#array = sorted(array) #sorted este folosit pentru sortarea
#array.sort()  #sort este folosit pentru sortarea listei
#int_array.sort(reverse=True)
#print(int_array) #printeaza lista
#print(sorted(int_array)) #printeaza lista
#print(float_array) #printeaza lista
#print(bool_array) #printeaza lista





#list = []
#list_length = int(input("Enter list length"))

#for i in range(0, list_length):
 #   element = int(input("Enter element"))
  #  list.append(element)
#else:
  #  print(list)
 #   list.sort()
  #  list.sort(reverse=True)
  #  print(list)





#print(list[0])
#if 12 in list:
 #   print(True)
#else:
   # print(False)





#list = ["12", "231", "41", "643", "21"]
#print(list) #printeaza lista

#for i in range(0, len(list)):
 #   print(list[i]) #print list by index


#for e in list:
   # print(e) #print list by element






#tuple = ("I", "O", "N")
#print(tuple + ("M", "A", "N", "O", "L", "I"))






#int_array = [1, 2, 3, 4, 5, 6, 7, 1, 5, 6, 7]
#int_array = set(int_array)
#set_array ={1, 2, 3, 4, 5, 6, 7, 1, 5, 6, 7}
#print(set_array)
#print(int_array)






dex = {"Cod": "Python", "Extend": ".py", "Less": "3"}

print(dex.get("Cod")) #use key to display value with that

dex.update({"Less": 3}) #update value where key is Less

print(dex) #printeaza dex

for i in dex:
    print(i) #display key
    print(dex.get(i)) #display value with key (i)