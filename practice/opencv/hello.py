import cv2

img = cv2.imread("images/logo.jpg")
cv2.rectangle(img, (100,100), (200, 200), (0, 255, 255), 3)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 200, 200)
cv2.imshow("Gray", gray)
cv2.imshow("Edges", edges)

print(img.shape)
print(img.dtype)
print(img.size)
cv2.waitKey(0)
cv2.destroyAllWindows()