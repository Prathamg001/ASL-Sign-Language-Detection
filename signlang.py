import cv2 as cv
import mediapipe as mp
import math

cap = cv.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(min_detection_confidence=0.7)
fingertip = [4, 8, 12, 16, 20]


def Aa(list, hand_type):
    len = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
    if len < 70 and list[4][2] < list[7][2] and abs(list[4][2] - list[3][2]) > 20:
        if hand_type == 'Right':
            if list[3][1] > list[6][1]:
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and
                        list[20][2] > list[18][2] and list[4][1] > list[18][1]):
                    return True

        elif hand_type == 'Left':
            if list[3][1] < list[6][1]:
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and
                        list[20][2] > list[18][2] and list[4][1] < list[18][1]):
                    return True

    return False


def Bb(list, hand_type):
    len1 = math.hypot(list[8][1] - list[11][1], list[8][2] - list[11][2])
    if len1 < 30:
        if hand_type == 'Right':
            if (list[8][2] < list[6][2] and list[12][2] < list[10][2] and list[16][2] < list[14][2] and
                    list[20][2] < list[18][2] and list[4][1] < list[5][1]):
                return True

        if hand_type == 'Left':
            if (list[8][2] < list[6][2] and list[12][2] < list[10][2] and list[16][2] < list[14][2] and
                    list[20][2] < list[18][2] and list[4][1] > list[5][1]):
                return True

    return False


def Cc(list):
    cnt = 0
    for i in range(0, 5):
        if (abs(list[fingertip[i]][2] - list[fingertip[i] - 2][2]) < 40):
            cnt = cnt + 1
    if cnt == 5:
        len1 = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
        len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
        len3 = math.hypot(list[4][1] - list[16][1], list[4][2] - list[16][2])
        len4 = math.hypot(list[4][1] - list[20][1], list[4][2] - list[20][2])
        if (len1 > 80 and len2 > 80 and len3 > 80 and len4 > 80):
            return True

    return False


def Dd(list):
    if (list[8][2] < list[6][2] and abs(list[8][2] - list[6][2]) > 40):
        len1 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
        len2 = math.hypot(list[4][1] - list[16][1], list[4][2] - list[16][2])
        len3 = math.hypot(list[4][1] - list[20][1], list[4][2] - list[20][2])
        if len1 < 30 and len2 < 30 and len3 < 30:
            return True

    return False


def Ee(list, hand_type):
    len1 = math.hypot(list[3][1] - list[8][1], list[3][2] - list[8][2])
    len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
    if len1 > 30 and len2 > 30 and list[12][2] < list[9][2]:
        if hand_type == 'Right':
            if list[3][1] > list[6][1]:
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][
                    2] > list[18][2]
                        and list[4][1] > list[18][1]):
                    return True

        elif hand_type == 'Left':
            if list[3][1] < list[6][1]:
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][
                    2] > list[18][2]
                        and list[4][1] < list[18][1]):
                    return True

    return False


def Ff(list):
    if (list[12][2] < list[9][2] and list[16][2] < list[13][2] and list[20][2] < list[17][2] and list[12][2] < list[10][
        2]):
        if abs(list[8][1] - list[5][1]) < 40:
            len1 = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
            len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
            if len1 < 60 and len2 > 50:
                return True

    return False


def Gg(list, hand_type):
    if (abs(list[4][2] - list[6][2]) < 50):
        if (hand_type == 'Right'):
            if list[8][1] > list[5][1]:
                if (list[12][1] < list[10][1] and list[16][1] < list[14][1] and list[20][1] < list[18][1] and list[6][
                    2] < list[10][2]):
                    return True

        elif (hand_type == 'Left'):
            if list[8][1] < list[5][1]:
                if (list[12][1] > list[10][1] and list[16][1] > list[14][1] and list[20][1] > list[18][1] and list[6][
                    2] < list[10][2]):
                    return True
    return False


