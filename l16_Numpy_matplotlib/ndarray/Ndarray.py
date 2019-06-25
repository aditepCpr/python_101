import numpy as np

aray = np.array(range(3,7))
araya = np.array([[1,2],[3,4]])
print(aray)
print(araya)

print(aray.shape) # (4,) 	รูปร่างของอาเรย์
print(aray.size) # 4 	จำนวนสมาชิกในอาเรย์
print(aray.ndim) #  1 	จำนวนมิติของอาเรย์

print(araya.shape) # ได้ (2, 2)
print(araya.size) # ได้ 4
print(araya.ndim) # ได้ 2

print(np.size(araya))
print(np.shape(araya))
print(np.ndim(araya))

print('#'*30)
# array 3D
araye = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(araye)
print(araye.shape)
print(araye.size)
print(araye.ndim)

print('#'*30)
# ดู type
araye = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arayu = np.array([[1,2],[3,4,5]])
print(araye.dtype) # ได้ int64
print(arayu.dtype) # ได้ object


print('#'*30)

# ดู type array
print(np.sctypes)

print('#'*30)

# เปลี่ยน type ด้วย astype()
x = np.array([3.5,4.7,9,11.3,15])
print(x) # ได้ [  3.5   4.7   9.   11.3  15. ]
print(x.astype(int)) # ได้ [ 3  4  9 11 15]
print(x.astype(str)) # ได้ ['3.5' '4.7' '9.0' '11.3' '15.0']

print('#'*30)

# การอ้างอิงถึงข้อมูลในอาเรย์

ariyu = np.array([[1,2,3],[4,5,6]])
print(ariyu[0][1]) # ได้ 2
print(ariyu[1][2]) # ได้ 6
print('#'*30)

#ใช้ [0,0]  "," ปกติ list ทำไม่ได้

print(ariyu[0,2]) # ได้ 3
print(ariyu[1,1]) # ได้ 5
print('#'*30)

# การเข้าถึงสมาชิคที่ละตัว

print(ariyu[1][:]) # ได้ [4 5 6]
print(ariyu[1,:]) # ได้ [4 5 6]


print('#'*30)


# เข้าถึงข้อมูลแนมตั้ง

print(ariyu[:,1]) # ได้ [2 5]
print(ariyu[:][1]) # ได้ [4 5 6]]   # [:][1] ไม่สามารถเข้าถึงข้อมูลแนวตั้งได้


# array 1 D
aroi = np.array([13,14,15,16,17,18,19])
print(aroi[:3]) # ได้ [13 14 15]
print(aroi[3:5]) # ได้ [16 17]
print(aroi[5:]) # ได้ [18 19]

# เลขติดลบก็แสดงถึงสมาชิกที่ไล่จากท้าย โดย -1 คือสมาชิกตัวท้ายสุด

print(aroi[-1]) # ได้ 19
print(aroi[-3:-1]) # ได้ [17 18]
print(aroi[5:-1]) # ได้ [18]

# กำหนดระยะเว้นช่วง [::-1]

print(aroi[1:4:2]) # ได้ [14 16]
print(aroi[1::2]) # ได้ [14 16 18]
print(aroi[:6:2]) # ได้ [13 15 17]
print(aroi[::2]) # ได้ [13 15 17 19]
print(aroi[::-1]) # ได้ [19 18 17 16 15 14 13]

print("#"*30)

aroy = np.array([[13,14,15,16],

                [17,18,19,20],

                [21,22,23,24]])


print(aroy[1:2,:]) # [[17 18 19 20]]
print(aroy[:,2:3])

# [[15]
#  [19]
#  [23]]

print(aroy[1:2,2:3]) # ได้ [[19]]  # [1:2] แนวนอน  [2:3] แนวตั้ง    ทับกันเท่ากับ 19

print(aroy[0:2,1:3])# ได้

# [[14 15]
#  [18 19]]


print(aroy[0,1:3]) # ได้ [14 15]

print(aroy[::2,2]) # ได้ [15 23]

print(aroy[::-1,::-1]) # ได้

# [[24 23 22 21]
#  [20 19 18 17]
#  [16 15 14 13]]

print("#"*30)

## การเขียนทับข้อมูลในอาเรย์
aruy = np.array([[2,2,2],[2,2,2],[2,2,2]])
print(aruy)
print("*"*10)
aruy[1,1] = 3
print(aruy)
print("*"*10)
## แก้ที่ละหลายๆ ตัว

aruy[1,:] = 4
print(aruy)
print("*"*10)
aruy[:,2] = 5
print(aruy)
print("*"*10)
aruy[:,:] = 6
print(aruy)
print("#"*30)

## การกระจายค่า (broadcast)

aruy[:,:] = np.array([7,8,9]) # หรือจะใช้ในรูปลิสต์ aruy[:,:] = [7,8,9] ก็ได้
print(aruy)

# [[7 8 9]
#  [7 8 9]
#  [7 8 9]]