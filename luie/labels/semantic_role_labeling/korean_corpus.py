# KLUE
"""
labels = [
    "PREDICATE",
    "ARG0",  # 서술어의 동작주, 행위자(Agent), 경험주(Experiencer)
    "ARG1",  # 서술어의 피동작주(Patient), 대상(Theme) 등
    "ARG2",  # 시작점(Starting Point), 수혜자(Benefactive) 등
    "ARG3",  # 도착점(Ending Point) 등
    "ARGA",  # 장형 사동 구문(-게 하다)의 사동주
    "ARGM-LOC",  # 장소
    "ARGM-DIR",  # 방향
    "ARGM-CND",  # 조건
    "ARGM-MNR",  # 방법
    "ARGM-INS",  # 도구
    "ARGM-TMP",  # 시간
    "ARGM-CAU",  # 이유/원인
    "ARGM-EXT",  # 범위
    "ARGM-PRD",  # 보조 서술
    "ARGM-PRP",  # 목적
    "ARGM-DIS",  # 담화 연결
    "ARGM-ADV",  # 부사적 어구
    "ARGM-NEG",  # 부정
    "ARGM-AUX",  # 보조 용언
]
"""
from typing import Dict


class SrlKoreanCorpusLabels:
    SIZE: int = 81
    PAD = "[PAD]"
    LABEL2IDX: Dict[str, int] = {
        PAD: 0,
        "B-PREDICATE": 1,
        "I-PREDICATE": 2,
        "E-PREDICATE": 3,
        "S-PREDICATE": 4,
        "B-ARG0": 5,
        "I-ARG0": 6,
        "E-ARG0": 7,
        "S-ARG0": 8,
        "B-ARG1": 9,
        "I-ARG1": 10,
        "E-ARG1": 11,
        "S-ARG1": 12,
        "B-ARG2": 13,
        "I-ARG2": 14,
        "E-ARG2": 15,
        "S-ARG2": 16,
        "B-ARG3": 17,
        "I-ARG3": 18,
        "E-ARG3": 19,
        "S-ARG3": 20,
        "B-ARGA": 21,
        "I-ARGA": 22,
        "E-ARGA": 23,
        "S-ARGA": 24,
        "B-ARGM-LOC": 25,
        "I-ARGM-LOC": 26,
        "E-ARGM-LOC": 27,
        "S-ARGM-LOC": 28,
        "B-ARGM-DIR": 29,
        "I-ARGM-DIR": 30,
        "E-ARGM-DIR": 31,
        "S-ARGM-DIR": 32,
        "B-ARGM-CND": 33,
        "I-ARGM-CND": 34,
        "E-ARGM-CND": 35,
        "S-ARGM-CND": 36,
        "B-ARGM-MNR": 37,
        "I-ARGM-MNR": 38,
        "E-ARGM-MNR": 39,
        "S-ARGM-MNR": 40,
        "B-ARGM-INS": 41,
        "I-ARGM-INS": 42,
        "E-ARGM-INS": 43,
        "S-ARGM-INS": 44,
        "B-ARGM-TMP": 45,
        "I-ARGM-TMP": 46,
        "E-ARGM-TMP": 47,
        "S-ARGM-TMP": 48,
        "B-ARGM-CAU": 49,
        "I-ARGM-CAU": 50,
        "E-ARGM-CAU": 51,
        "S-ARGM-CAU": 52,
        "B-ARGM-EXT": 53,
        "I-ARGM-EXT": 54,
        "E-ARGM-EXT": 55,
        "S-ARGM-EXT": 56,
        "B-ARGM-PRD": 57,
        "I-ARGM-PRD": 58,
        "E-ARGM-PRD": 59,
        "S-ARGM-PRD": 60,
        "B-ARGM-PRP": 61,
        "I-ARGM-PRP": 62,
        "E-ARGM-PRP": 63,
        "S-ARGM-PRP": 64,
        "B-ARGM-DIS": 65,
        "I-ARGM-DIS": 66,
        "E-ARGM-DIS": 67,
        "S-ARGM-DIS": 68,
        "B-ARGM-ADV": 69,
        "I-ARGM-ADV": 70,
        "E-ARGM-ADV": 71,
        "S-ARGM-ADV": 72,
        "B-ARGM-NEG": 73,
        "I-ARGM-NEG": 74,
        "E-ARGM-NEG": 75,
        "S-ARGM-NEG": 76,
        "B-ARGM-AUX": 77,
        "I-ARGM-AUX": 78,
        "E-ARGM-AUX": 79,
        "S-ARGM-AUX": 80,
    }
    IDX2LABEL: Dict[str, str] = {
        "0": PAD,
        "1": "B-PREDICATE",
        "2": "I-PREDICATE",
        "3": "E-PREDICATE",
        "4": "S-PREDICATE",
        "5": "B-ARG0",
        "6": "I-ARG0",
        "7": "E-ARG0",
        "8": "S-ARG0",
        "9": "B-ARG1",
        "10": "I-ARG1",
        "11": "E-ARG1",
        "12": "S-ARG1",
        "13": "B-ARG2",
        "14": "I-ARG2",
        "15": "E-ARG2",
        "16": "S-ARG2",
        "17": "B-ARG3",
        "18": "I-ARG3",
        "19": "E-ARG3",
        "20": "S-ARG3",
        "21": "B-ARGA",
        "22": "I-ARGA",
        "23": "E-ARGA",
        "24": "S-ARGA",
        "25": "B-ARGM-LOC",
        "26": "I-ARGM-LOC",
        "27": "E-ARGM-LOC",
        "28": "S-ARGM-LOC",
        "29": "B-ARGM-DIR",
        "30": "I-ARGM-DIR",
        "31": "E-ARGM-DIR",
        "32": "S-ARGM-DIR",
        "33": "B-ARGM-CND",
        "34": "I-ARGM-CND",
        "35": "E-ARGM-CND",
        "36": "S-ARGM-CND",
        "37": "B-ARGM-MNR",
        "38": "I-ARGM-MNR",
        "39": "E-ARGM-MNR",
        "40": "S-ARGM-MNR",
        "41": "B-ARGM-INS",
        "42": "I-ARGM-INS",
        "43": "E-ARGM-INS",
        "44": "S-ARGM-INS",
        "45": "B-ARGM-TMP",
        "46": "I-ARGM-TMP",
        "47": "E-ARGM-TMP",
        "48": "S-ARGM-TMP",
        "49": "B-ARGM-CAU",
        "50": "I-ARGM-CAU",
        "51": "E-ARGM-CAU",
        "52": "S-ARGM-CAU",
        "53": "B-ARGM-EXT",
        "54": "I-ARGM-EXT",
        "55": "E-ARGM-EXT",
        "56": "S-ARGM-EXT",
        "57": "B-ARGM-PRD",
        "58": "I-ARGM-PRD",
        "59": "E-ARGM-PRD",
        "60": "S-ARGM-PRD",
        "61": "B-ARGM-PRP",
        "62": "I-ARGM-PRP",
        "63": "E-ARGM-PRP",
        "64": "S-ARGM-PRP",
        "65": "B-ARGM-DIS",
        "66": "I-ARGM-DIS",
        "67": "E-ARGM-DIS",
        "68": "S-ARGM-DIS",
        "69": "B-ARGM-ADV",
        "70": "I-ARGM-ADV",
        "71": "E-ARGM-ADV",
        "72": "S-ARGM-ADV",
        "73": "B-ARGM-NEG",
        "74": "I-ARGM-NEG",
        "75": "E-ARGM-NEG",
        "76": "S-ARGM-NEG",
        "77": "B-ARGM-AUX",
        "78": "I-ARGM-AUX",
        "79": "E-ARGM-AUX",
        "80": "S-ARGM-AUX",
    }