def Hh(list, hand_type):
    if (list[4][2] > list[6][2] and list[4][2] < list[14][2]):
        if (hand_type == 'Right'):
            if list[8][1] > list[5][1] and list[12][1] > list[9][1]:
                if (list[16][1] < list[14][1] and list[20][1] < list[18][1] and list[10][2] < list[14][2]):
                    return True

        elif (hand_type == 'Left'):
            if list[8][1] < list[5][1]:
                if (list[16][1] > list[14][1] and list[20][1] > list[18][1] and list[10][2] < list[14][2]):
                    return True

    return False


def Ii(list, hand_type):
    len = math.hypot(list[4][1] - list[17][1], list[4][2] - list[17][2])
    if list[9][2] > list[10][2] and len < 100:
        if (hand_type == 'Right'):
            if list[4][1] > list[18][1]:
                if (list[20][2] < list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][
                        2] < list[16][2]):
                        return True

        elif (hand_type == 'Left'):
            if list[4][1] < list[18][1]:
                if (list[20][2] < list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][
                        2] < list[16][2]):
                        return True

    return False


def Jj(list, hand_type):
    len = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
    if len < 50:
        if (hand_type == 'Right'):
            if list[4][1] < list[20][1] and abs(list[10][2] - list[20][2]) < 50:
                if (list[20][2] < list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][
                        2] <
                            list[16][2]):
                        return True

        elif (hand_type == 'Left'):
            if list[4][1] > list[20][1] and abs(list[10][2] - list[20][2]) < 50:
                if (list[20][2] < list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][
                        2] <
                            list[16][2]):
                        return True

    return False


def Kk(list, hand_type):
    len = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
    if len < 50 and list[8][2] < list[12][2] and abs(list[8][1] - list[12][1]) < 50 and list[8][2] < list[6][2] and \
            list[12][2] < list[10][2] and list[14][2] < list[16][2] and list[18][2] < list[20][2]:
        if (hand_type == 'Right'):
            if (list[4][1] > list[20][1]):
                return True

        elif (hand_type == 'Left'):
            if (list[4][1] < list[20][1]):
                return True

    return False


def Ll(list, hand_type):
    if abs(list[4][2] - list[2][2]) < 50 and abs(list[8][1] - list[5][1]) < 50 and list[8][2] < list[6][2] and abs(
            list[4][1] - list[10][1] > 50) and abs(list[9][2] - list[10][2]) < 20:
        if (hand_type == 'Right'):
            if (list[4][1] > list[20][1] and list[9][2] < list[12][2] and list[13][2] < list[16][2] and list[17][2] <
                    list[20][2]):
                return True

        elif (hand_type == 'Left'):
            if (list[4][1] < list[20][1] and list[9][2] < list[12][2] and list[13][2] < list[16][2] and list[17][2] <
                    list[20][2]):
                return True

    return False


def Mm(list, hand_type):
    if list[4][2] < list[18][2] and abs(list[4][2] - list[6][2]) < 50:
        len1 = math.hypot(list[4][1] - list[18][1], list[4][2] - list[18][2])
        len2 = math.hypot(list[4][1] - list[14][1], list[4][2] - list[14][2])
        if len1 < 40 and len2 < 60:
            if hand_type == 'Right':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][
                    2] >
                        list[18][2]):
                    if (list[4][1] < list[14][1]):
                        return True

            elif hand_type == 'Left':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][
                    2] >
                        list[18][2]):
                    if (list[4][1] > list[14][1]):
                        return True

    return False


def Nn(list, hand_type):
    if list[4][2] < list[14][2] and abs(list[4][2] - list[10][2]) < 50:
        len1 = math.hypot(list[4][1] - list[14][1], list[4][2] - list[14][2])
        len2 = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
        if len1 < 40 and len2 < 60:
            if hand_type == 'Right':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][
                    2] >
                        list[18][2]):
                    if (list[4][1] < list[10][1]):
                        return True

            elif hand_type == 'Left':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][
                    2] >
                        list[18][2]):
                    if (list[4][1] > list[10][1]):
                        return True

    return False


