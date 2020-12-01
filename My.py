import cv2

rgb = cv2.imread("RGB.jpg")
rgb = cv2.resize(rgb, (500, 250))
cv2.imshow("rgb", rgb)

# [x,y,[b,g,r]]

b = rgb[:, :, 0]
g = rgb[:, :, 1]
r = rgb[:, :, 2]

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)

while (1):
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
