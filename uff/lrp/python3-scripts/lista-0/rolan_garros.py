# Roland Garros

# No torneio de Roland Garros, um dos mais tradicionais torneios de tênis do mundo, realizado em
# Paris, participam 128 tenistas. Em cada partida, participam dois jogadores, sendo que o vencedor
# passa para a próxima fase, e o perdedor é eliminado do torneio. A cada rodada, os tenistas que
# ainda continuam no torneio participam de exatamente uma partida.

# Total de jogagores no torneio.
n = 128
# Contador de partidas realizadas.
p = 0
# Contadore de partidas.
r = 0
# Enquanto o total de jogadores no torneio for maior que 1, ou seja o vencedor.
while n > 1:
    # Soma-se 1 rodada a cada iteração.
    r = r + 1
    # Para cada rodada temos n/2 de partidas sendo realizadas.
    n = n // 2
    # Somamos o total de partidas realizadas na rodada ao contador p.
    p = p + n

print(f"""  No torneio de Roland Garros, um dos mais tradicionais torneios de tênis do mundo, realizado em
 Paris, participam 128 tenistas. Em cada partida, participam dois jogadores, sendo que o vencedor
 passa para a próxima fase, e o perdedor é eliminado do torneio. A cada rodada, os tenistas que
 ainda continuam no torneio participam de exatamente uma partida. Sendo assim, são realizadas no total
 {p} partidas em {r} rodadas, durante todo o evento.
""")

# 3. Qual o número total de partidas deste torneio?
# (A) 64 F
# (B) 65 F
# (C) 127 V
# (D) 128 F
# (E) nenhuma das acima F

# 4. Quantas rodadas existem, no total, durante o torneio?
# (A) 8 F
# (B) 9 F
# (C) 10 F
# (D) 16 F
# (E) nenhuma das acima. V temos 7 partidas no total.