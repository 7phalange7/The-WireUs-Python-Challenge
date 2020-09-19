#challange 1

from ast import literal_eval

def datatype(x):
    
    try:
        y = str(type(literal_eval(x)))
    except (ValueError, SyntaxError):
        return "String"
        
        
    switcher = { 
      
        "<class 'int'>": "Integer",
        "<class 'float'>": "Float",
        "<class 'complex'>": "Complex",
        "<class 'list'>": "List",
        "<class 'tuple'>": "Tuple",
        "<class 'range'>": "Range",
        "<class 'dict'>": "Dictionary",
        "<class 'set'>": "Set",
        "<class 'frozenset'>": "Frozen Set",
        "<class 'bool'>": "Boolean",
        "<class 'bytes'>": "Bytes",
        "<class 'bytearray'>": "Byte Array",
        "<class 'memoryview'>": "Memory View",
    } 
    
    return switcher.get(y, str(type(literal_eval(x))))


# Main program
x = input("Enter value of any datatype : ")
print("The data type is : ",datatype(x))
