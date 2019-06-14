def temp_convert(var):/home/aditep/softwares/Test
    try:
        return int(var)
    except ValueError as e:
        print("the argument does cantain number\n",e.args)

temp_convert("xyz")