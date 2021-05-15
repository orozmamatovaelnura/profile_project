def func(*args):
    summ=0
    for i in args:
        try:
            summ+=i
        except:
            pass
    return summ


