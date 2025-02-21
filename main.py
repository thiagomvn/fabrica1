import datetime

def date_and_time():
    date_n_time = datetime.datetime.now()
    return date_n_time
    # Função p/coletar data e hora


name = str(input("Type in your name: "))
flight_number = str(input("Type in your flight number: "))
company = str(input("Type in the name of the flight company: "))
date_time = date_and_time() #retorna o horário de check-in
#Coleta de dados do usuário

print(f"Your name is {name}, flying for {company} in flight number {flight_number}, checked in at {date_time}")


    
