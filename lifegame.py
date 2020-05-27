import random

nome = input("Digite o nome do seu personagem: ")
reputação = 0
felicidade = 0
saúde = 10
destreza = 0
cultura = 0
animaldeestimação = ["Gato", "Cachorro", "Papaguaio", "Cobra", "Peixe"]
doenças = ["Pneumonia", "Cancêr"]
sim = ["Sim", "sim", "S", "Simm"]
não = ["nao", "não", "n", "Não", "Nao"]
anosdevida = random.randint(10, 99)
nascimento = 2020 - anosdevida
print(nome, "você morreu com", anosdevida, "anos de vida")
print("Agora vamos ver como foi a sua vida?")

print()
print(nome, "é o ano de", nascimento, "e você nasceu!")
print("No mesmo ano em que:")

if nascimento == 1922:
    print("Mussolini chega ao poder na Itália")
    print("Realização da Semana de Arte Moderna em São Paulo")
if nascimento == 1923:
    print(
        "Putsch da Cervejaria ou Putsch de Munique, uma tentativa falhada de golpe de Adolf Hitler e do Partido Nazista contra o governo da região alemã da Bavaria.")
if nascimento == 1924:
    print("Morreria Vladimir Lenin, revolucionário e Chefe de Estado Russo de 1917 a 1924")
if nascimento == 1925:
    print("Nasceria B. B. King, guitarrista de blues, compositor e cantor estadunidense")
if nascimento == 1926:
    print(" Nasceria Fidel Castro, primeiro-ministro e posteriormente presidente de Cuba")
if nascimento == 1927:
    print("O bando de Lampião invade a cidade de Mossoró, no Rio Grande do Norte, e é derrotado")
if nascimento == 1928:
    print("Lançamento do curta-metragem Plane Crazy de Walt Disney, onde Mickey e Minnie fazem sua primeira aparição.")
if nascimento == 1929:
    print(
        "Ano em que se iniciou uma grande depressão econômica mundial, cujo início é marcado pela quebra da Bolsa de Valores de Nova York")
if nascimento == 1930:
    print(" Nasceria Neil Armstrong, astronauta dos Estados Unidos e primeiro homem a pisar na Lua.")
if nascimento == 1931:
    print("Nasceria Fernando Henrique Cardoso, futuro presidente do Brasil")
if nascimento == 1932:
    print("Ocorreram na Alemanha as últimas eleições em todo o território alemão até o ano de 1990")
if nascimento == 1933:
    print(
        "Adolf Hitler foi nomeado chanceler da Alemanha ( Reichskanzler) por Hindenburg (a Machtergreifung), sendo o gabinete ministerial em seguida dissolvido por Hitler.")
if nascimento == 1934:
    print("Alemanha nazista aprova a Lei para a Prevenção de Descendentes Geneticamente Doentes")
if nascimento == 1935:
    print("Lido na Câmara Federal o Primeiro Manifesto da Aliança Nacional Libertadora.")
if nascimento == 1936:
    print(
        " Luís Carlos Prestes e sua esposa Olga Benário são presos. Ele ficará 9 anos na prisão, e Olga, sendo alemã, será deportada.")
if nascimento == 1937:
    print(
        "Getúlio Vargas desfere um golpe de estado fundando o Estado Novo. É cancelada a Eleição direta presidencial que ocorreria em 1938 e é outorgada uma nova Constituição para o Brasil.")
if nascimento == 1938:
    print(
        "O cangaceiro Lampião foi morto e degolado na fazenda de Angicos, no sertão do estado de Sergipe com sua companheira Maria Bonita e mais nove companheiros de crime.")
if nascimento == 1939:
    print("Se da o início da Segunda Guerra Mundial.")
if nascimento == 1940:
    print()
if nascimento == 1941:
    print()
if nascimento == 1942:
    print()
if nascimento == 1943:
    print()
if nascimento == 1944:
    print()
if nascimento == 1945:
    print()
if nascimento == 1946:
    print()
if nascimento == 1947:
    print()
if nascimento == 1948:
    print()
if nascimento == 1949:
    print()
if nascimento == 1950:
    print()
if nascimento == 1951:
    print()
if nascimento == 1952:
    print()
if nascimento == 1953:
    print()
if nascimento == 1954:
    print()
if nascimento == 1955:
    print()
if nascimento == 1956:
    print()
if nascimento == 1957:
    print()
if nascimento == 1958:
    print()
if nascimento == 1959:
    print()
if nascimento == 1960:
    print()
if nascimento == 1961:
    print()
if nascimento == 1962:
    print()
if nascimento == 1963:
    print()
if nascimento == 1964:
    print()
if nascimento == 1965:
    print()
if nascimento == 1966:
    print()
if nascimento == 1967:
    print()
if nascimento == 1968:
    print()
if nascimento == 1969:
    print()
if nascimento == 1970:
    print()