def Oo(list, hand_type):
    len1 = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
    len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
    len3 = math.hypot(list[4][1] - list[16][1], list[4][2] - list[16][2])
    len4 = math.hypot(list[4][1] - list[7][1], list[4][2] - list[7][2])
    len5 = math.hypot(list[4][1] - list[11][1], list[4][2] - list[11][2])
    len6 = math.hypot(list[4][1] - list[15][1], list[4][2] - list[15][2])
    if (len1 < 60 and len2 < 40 and len3 < 60 and abs(list[4][1] - list[3][1]) < 30
            and abs(list[8][2] - list[12][2]) < 30 and abs(list[12][2] - list[16][2] < 30) and abs(
                list[16][2] - list[20][2] < 30)
            and len4 > 20 and len5 > 20 and len6 > 20):
        if hand_type == 'Right':
            if list[4][1] > list[20][1]:
                return True

        elif hand_type == 'Left':
            if list[4][1] < list[20][1]:
                return True

    return False


def Pp(list, hand_type):
    len = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
    if (len < 60 and list[8][2] < list[12][2] and abs(list[8][1] - list[12][1]) < 60 and abs(
            list[8][2] - list[6][2]) < 40 and
            list[10][2] < list[12][2] and list[14][2] < list[16][2] and list[18][2] < list[20][2] and abs(
                list[9][2] - list[10][2]) > 30):
        if (hand_type == 'Right'):
            if (list[4][1] > list[20][1]):
                return True

        elif (hand_type == 'Left'):
            if (list[4][1] < list[20][1]):
                return True

    return False


def Qq(list, hand_type):
    if (list[4][1] < list[2][1] and list[8][1] < list[5][1]):
        if (hand_type == 'Right'):
            if list[8][1] < list[5][1]:
                if (list[12][1] > list[10][1] and list[16][1] > list[14][1] and list[20][1] > list[18][1] and list[6][
                    1] < list[10][1]):
                    return True

        elif (hand_type == 'Left'):
            if list[8][1] > list[5][1]:
                if (list[12][1] < list[10][1] and list[16][1] < list[14][1] and list[20][1] < list[18][1] and list[6][
                    1] > list[10][1]):
                    return True

    return False


def Rr(list, hand_type):
    if (list[2][1] > list[18][1]):
        if (hand_type == 'Right'):
            if (abs(list[6][2] - list[10][2]) < 30 and abs(list[7][2] - list[11][2]) < 30 and list[8][2] < list[5][
                2] and list[12][2] < list[9][2] and list[12][1] > list[8][1]):
                if (list[4][2] < list[2][2] and list[16][2] > list[14][2] and list[20][2] > list[18][1]):
                    return True

    if (list[2][1] < list[18][1]):
        if (hand_type == 'Left'):
            if (abs(list[6][2] - list[10][2]) < 30 and abs(list[7][2] - list[11][2]) < 30 and list[8][2] < list[5][
                2] and list[12][2] < list[9][2] and list[12][1] < list[8][1]):
                if (list[4][2] < list[2][2] and list[16][2] > list[14][2] and list[20][2] > list[18][1]):
                    return True

    return False


def Ss(list, hand_type):
    len = math.hypot(list[4][1] - list[15][1], list[4][2] - list[15][2])
    if list[9][2] > list[10][2] and len < 30:
        if (hand_type == 'Right'):
            if list[4][1] > list[18][1]:
                if (list[20][2] > list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][
                        2] < list[16][2]):
                        return True

        elif (hand_type == 'Left'):
            if list[4][1] < list[18][1]:
                if (list[20][2] > list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][
                        2] < list[16][2]):
                        return True

    return False


