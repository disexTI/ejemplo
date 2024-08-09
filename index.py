import pandas as pd
import os

def escribirLineas():
    df = pd.read_excel("lista2.xlsx")
    archivo = open("resultado2.txt", "w")
    
    df.columns = df.columns.str.strip()

    numero_reg = 2
    archivo.write("000000100000001001\n")

    for i in range(len(df)):
        for color, sufijo in zip(["blanco", "claro", "oscuro"], ["B", "C", "O"]):
            
            columna = "f" + color.capitalize()
            
            linea = ""
            
            # F_NUMERO_REG
            linea += completarCeros(7, str(numero_reg))
            
            # F_TIPO_REG
            linea += "0126"
            
            # F_SUBTIPO_REG
            linea += "00"
            
            # F_VERSION_REG
            linea += "04"
            
            # F_CIA
            linea += "001"
            
            # F_ACTUALIZA_REG
            linea += "1"
            
            # f126_id_lista_precio
            linea += "500"  
            
            # f126_id_item
            linea += "0000000"
            
            # f126_referencia_item
            referencia = f"T{completarCeros(4, str(df['codigo'][i]))}{sufijo}"
            
            linea += completarEspacios(50, referencia)
            
            # F126_CODIGO_BARRAS_ITEM
            linea += completarEspacios(20, "")
            
            # f126_id_ext1_detalle
            linea += completarEspacios(20, "")
            
            # f126_id_ext2_detalle
            linea += completarEspacios(20, "")
            
            #Si fechaActivacion es un valor nulo, se debe reemplazar por el string 20240808
            if str(df[columna][i]) == "nan":
                #Terminar el ciclo
                break
            else:
                linea += str(df[columna][i]).replace(".0","")
            
            
            # f126_fecha_inactivacion
            linea += completarEspacios(8, "")
            
            # f126_id_promo_dscto
            linea += completarCeros(8, "")
            
            # f126_id_unidad_medida
            linea += completarEspacios(4, "KG")
            
            # f126_precio
            linea += "000000000000000.0000"
            
            # f126_precio_minimo
            precio_minimo = str(df[color][i]).replace("$", "").replace(",", "").replace(".0", "")
            if precio_minimo != "nan":
                linea += completarCeros(15, precio_minimo) + ".0000"
            else:
                break
                
                
                
            # f126_precio_maximo
            linea += completarCeros(20, "100000.0000")
            
            # f126_precio_sugerido
            linea += "000000000000000.0000"

            
            # f126_puntos_fiel
            linea += completarCeros(7, "")
            
            # f126_ind_exclusivo_oferta
            linea += "0"
            
            # f126_notas
            linea += completarEspacios(255, "")
            
            archivo.write(linea + "\n")
            numero_reg += 1

    archivo.write(completarCeros(7,str(numero_reg)) + "99990001001")     
    archivo.close()

def completarEspacios(tamano, cadena):
    if len(cadena) < tamano:
        espacios = tamano - len(cadena)
        cadena = cadena + (" " * espacios)
    return cadena

def completarCeros(tamano, cadena):
    if len(cadena) < tamano:
        ceros = tamano - len(cadena)
        cadena = "0" * ceros + cadena
    return cadena

def main():
    escribirLineas()

main()
