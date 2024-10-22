import random

class Forca:
    def __init__(self, palavras):
        self.palavras = palavras
        self.palavra_atual = random.choice(self.palavras)
        self.tentativas_restantes = 6
        self.letras_adivinhadas = set()

    def exibir_estado(self):
      from IPython.display import clear_output
      clear_output(wait=True)
      palavra_exibida = ""
      for letra in self.palavra_atual:
          if letra in self.letras_adivinhadas:
              palavra_exibida += letra
          else:
              palavra_exibida += "_"
      print(palavra_exibida)
      print("Tentativas restantes:", self.tentativas_restantes)
      if self.letras_adivinhadas:
          print("Letras adivinhadas:", ", ".join(self.letras_adivinhadas))
      return palavra_exibida

    def obter_palpite(self):
        while True:
            palpite = input("Digite uma letra: ").lower()
            if len(palpite) != 1 or not palpite.isalpha():
                print("Palpite inválido. Digite uma única letra.")
            elif palpite in self.letras_adivinhadas:
                print("Você já adivinhou essa letra. Tente outra.")
            else:
                return palpite

    def verificar_palpite(self, palpite):
        if palpite in self.palavra_atual:
            self.letras_adivinhadas.add(palpite)
            return True
        else:
            self.tentativas_restantes -= 1
            self.letras_adivinhadas.add(palpite)
            return False

    def verificar_fim_de_jogo(self):
        if "_" not in self.exibir_estado():
            print("Parabéns! Você ganhou!")
            return True
        elif self.tentativas_restantes == 0:
            print("Você perdeu! A palavra era", self.palavra_atual)
            return True
        else:
            return False