def Uu(list, hand_type):
    len = math.hypot(list[8][1] - list[12][1], list[8][2] - list[12][2])
    if (list[8][2] < list[6][2] and list[12][2] < list[10][2] and abs(list[4][2] - list[14][2]) < 50 and len < 50):
        if (hand_type == 'Right'):
            if (list[2][1] > list[18][1]):
                if (list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True

        elif (hand_type == 'Left'):
            if (list[2][1] < list[18][1]):
                if (list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True
    return False


def Vv(list, hand_type):
    len = math.hypot(list[8][1] - list[12][1], list[8][2] - list[12][2])
    if (list[8][2] < list[6][2] and list[12][2] < list[10][2] and abs(list[4][2] - list[14][2]) < 50 and len > 100):
        if (hand_type == 'Right'):
            if (list[2][1] > list[18][1]):
                if (list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True

        elif (hand_type == 'Left'):
            if (list[2][1] < list[18][1]):
                if (list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True
    return False


def Ww(list, hand_type):
    len1 = math.hypot(list[8][1] - list[12][1], list[8][2] - list[12][2])
    len2 = math.hypot(list[12][1] - list[16][1], list[12][2] - list[16][2])
    if (list[8][2] < list[6][2] and list[12][2] < list[10][2] and abs(
            list[4][2] - list[19][2]) < 30 and len1 > 50 and len2 > 50):
        if (hand_type == 'Right'):
            if (list[5][1] > list[18][1]):
                return True

        elif (hand_type == 'Left'):
            if (list[5][1] < list[18][1]):
                return True

    return False


def Xx(list, hand_type):
    if (list[8][2] > list[6][2] and list[6][2] < list[5][2] and abs(list[4][2] - list[14][2]) < 50 and abs(
            list[8][2] - list[7][2]) < 40):
        if (hand_type == 'Right'):
            if (list[2][1] > list[18][1]):
                if (list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True

        elif (hand_type == 'Left'):
            if (list[2][1] < list[18][1]):
                if (list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True
    return False


def Yy(list, hand_type):
    len = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
    if (list[4][2] < list[2][2] and list[20][2] < list[17][2] and len > 30):
        if (hand_type == 'Right'):
            if (list[4][1] > list[18][1]):
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2]):
                    return True

        elif (hand_type == 'Left'):
            if (list[4][1] < list[18][1]):
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2]):
                    return True

    return False


def which(list):
    if ((list[4][2] < list[3][2] and list[3][2] < list[2][2]) and (list[5][1] < list[6][1] and
                                                                   list[9][1] < list[10][1] and list[13][1] < list[14][
                                                                       1] and list[17][1] < list[18][1]) and
            (list[25][2] < list[24][2] and list[24][2] < list[23][2]) and (list[26][1] > list[27][1] and
                                                                           list[30][1] > list[31][1] and list[34][1] >
                                                                           list[35][1] and list[38][1] > list[39][1])):
        if (list[8][1] < list[6][1] and list[12][1] < list[10][1] and list[16][1] < list[14][1] and list[20][1] <
            list[18][1]) and (
                list[29][1] > list[27][1] and list[33][1] > list[31][1] and list[37][1] > list[35][1] and list[41][1] >
                list[39][1]):
            return True

    return False


def stop(list, hand_type):
    if abs(list[8][2] - list[6][2]) > 50:
        if hand_type == 'Right':
            if list[4][1] > list[5][1]:
                cnt = 0
                for i in range(0, 5):
                    if (list[fingertip[i]][2] < list[fingertip[i] - 2][2]):
                        cnt = cnt + 1
                if cnt == 5:
                    len = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
                    if len > 100:
                        return True

        elif hand_type == 'Left':
            if list[4][1] < list[5][1]:
                cnt = 0
                for i in range(0, 5):
                    if (list[fingertip[i]][2] < list[fingertip[i] - 2][2]):
                        cnt = cnt + 1
                if cnt == 5:
                    len = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
                    if len > 100:
                        return True

    return False


def love_you(list):
    if abs(list[8][2] - list[6][2]) > 50:
        if (list[4][2] < list[2][2] and list[8][2] < list[6][2] and list[20][2] < list[18][2]):
            if (list[12][2] > list[10][2] and list[16][2] > list[14][2]):
                return True

    return False


def okay(list):
    if (list[12][2] < list[9][2] and list[16][2] < list[13][2] and list[20][2] < list[17][2]):
        len = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
        if len < 60:
            return True

    return False


def no(list):
    if (list[16][2] > list[14][2] and list[20][2] > list[18][2] and abs(list[6][2] - list[7][2]) < 20):
        len1 = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
        len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
        len3 = math.hypot(list[5][1] - list[6][1], list[5][2] - list[6][2])
        len4 = math.hypot(list[9][1] - list[10][1], list[9][2] - list[10][2])
        if len1 < 60 and len2 < 60 and len3 < 20 and len4 < 20:
            return True

    return False


def bathroom(list, hand_type):
    if list[4][2] < list[6][2]:
        len1 = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
        len2 = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
        if len1 < 50 and len2 < 50:
            if hand_type == 'Right':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][
                    2] >
                        list[18][2]):
                    if (list[4][1] < list[6][1]):
                        return True

            elif hand_type == 'Left':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][
                    2] >
                        list[18][2]):
                    if (list[4][1] > list[6][1]):
                        return True
    return False


