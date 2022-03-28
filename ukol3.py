def get_number_control(telephone_number):
    if "+420" in telephone_number:
        if len(telephone_number)==13:
            controlled=True
        else:
            controlled=False
    elif len(telephone_number)==9:
        controlled=True
    else: 
        controlled=False
    return controlled
def get_message_price(message):
    price=((len(message)//180)+1)*3
    return price
telephone_number=str(input("Zadejte číslo, kam bude zpráva odeslána:"))
controlled_number=get_number_control(telephone_number)
if controlled_number==False:
    print("Telefonní číslo není ve správném formátu, zadejte srávné telefonní číslo")
else:
    message=input("Zadejte text zprávy:")
    message_price=get_message_price(message)
    print(f"Cena sms na telefonní číslo {telephone_number} je {message_price} Kč")