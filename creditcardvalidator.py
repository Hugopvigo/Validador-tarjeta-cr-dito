class creditCard:
    def __init__(self,card_no):
        self.card_no = card_no
  
    @classmethod
    def set_card(self,card_to_check):
        return self(card_to_check)

    @property
    def company(self):
        comp = None
        if str(self.card_no).startswith('4'):
            comp = 'VISA'
        elif str(self.card_no).startswith(('50','67','58','63')):
            comp='MAESTRO'

        elif str(self.card_no).startswith('5'):
            comp='MASTER CARD'
        elif str(self.card_no).startswith('37'):
            comp='AMEX'

# Ver si hay más tarjetas. Euro6000 y similares

        return 'Company: ' +comp

    def first_check(self):
        if 13 <= len(self.card_no) <= 19:
            message = "Verificación: Tarjeta de crédito válida"

        else:
            message = "Verificación: Tarjeta de crédito no válida"

        return message


card_number = input("Introduce el número de la tarjeta: ")
card = creditCard.set_card(card_number)
print(card.company)

print('Card: ',card.card_no)
print(card.first_check())
