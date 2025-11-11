def index(keys:list[int],values,match:function)->dict:
    """
    返回一个字典，该字典的键对应一个列表的值，该列表的值能使match(k,v)返回为真
    """

    return  {k:{v for v in values if match(k,v)}  for k in keys}
    # return {k:v for k,v in keys,values if match(k,v)} 这个是错误的，python不支持这样遍历
