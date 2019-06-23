# Closure
การซ่อน data,logic

```
The nested function was able ti access the non-local variable of the enclosing function.

```

## Nested function
``` การที่เราประกาศ function ภายใน function  
function ภายในสามารถ access  variables ภายใน function ภายนอกได้  
```
```
 A function defined inside another function
 Nested functions can access variables of the enclosing scope
```

## Non-Local variable
```
non-local variables are read only by default
we must declare them explicitly
```

### closure
```python
def myprint(msg):
# This is the outer enclosing function
    def inner_print():
    # this is the nested function
        print(msg)
    return  inner_print #ต้องมี return
```

ใช้ตอนไหน
``` 
- Avoid the use of global values
- Date hiding
- Object oriented solution 

