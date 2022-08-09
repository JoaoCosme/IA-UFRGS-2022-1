from math import log, sqrt


def ucb(vitoria_suc,jogadas_suc,jogadas_no):
    return vitoria_suc/jogadas_suc + 2*1 * sqrt(2*log(jogadas_no)/jogadas_suc)


while True:
    enter = input("Enter:").split(",")
    enter = [ int(x1) for x1 in enter]
    print(ucb(enter[0],enter[1],enter[2]))