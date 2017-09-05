def calc(a,b):
    count=5
    try:
        count+=a/b
    except TypeError:
        count-=4
        print("type error")
    except:
        count+=27
    return count
print(str(calc("6", 4)))