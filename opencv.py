import cv2
import numpy as np

i = 1
while (i < 4):
    # выводим на экран изображение светофора
    frame = cv2.imread(str(i) + ".jpg")
    frame = cv2.resize(frame, (148, 365))
    cv2.imshow(str(i), frame)

    # переводим из BGR в HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    v = hsv[:, :, 2]
    
    # находим сумму красного,желтого и зеленого цвета
    red_sum = np.sum(v[0:121, 0:148])
    yellow_sum = np.sum(v[122:243, 0:148])
    green_sum = np.sum(v[244:365, 0:148])

    # отделяем красную, желтую и зеленую зону квадратами
    cv2.rectangle(frame, (0, 0), (148, 121), (0, 0, 255), 2)
    cv2.rectangle(frame, (0, 121), (148, 243), (0, 255, 255), 2)
    cv2.rectangle(frame, (0, 244), (148, 365), (0, 255, 0), 2)
    cv2.imshow("frameCopy" + str(i), frame)

    # сравниваем суммы
    print(str(red_sum) + ":" + str(yellow_sum) + ":" + str(green_sum))
    if green_sum > yellow_sum and green_sum > red_sum:
        print("green")
    elif yellow_sum > green_sum and yellow_sum > red_sum:
        print("yellow")
    elif red_sum > yellow_sum and red_sum > green_sum:
        print("red")
    else:
        print("red")

    key = cv2.waitKey(1)
    if key == ord("n"):
        i += 1
        cv2.destroyAllWindows()

    if key == ord("q"):
        break

cv2.destroyAllWindows()