def yes(list):
    if (list[2][2] > list[5][2] and list[5][2] < list[6][2] and list[9][2] < list[10][2] and list[13][2] < list[14][2]
            and list[17][2] < list[18][2] and list[8][2] < list[12][2] and list[12][2] < list[10][2]):
        #if(abs(list[2][2] - list[4][2]) < 30):
        len1 = math.hypot(list[10][1] - list[0][1], list[10][2] - list[0][2])
        len2 = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
        if len1 < 100 and len2 < 60:
            return True
    return False


def house(list):
    len1 = math.hypot(list[4][1] - list[25][1], list[4][2] - list[25][2])
    len2 = math.hypot(list[8][1] - list[29][1], list[8][2] - list[29][2])
    len3 = math.hypot(list[12][1] - list[33][1], list[12][2] - list[33][2])
    len4 = math.hypot(list[16][1] - list[37][1], list[16][2] - list[37][2])
    len5 = math.hypot(list[20][1] - list[41][1], list[20][2] - list[41][2])
    len6 = math.hypot(list[0][1] - list[21][1], list[0][2] - list[21][2])

    if len1 > 30 and len2 < 20 and len3 < 20 and len4 < 20 and len5 < 50 and len6 > 50:
        return True

    return False


def angry(list):
    if (list[3][1] < list[19][1] and list[24][1] > list[40][1]):
        len1 = math.hypot(list[8][1] - list[6][1], list[8][2] - list[6][2])
        len2 = math.hypot(list[12][1] - list[10][1], list[12][2] - list[10][2])
        len3 = math.hypot(list[16][1] - list[14][1], list[16][2] - list[14][2])
        len4 = math.hypot(list[20][1] - list[18][1], list[20][2] - list[18][2])
        len5 = math.hypot(list[29][1] - list[27][1], list[29][2] - list[27][2])
        len6 = math.hypot(list[33][1] - list[31][1], list[33][2] - list[31][2])
        len7 = math.hypot(list[37][1] - list[35][1], list[37][2] - list[35][2])
        len8 = math.hypot(list[41][1] - list[39][1], list[41][2] - list[39][2])
        len9 = math.hypot(list[4][1] - list[5][1], list[4][2] - list[5][2])
        len10 = math.hypot(list[25][1] - list[26][1], list[25][2] - list[26][2])
        if len1 < 40 and len2 < 40 and len3 < 40 and len4 < 40 and len5 < 40 and len6 < 40 and len7 < 40 and len8 < 40 and len9 < 60 and len10 < 60:
            return True
    return False


def cry(list):
    if (list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] > list[18][2] and list[33][2] >
            list[31][2] and list[37][2] > list[35][2] and list[41][2] > list[39][2]):
        if (list[3][1] < list[19][1] and list[24][1] > list[40][1]):
            len1 = math.hypot(list[8][1] - list[47][1], list[8][2] - list[47][2])
            len2 = math.hypot(list[29][1] - list[44][1], list[29][2] - list[44][2])
            len3 = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
            len4 = math.hypot(list[25][1] - list[31][1], list[25][2] - list[31][2])
            if len1 < 30 and len2 < 30 and len3 < 40 and len4 < 40:
                return True
    return False


