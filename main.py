class MataMata:
    def __init__(self, selecoes, partidas):
        self.selecoes = selecoes
        self.partidas = partidas
        self.dic = {}

    # Leitura da lista de seleções e montagem do dicionario
    def coletar_selecoes(self):

        self.dic = {self.selecoes[i].replace("\n", ""): {
            'partidas_disputadas': 0,
            'partidas_tempo_normal': 0,
            'partidas_penaltis': 0,
            'vitorias': 0,
            'derrotas': 0,
            'gols_marcados': 0,
            'gols_sofridos': 0
        } for i in range(len(self.selecoes))}

    # Leitura da lista de partidas
    def coletar_partidas(self):
        for i in range(len(self.partidas)):
            self.partidas[i] = self.partidas[i].split(" ")

            # Remover o \n do ultimo pais de cada array
            self.partidas[i][len(self.partidas[i]) - 1] = self.partidas[i][len(self.partidas[i]) - 1].replace("\n", "")
            # print(f'AQUII {self.partidas[i][len(self.partidas[i])-1]}')

        self.leitura_das_partidas()

    def leitura_das_partidas(self):
        local_do_x = 0
        contador = 0
        # print(f'HEREE {self.partidas[0]}')

        # Iteracao para cada partida
        for i in range(len(self.partidas)):
            if len(self.partidas[i]) == 5:
                time1 = self.partidas[i][0]
                time2 = self.partidas[i][4]
                gol_time_1 = self.partidas[i][1]
                gol_time_2 = self.partidas[i][3]
                self.atribuicao_resultados(time1, time2, gol_time_1, gol_time_2, 0, 0, 0)

            else:  # Com penalti Brasil 0 x 0 (2 x 5) Tunisia
                time1_penalti = self.partidas[i][0]
                time2_penalti = self.partidas[i][-1]
                golTime1 = self.partidas[i][1]
                golTime2 = self.partidas[i][3]
                penatilTime1 = self.partidas[i][4].replace("(", "")
                penatilTime2 = self.partidas[i][6].replace(")", "")
                self.atribuicao_resultados(time1_penalti, time2_penalti, golTime1, golTime2, 1, penatilTime1,
                                           penatilTime2)

    def atribuicao_resultados(self, time1, time2, golTime1, golTime2, penalti, penaltis_time1, penaltis_time2):
        self.dic[time1]['partidas_disputadas'] += 1
        self.dic[time2]['partidas_disputadas'] += 1
        self.dic[time1]["gols_marcados"] += int(golTime1)
        self.dic[time2]["gols_marcados"] += int(golTime2)
        self.dic[time1]["gols_sofridos"] += int(golTime2)
        self.dic[time2]["gols_sofridos"] += int(golTime1)
        if penalti == 0:
            self.dic[time1]['partidas_tempo_normal'] += 1
            self.dic[time2]['partidas_tempo_normal'] += 1
            if golTime1 > golTime2:
                self.dic[time1]['vitorias'] += 1
                self.dic[time2]['derrotas'] += 1
            else:
                self.dic[time2]['vitorias'] += 1
                self.dic[time1]['derrotas'] += 1
        elif penalti == 1:
            self.dic[time1]['partidas_penaltis'] += 1
            self.dic[time2]['partidas_penaltis'] += 1
            if penaltis_time1 > penaltis_time2:
                self.dic[time1]['vitorias'] += 1
                self.dic[time2]['derrotas'] += 1
            else:
                self.dic[time2]['vitorias'] += 1
                self.dic[time1]['derrotas'] += 1

    def confereGanhador(self):
        for i in self.dic:
            if self.dic[i]['vitorias'] == 4:
                print("---------------------------------------------------")
                print("Ganhador:", i)

    def printaTudo(self):
        for i in self.dic:
            print("---------------------------------------------------")
            print("Pais: {}\nPartidas decididas em tempo normal: {}\n"
                  "Partidas decidadas nos penaltis: {}\nVitorias: {}\nDerrotas: {}\n"
                  "Gols Marcados: {}\nGols Sofridos: {}"
                  .format(i, self.dic[i]["partidas_tempo_normal"], self.dic[i]["partidas_penaltis"],
                          self.dic[i]["vitorias"], self.dic[i]["derrotas"], self.dic[i]["gols_marcados"],
                          self.dic[i]["gols_sofridos"]))
        self.confereGanhador()
        # if valor_time_1 > valor_time_2:
        #     self.dic[time1][]


def main():
    print("Mata Mata")

    # Leitura dos arquivos que contem os dados de entrada
    with open('partidas') as arquivo_partidas:
        partidas = arquivo_partidas.readlines()

    with open('paises') as arquivo_paises:
        selecoes = arquivo_paises.readlines()

    mata_mata = MataMata(selecoes, partidas)
    mata_mata.coletar_selecoes()
    mata_mata.coletar_partidas()
    mata_mata.printaTudo()


if __name__ == '__main__':
    main()

# selecoes = []
# partidas = []
# dic = {}
# caracteres = ["(", ")"]
# campeao = ""
# # Leitura da lista de seleções
# for i in range(16):
#
# # Leitura das partidas
# # Processamento dos dados
# # Saída de dados
# for selecao in selecoes:
#     print("-" * 50)
#     print("Pais:", selecao)
#     print("Partidas:", dic[selecao]["partidas"])
#     print("Partidas decididas em tempo normal de jogo:", dic[selecao]["normal"])
#     print("Partidas decicidas nos penaltis:", dic[selecao]["penaltis"])
#     print("Vitorias:", dic[selecao]["vitorias"])
#     print("Derrotas:", dic[selecao]["derrotas"])
#     print("Gols marcados:", dic[selecao]["marcados"])
#     print("Gols sofridos:", dic[selecao]["sofridos"])
# print("-" * 50)
# print("Pais campeao:", campeao)
# print("-" * 50)
# ###################
# Quantidade de partidas disputadas.
# Quantidade de partidas decididas em tempo normal de jogo.
# Quantidade de partidas decicidas nos pênaltis.
# Número de vitórias.
# Número de derrotas.
# Quantidade de gols marcados.
# Quantidade de gols sofridos.
