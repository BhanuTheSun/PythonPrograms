def recursive_fun(k):
    print("k value:",k)
    if k>0:
        result = k + recursive_fun(k-1)
        print("result inside",result)
    else:
        print("in else")
        result = 0
    return result


result = recursive_fun(3)
print("result outside",result)