def process_frame(image):
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    with mp_holistic.Holistic(static_image_mode=True) as holistic:
        results = holistic.process(image_rgb)

        if results.right_hand_landmarks or results.left_hand_landmarks:
            landmarks = []
            hand_type = 'Right' if results.right_hand_landmarks else 'Left'

            # Process right hand landmarks if present
            if results.right_hand_landmarks:
                for id, lm in enumerate(results.right_hand_landmarks.landmark):
                    landmarks.append([id, lm.x * image.shape[1], lm.y * image.shape[0]])

            # Process left hand landmarks if present
            if results.left_hand_landmarks:
                for id, lm in enumerate(results.left_hand_landmarks.landmark):
                    landmarks.append([id, lm.x * image.shape[1], lm.y * image.shape[0]])

            # Process pose landmarks if present
            if results.pose_landmarks:
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    landmarks.append([id + 42, lm.x * image.shape[1], lm.y * image.shape[0]])

            # Check for gestures
            if which(landmarks):
                return "Which?"
            elif house(landmarks):
                return "House"
            elif angry(landmarks):
                return "Angry"
            elif cry(landmarks):
                return "Cry"
            elif love_you(landmarks):
                return "I love you"
            elif no(landmarks):
                return "No"
            elif yes(landmarks):
                return "Yes"
            elif Cc(landmarks):
                return "Cc"
            elif Dd(landmarks):
                return "Dd"
            elif Ff(landmarks):
                return "Ff"
            elif hand_type == 'Right':
                if bathroom(landmarks, 'Right'):
                    return "Bathroom"
                elif stop(landmarks, 'Right'):
                    return "Stop"
                elif Aa(landmarks, 'Right'):
                    return "Aa"
                elif Bb(landmarks, 'Right'):
                    return "Bb"
                elif Ee(landmarks, 'Right'):
                    return "Ee"
                elif Gg(landmarks, 'Right'):
                    return "Gg"
                elif Hh(landmarks, 'Right'):
                    return "Hh"
                elif Ii(landmarks, 'Right'):
                    return "Ii"
                elif Jj(landmarks, 'Right'):
                    return "Jj"
                elif Kk(landmarks, 'Right'):
                    return "Kk"
                elif Ll(landmarks, 'Right'):
                    return "Ll"
                elif Mm(landmarks, 'Right'):
                    return "Mm"
                elif Nn(landmarks, 'Right'):
                    return "Nn"
                elif Oo(landmarks, 'Right'):
                    return "Oo"
                elif Pp(landmarks, 'Right'):
                    return "Pp"
                elif Qq(landmarks, 'Right'):
                    return "Qq"
                elif Rr(landmarks, 'Right'):
                    return "Rr"
                elif Ss(landmarks, 'Right'):
                    return "Ss"
                elif Uu(landmarks, 'Right'):
                    return "Uu"
                elif Vv(landmarks, 'Right'):
                    return "Vv"
                elif Ww(landmarks, 'Right'):
                    return "Ww"
                elif Xx(landmarks, 'Right'):
                    return "Xx"
                elif Yy(landmarks, 'Right'):
                    return "Yy"
            elif hand_type == 'Left':
                if bathroom(landmarks, 'Left'):
                    return "Bathroom"
                elif stop(landmarks, 'Left'):
                    return "Stop"
                elif Aa(landmarks, 'Left'):
                    return "Aa"
                elif Bb(landmarks, 'Left'):
                    return "Bb"
                elif Ee(landmarks, 'Left'):
                    return "Ee"
                elif Gg(landmarks, 'Left'):
                    return "Gg"
                elif Hh(landmarks, 'Left'):
                    return "Hh"
                elif Ii(landmarks, 'Left'):
                    return "Ii"
                elif Jj(landmarks, 'Left'):
                    return "Jj"
                elif Kk(landmarks, 'Left'):
                    return "Kk"
                elif Ll(landmarks, 'Left'):
                    return "Ll"
                elif Mm(landmarks, 'Left'):
                    return "Mm"
                elif Nn(landmarks, 'Left'):
                    return "Nn"
                elif Oo(landmarks, 'Left'):
                    return "Oo"
                elif Pp(landmarks, 'Left'):
                    return "Pp"
                elif Qq(landmarks, 'Left'):
                    return "Qq"
                elif Rr(landmarks, 'Left'):
                    return "Rr"
                elif Ss(landmarks, 'Left'):
                    return "Ss"
                elif Uu(landmarks, 'Left'):
                    return "Uu"
                elif Vv(landmarks, 'Left'):
                    return "Vv"
                elif Ww(landmarks, 'Left'):
                    return "Ww"
                elif Xx(landmarks, 'Left'):
                    return "Xx"
                elif Yy(landmarks, 'Left'):
                    return "Yy"

    return "Can't recognize gesture"