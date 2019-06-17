# Overloading

```python
# constructor
def __init__(self, wheel=None,color=None,engine=None)
    if(wheel is not None and color is not None and engine is not None) :
        self.wheel = wheel
        self.color=color
        self.engine=engine
    elif (wheel is not None and engine is not None):
        self.wheel = wheel
        self.color = "white"
        self.engine = engine
    elif (wheel is not None):
        self.wheel = wheel
        self.color = "white"
        self.engine = "ivtech"
    else:
        self.wheel = 4
        self.color = "white"
        self.engine = "ivtech"

```
 
