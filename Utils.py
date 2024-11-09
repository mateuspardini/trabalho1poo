class Utils:
    @staticmethod
    def confirm_action(message):
        while True:
            resposta = input(message).lower()
            if resposta in ['s', 'sim']:
                return True
            elif resposta in ['n', 'não', 'nao']:
                return False
            else:
                print("Por favor, responda com 's' para sim ou 'n' para não.")