def letras_numero(entrada):
     

    unidades = {
        "1": "uno",
        "2": "dos",
        "3": "tres",
        "4": "cuatro",
        "5": "cinco",
        "6": "seis",
        "7": "siete",
        "8": "ocho",
        "9": "nueve",
        "0": ''
        }

    decenas = { 
        "10": "diez",
        "11": "once",
        "12": "doce",
        "13": "trece",
        "14": "catorce",
        "15": "quince",
        "16": "dieciséis",
        "17": "diecisiete",
        "18": "dieciocho",
        "19": "diecinueve", 
        "20": "veinte",
        "2": "veinti",
        "3": "treinta y",
        "30": "treinta",
        "40": "cuarenta",
        "41": "cuarenta y",
        "50": "cincuenta",
        "5": "cincuenta y",
        "60": "sesenta",
        "6": "sesenta y",
        "70": "setenta",
        "7": "setenta y",
        "80": "ochenta",
        "8": "ochenta y",
        "90": "noventa",
        "9": "noventa y",
        "0": ''
        }

    centenas = {  
        "100": "cien",
        "1": "ciento",
        "2": "doscientos",
        "3": "trescientos",
        "4": "cuatrocientos",
        "5": "quinientos",
        "6": "seiscientos",
        "7": "setecientos",
        "8": "ochocientos",
        "9": "novecientos",
        "0": ''

    }

    salida = ""
    salida2 =""
    decena = 0
    decena2 = 0
    clave = 0
    valor = ""
    tamanio = len(entrada)
    if tamanio == 3:
            decena = entrada[0]
            decena2 = entrada[1]
            decena3 = entrada[2]
            decena_total = decena2 + decena3
            centena = decena + decena2 + decena3
            if centena == "100":
                salida = centenas.get(centena, "!")
                print(f"{salida}.")
            elif centena[1] == "0" and centena[2] == "0":
                salida = centenas.get(decena, "!")
                print(salida)
            elif centena[1] == "0" and centena[0] != "0" and centena[2]:
                salida = centenas.get(decena, "!") + " "
                salida = salida + unidades.get(decena3, "!")
                print(salida)
            elif centena[2] == "0":
                salida = centenas.get(decena, "!") + " "
                if decena_total in decenas:
                    salida = salida + decenas[decena_total]
                    print(salida)
            elif centena[0] != "0" and centena[1] != "0" and centena[2] != "0":
                salida = centenas.get(decena, "!") + " "
                if decena_total in decenas:
                    valor = decenas[decena_total]
                    salida = salida + valor
                    print(salida)
                elif centena[1] == "2" and centena [2] > "0":
                    salida = salida + decenas.get(decena2, "!") 
                    salida = salida + unidades.get(decena3, "!")
                    print(salida)
                else:
                    salida = salida + decenas.get(decena2, "!") + " "
                    salida = salida + unidades.get(decena3, "!") + " "
                    print(salida)
    elif tamanio == 2:
            decena = entrada[0]
            decena2 = entrada[1]
            clave = decena + decena2
            if clave in decenas:
                valor = decenas[clave]
                print(f"{valor}.")
            else:
                salida = decenas.get(decena, "!") + " "
                salida = salida + unidades.get(decena2, "!") + " "
                print(salida)
    elif tamanio == 1:
        salida = unidades.get(entrada)
        print(f"{salida}")
    else:
        print("Numero maximo de digitos rebasado")

entrada = str(120)
print(letras_numero(entrada))

