import time
while True:
    # here second operation        
    open_3 = open('file3_b.txt','r') 
    storeList = open_3.read().split("\n")
    open_3.close()
    print(storeList)
    time.sleep(3)
    for key,value in enumerate(storeList):
        if value.strip() == 'hi':
            print("Yes, from second operation")
            new_content = []
            for key2,value2 in enumerate(storeList):
                if key2 == key:
                    pass
                else:
                    new_content.append(value2)
            open_4 = open('file3_b.txt','w')
            for value3 in new_content:
                open_4.write(value3+'\n')
            open_4.close()
        else:
            print('No, from second operation')
