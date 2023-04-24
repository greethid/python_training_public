import time
import winsound

def odliczanie_czasu(czas):
    for i in range(czas, 0, -1):
        print(i)
        time.sleep(1)
    print("Czas minął!")
    frequency = 2500  # częstotliwość sygnału dźwiękowego w Hz
    duration = 1000  # czas trwania sygnału dźwiękowego w ms
    winsound.Beep(frequency, duration)

czas = int(input("Podaj czas w sekundach: "))
odliczanie_czasu(czas)