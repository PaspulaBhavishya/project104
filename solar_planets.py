import cv2
img = cv2.imread("solar-system.jpg")
#cv2.imshow("output",img)
#cv2.waitKey(0)
cv2.putText(
    img,
    "Sun",
    (100,60),
    fontFace = cv2.FONT_HERSHEY_COMPLEX,
    fontScale = 0.5,
    color = (255,255,255)
)
cv2.putText(
    img,
    "Mercury",
    (120,190),
    fontFace = cv2.FONT_HERSHEY_COMPLEX,
    fontScale = 0.4,
    color = (255,255,255)
)
cv2.putText(
    img,
    "Venus",
    (200,170),
    fontFace = cv2.FONT_HERSHEY_COMPLEX,
    fontScale = 0.4,
    color = (255,255,255)
)
cv2.putText(
    img,
    "Earth",
    (300,160),
    fontFace = cv2.FONT_HERSHEY_COMPLEX,
    fontScale = 0.4,
    color = (255,255,255)
)
cv2.putText(
    img,
    "Mars",
    (390,160),
    fontFace = cv2.FONT_HERSHEY_COMPLEX,
    fontScale = 0.4,
    color = (255,255,255)
)
cv2.putText(
    img,
    "Jupiter",
    (580,40),
    fontFace = cv2.FONT_HERSHEY_COMPLEX,
    fontScale = 0.4,
    color = (255,255,255)
)
cv2.putText(
    img,
    "Saturn",
    (790,110),
    fontFace = cv2.FONT_HERSHEY_COMPLEX,
    fontScale = 0.4,
    color = (255,255,255)
)
cv2.putText(
    img,
    "Uranus",
    (975,130),
    fontFace = cv2.FONT_HERSHEY_COMPLEX,
    fontScale = 0.4,
    color = (255,255,255)
)
cv2.putText(
    img,
    "Neptune",
    (1120,130),
    fontFace = cv2.FONT_HERSHEY_COMPLEX,
    fontScale = 0.4,
    color = (255,255,255)
)
cv2.imshow("output",img)
cv2.waitKey(0)