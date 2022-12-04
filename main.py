players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
average= sum(players)/10
#print("a media e "+average)
altos= [jogador  for jogador in players  if jogador>average]
print("os jogadores considerados altos pro basket sao:")
print(altos)
baixos=[jogador for jogador in players if jogador <180]
print("os jogadores considerados baixos pro basket sao:")
print(baixos)
print("o jogador mais baixo e:")
print(min(players))