if nascimento == 1971:
    print()
if nascimento == 1972:
    print()
if nascimento == 1973:
    print()
if nascimento == 1974:
    print()
if nascimento == 1975:
    print()
if nascimento == 1976:
    print()
if nascimento == 1977:
    print()
if nascimento == 1978:
    print()
if nascimento == 1979:
    print()
if nascimento == 1980:
    print()
if nascimento == 1981:
    print()
if nascimento == 1982:
    print()
if nascimento == 1983:
    print()
if nascimento == 1984:
    print()
if nascimento == 1985:
    print()
if nascimento == 1986:
    print()
if nascimento == 1987:
    print()
if nascimento == 1988:
    print()
if nascimento == 1989:
    print()
if nascimento == 1990:
    print()
if nascimento == 1991:
    print()
if nascimento == 1992:
    print()
if nascimento == 1993:
    print()
if nascimento == 1994:
    print()
if nascimento == 1995:
    print()
if nascimento == 1996:
    print()
if nascimento == 1997:
    print()
if nascimento == 1998:
    print()
if nascimento == 1999:
    print()
if nascimento == 2000:
    print()
if nascimento == 2001:
    print()
if nascimento == 2002:
    print()
if nascimento == 2003:
    print()
if nascimento == 2004:
    print()
if nascimento == 2005:
    print()
if nascimento == 2006:
    print()
if nascimento == 2007:
    print()
if nascimento == 2008:
    print()
if nascimento == 2009:
    print()
if nascimento == 2010:
    print()


def jogadado(x):
    d = random.randint(1, x)
    return d


if anosdevida >= 5:
    print("Parabéns você chegou aos 5 anos de idade")
    print("Não há muito o que fazer....")
if anosdevida >= 10:
    print("Você chegou aos 10 anos de idade!")
    anoshoje = nascimento + 10
    print("O ano é: ", anoshoje)
    print("Você está na escola, e tem 2 canetas, um colega te pediu uma emprestada")
    print(" mas a maioria das pessoas da escola não gosta dele, dizem que ele rouba coisas")
    resp = input("Você vai emprestar? Sim ou Não: ")
    print()
    if resp in sim:
        print("Vamos jogar nosso primeiro dado de conseqência")
        print("....")
        print("Será um dado de 10 faces")
        d10 = jogadado(10)
        print("Você tirou: ", d10)
        if d10 > 4:
            print("Você emprestou a caneta, ele devolveu, e mostou pra turma que os boatos não eram verdade")
            print("Sua reputação aumentou em 1")
            reputação = reputação + 1
        if d10 <= 4:
            print("Você emprestou a caneta, ele não devolveu e disse que você roubou as canetas")
            print("Sua reputação caiu em 1")
            reputação = reputação - 1
    if resp in não:
        print("Vamos jogar nosso primeiro dado de conseqência")
        print("....")
        print("Será um dado de 10 faces")
        d10 = random.randint(1, 10)
        print("Você tirou: ", d10)
        if d10 >= 7:
            print("Você entrou para o grupo dos mais populares")
            print("Sua reputação aumentou em 1")
            reputação = reputação + 1
        if d10 < 7:
            print("Ele inventou para a turma que você espalhou os boatos sobre ele, eles acreditaram")
            print("Sua reputação caiu em 1")
            reputação = reputação - 1

