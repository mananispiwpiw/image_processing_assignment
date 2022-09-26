import cv2

img = cv2.imread("resources/lena.png")
hpf = img - cv2.GaussianBlur(img, (21, 21), 3)+127

cv2.imshow("original lena", img)
cv2.imshow("hpf lena", hpf)

# cv2.waitkey is used to display
# the image continuously
# if you provide 1000 instead of 0 then
# image will close in 1sec
# you pass in milli second
cv2.waitKey(0)
cv2.destroyAllWindows()
