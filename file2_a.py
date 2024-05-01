import time
while True:
    # here first operation       
    open_ = open('file3_a.txt','r') 
    storeList = open_.read().split("\n")
    open_.close()
    print(storeList)
    time.sleep(3)
    for key,value in enumerate(storeList):
        if value.strip() == 'hi':
            print("Yes, from first operation")
            new_content = []
            for key2,value2 in enumerate(storeList):
                if key2 == key:
                    pass
                else:
                    new_content.append(value2)
            open_2 = open('file3_a.txt','w')
            for value3 in new_content:
                open_2.write(value3+'\n')
            open_2.close()
        else:
            print('No, from first operation')
