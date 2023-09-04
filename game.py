
# This is variables and printing
# n=5
# print(n)
# m="abc"
# print(m,n)
# y="peepee"
# u="poopoo"
# print(y,u)

# This is an if statement
# n = 10
# if n < 9:
#     print("TRUE!")
# else:
#     print("FALSE!")

# print("WINNIE POOP")


# This is a loop
# sum = 0
# prod = 1
# for i in list(range(5)):
#     sum = sum + (i + 1)
#     prod = prod * (i + 1)
# print("sum=", sum)
# print("prrod=", prod)


# This is Fibonacci numbers
# n0=0
# n1=1
# print(n0)
# print(n1)
# for i in list(range(5)):
#     f = n0 + n1
#     print(f)
#     n0 = n1
#     n1 = f

###### Pictures

# load images library
import cv2 

nextTurn = "x"
def drawfunction(event,x,y,flags,param):
    global nextTurn
    print("event", event, "x", x, "y", y)
    if event == 4:
        cv2.putText(img, nextTurn, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 7, (255, 0, 0), 10, cv2.LINE_AA)
        cv2.imshow("cat", img)

        if nextTurn == "x":
            nextTurn = "o"
        else: # if it's o then it should become x
            nextTurn = "x"


# read image file from disk
img = cv2.imread("cat.jpg", cv2.IMREAD_ANYCOLOR)

# show image in a window
cv2.imshow("cat", img)

# draw diagonal green line on the image
size = img.shape
print(size)

height=size[0]
width=size[1]

x1 = int(width/3)
print(x1) # should be 204
x2 = int(x1+x1)
print(x2) # should be 408

cv2.line(img, (x1, 0), (x1, height), (0, 255, 0))
cv2.line(img, (x2, 0), (x2, height), (0, 255, 0))
cv2.line(img, (0, 272), (width, 272), (0, 255, 0))
cv2.line(img, (0, 136), (width, 136), (0, 255, 0))

# show image again with grid lines
cv2.imshow("cat", img)
cv2.setMouseCallback("cat", drawfunction)

# wait for key press on the image
cv2.waitKey(0) 

# close the window
cv2.destroyAllWindows() # destroy all windows
