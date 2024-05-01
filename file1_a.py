while True:
    x1 = input()
    open_ = open('file3_a.txt','a')
    form_ = x1+'\n'
    open_.write(form_)
    open_.close()
    
