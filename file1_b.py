while True:
    x2 = input()
    open_ = open('file3_b.txt','a')
    form_ = x2+'\n'
    open_.write(form_)
    open_.close()
    