if anosdevida >= 11:
    print("Você chegou aos 11 anos de idade!")
    anoshoje = nascimento + 11
    print("O ano é: ", anoshoje)
    if anoshoje > 1920 and anoshoje < 1960:
        print("Você está em casa e é o primeiro dia de férias")
        print("as crianças da rua te chamaram para jogar peteka")
        resp = input("Você vai? Sim ou Não: ")
        print()
        if resp in sim:
            print("Vamos jogar o dado de conseqência")
            print("....")
            print("Será um dado de 10 faces")
            d10 = random.randint(1, 10)
            print("Você tirou: ", d10)
            if d10 > 6:
                print("Você se divertiu, se mostrou um bom jogador e fez novos amigos")
                print("Sua reputação aumentou em 1")
                print("Sua destreza aumentou em 1")
                destreza = destreza + 1
                reputação = reputação + 1
            if d10 > 2 and d10 <= 6:
                print("Você ficou mais de próximo do que jogou, mas fez novos amigos")
                print("Sua reputação aumentou em 1")
                reputação = reputação + 1
            if d10 <= 2:
                print("Você quebrou o braço jogando peteka, e perdeu as férias com os amigos")
                print("Sua reputação caiu em 1")
                print("Sua Saúde caiu em 1")
                reputação = reputação - 1

                saúde = saúde - 1
        if resp in não:
            print("Vamos jogar nosso dado de conseqência")
            print("....")
            print("Será um dado de 10 faces")
            d10 = random.randint(1, 10)
            print("Você tirou: ", d10)
            if d10 >= 5:
                print("Você ficou em casa e bricou com pião")
                print("Sua destreza aumentou em 1")  # é preciso ver o que acontece de acordo com a época vivida
                destreza = destreza + 1
            if d10 < 5:
                print("Você ficou em casa")
                print("Nada especial aconteceu")
    if anoshoje > 1960 and anoshoje < 2020:
        print("Você está em casa e é o primeiro dia de férias")
        print("as crianças da rua te chamaram para jogar bola")
        resp = input("Você vai? Sim ou Não: ")
        print()
        if resp in sim:
            print("Vamos jogar o dado de conseqência")
            print("....")
            print("Será um dado de 10 faces")
            d10 = random.randint(1, 10)
            print("Você tirou: ", d10)
            if d10 > 6:
                print("Você se divertiu, se mostrou um bom jogador e fez novos amigos")
                print("Sua reputação aumentou em 1")
                print("Sua destreza aumentou em 1")
                destreza = destreza + 1
                reputação = reputação + 1
            if d10 > 2 and d10 <= 6:
                print("Você ficou mais de próximo do que jogou, mas fez novos amigos")
                print("Sua reputação aumentou em 1")
                reputação = reputação + 1
            if d10 <= 2:
                print("Você quebrou a perna jogando bola, e perdeu as férias com os amigos")
                print("Sua reputação caiu em 1")
                print("Sua Saúde caiu em 1")
                reputação = reputação - 1
                saúde = saúde - 1
        if resp in não:
            if anoshoje > 1960 and anoshoje < 1980:
                print("Vamos jogar nosso dado de conseqência")
                print("....")
                print("Será um dado de 10 faces")
                d10 = random.randint(1, 10)
                print("Você tirou: ", d10)
                if d10 >= 3:
                    print("Você ficou em casa e jogou bola de gude")
                    print("Sua destreza aumentou em 1")  # é preciso ver o que acontece de acordo com a época vivida
                    destreza = destreza + 1
                if d10 < 3:
                    print("Você ficou em casa")
                    print("Nada especial aconteceu")
            if anoshoje > 1980 and anoshoje < 1990:
                print("Vamos jogar nosso dado de conseqência")
                print("....")
                print("Será um dado de 10 faces")
                d10 = random.randint(1, 10)
                print("Você tirou: ", d10)
                if d10 >= 3:
                    print("Você ficou em casa e descobriu uma música nova na vitrola dos seus pais")
                    print("Sua cultura aumentou em 1")  # é preciso ver o que acontece de acordo com a época vivida
                    cultura = cultura + 1
                if d10 < 3:
                    print("Você ficou em casa")
                    print("Nada especial aconteceu")
            if anoshoje > 1990 and anoshoje < 2000:
                print("Vamos jogar nosso dado de conseqência")
                print("....")
                print("Será um dado de 10 faces")
                d10 = random.randint(1, 10)
                print("Você tirou: ", d10)
                if d10 >= 3:
                    print("Você ficou em casa e descobriu um clipe novo na MTV dos seus pais")
                    print("Pearl Jam!!!!")
                    print("Sua cultura aumentou em 1")  # é preciso ver o que acontece de acordo com a época vivida
                    cultura = cultura + 1
                if d10 < 3:
                    print("Você ficou em casa")
                    print("Nada especial aconteceu")
            if anoshoje > 2000 and anoshoje < 2020:
                print("Vamos jogar nosso dado de conseqência")
                print("....")
                print("Será um dado de 10 faces")
                d10 = random.randint(1, 10)
                print("Você tirou: ", d10)
                if d10 >= 3:
                    print("Você ficou em casa e descobriu um jogo novo no computador")
                    print("World of Warcraft!!!")
                    print("Sua cultura aumentou em 1")  # é preciso ver o que acontece de acordo com a época vivida
                    cultura = cultura + 1
                if d10 < 3:
                    print("Você ficou em casa")
                    print("Nada especial aconteceu")
if anosdevida >= 12:
    print("12 anos!")
    anoshoje = nascimento + 12
    print("O ano é: ", anoshoje)
    bicho = random.choice(animaldeestimação)
    print("parabéns vocë ganhou um", bicho)
    nomebicho = input("Qual será o nome dele? ")

if anosdevida >= 14:
    print("Você chegou aos 14 anos!")
    anoshoje = nascimento + 14
    print("O ano é: ", anoshoje)
    print("Você encontrou com o Gollum, e ele te fez a seguinte charada para continuar")
    print("Tem raízes misteriosas,"
          "É mais alta que as frondosa Sobe, sobe"
          "e também desce, Mas não cresce nem decresce.")
    resposta = input("Digite aqui a sua resposta: ")
    if resposta == "Montanha" or "montanha":
        print("Você Avançou")
    else:
        print("Voce perdeu, e eu testei o git")


