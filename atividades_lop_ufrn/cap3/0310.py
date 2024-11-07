altura_cone, raio_cone, altura_para, largura_para, comprimento_para = map(float, input().split())

volume_cone = (1/3) * 3.1415926 * (raio_cone ** 2) * altura_cone
volume_para= altura_para * largura_para * comprimento_para

massa_cone = volume_cone * 8
massa_para = volume_para * 0.5

if abs(massa_cone - massa_para) < 5:
    print(f"O paralepípedo e o cone possuem o mesmo peso.")
elif massa_cone > massa_para:
    print(f"O cone é mais pesado com {massa_cone:.2f}g.")
elif massa_para > massa_cone:
    print(f"O paralelepípedo é mais pesado com {massa_para:.2f}g.")