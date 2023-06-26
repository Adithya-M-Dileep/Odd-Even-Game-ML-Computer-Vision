import mediapipe as mp


class handDetector():
    def __init__(self):
        self.mpHand = mp.solutions.hands
        self.hands = self.mpHand.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        self.results = self.hands.process(img)
        return img

    def findPosition(self, img, handNo=0):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
        return lmList


hd = handDetector()
tip = [8, 12, 16, 20]


def getHandReading(img):
    img = hd.findHands(img)
    lmList = hd.findPosition(img)
    res = 0
    if lmList:
        final = []
        if lmList[4][1] > lmList[3][1]:
            final.append(1)
        else:
            final.append(0)

        for id in tip:
            if lmList[id][2] < lmList[id-2][2]:
                final.append(1)
            else:
                final.append(0)
        res = sum(final)
    return res
