name = "Amitkumar"
nameshort = name[0:5] #start from 0 index and end on 4th index excluding 5th index
print(nameshort)
nameshort = name[:4] # start from 0 index and end on 3rd index with excluding 4th index [0:4]
print(nameshort)
nameshort = name[4:] # start from 4th index and end on 8th index without excluding 8th index [4:8]
print(nameshort)

#slicing value with skiping value
slicing = "AmazoneBasics" 
slicing_value = slicing[1:6:3]
print(slicing_value)