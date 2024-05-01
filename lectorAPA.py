from pdfminer.high_level import extract_text
import re
import os

def extraer_contenido_fuentes(pdf_path):
    texto = extract_text(pdf_path)

    # New (2014)
    regex_apa = re.compile(r'\(\d{4}\)')

    fuentes_encontradas = re.finditer(regex_apa, texto)
    
    inicio_citas = [match.start() for match in fuentes_encontradas] + [len(texto)]

    contenido_por_fuente = []
    for i in range(len(inicio_citas) - 1):
        inicio = inicio_citas[i]
        fin = inicio_citas[i + 1]
        contenido = texto[inicio:fin].strip()

        # Identificar la fuente actual
        match_fuente = re.search(regex_apa, contenido)

        contenido_por_fuente.append(f"Fuente numero {i}: {contenido}")
    
    return contenido_por_fuente

def inicializar( recursivo = False ):
    contenido_por_fuente = []
    if recursivo:
        path = "./pdfs"
        lista_directorio = os.listdir(path)
        print("Files in '", path, "' :")
        for archivo in lista_directorio:
            pdf_path = os.path.join(path, archivo)
            contenido_por_fuente.extend(extraer_contenido_fuentes(pdf_path))
    else:
        pdf_path = "Restorative and regenerative_ Exploring the concepts in the circular econom..._ Discovery Service for UNIVERSIDAD BLAS PASCAL.pdf"
        contenido_por_fuente = extraer_contenido_fuentes(pdf_path)

    # print(f"Contenido por fuente \n{contenido_por_fuente} ")

    if contenido_por_fuente:
        return contenido_por_fuente
    else:
        print("No se encontró contenido relacionado con fuentes en formato APA.")



# Utiliza PyPDF2
''' 
import PyPDF2
import re
import os

def extraer_contenido_fuentes(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        contenido_por_fuente = []

        # print(f"Paginas: {len(reader.pages)}")

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            texto = page.extract_text()

            # Old (AFP, 2014) | (2014) | garbage
            # regex_apa = re.compile(r'\(\w+,\s\d+\)|\w+(?:\s+&\s+\w+)?\s\(?\d{4}(?:[-\w]*,?\s?\d{0,2})?\)?')

            # New (2014)
            regex_apa = re.compile(r'\(\d{4}\)')

            fuentes_encontradas = re.finditer(regex_apa, texto)
            
            inicio_citas = [match.start() for match in fuentes_encontradas] + [len(texto)]

            for i in range(len(inicio_citas) - 1):
                inicio = inicio_citas[i]
                fin = inicio_citas[i + 1]
                contenido = texto[inicio:fin].strip()

                # Identificar la fuente actual
                match_fuente = re.search(regex_apa, contenido)
                if match_fuente:
                    fuente_actual = match_fuente.group()

                contenido_por_fuente.append(f"Fuente numero {i}: {contenido}")
    return contenido_por_fuente

def inicializar( recursivo = False ):
    contenido_por_fuente = []
    if ( recursivo ):
        path = "./pdfs"
        lista_directorio = os.listdir(path)
        print("Files in '", path, "' :")
        ## print(lista_directorio)
        for archivo in lista_directorio:
            pdf_path = path + "/" + archivo
            contenido_por_fuente.append(extraer_contenido_fuentes(pdf_path))
    else:
        pdf_path = "Restorative and regenerative_ Exploring the concepts in the circular econom..._ Discovery Service for UNIVERSIDAD BLAS PASCAL.pdf"
        # pdf_path = "./pdfs/\'Systemic thinking\', \'regenerative culture\', and new forms of prefigurative..._ Discovery Service for UNIVERSIDAD BLAS PASCAL.pdf"
        contenido_por_fuente = extraer_contenido_fuentes(pdf_path)

    print(f"Contenido por fuente \n{contenido_por_fuente} ")

    if contenido_por_fuente:
            #print("Contenido relacionado con fuentes en formato APA:")
            #for i, fragmento in enumerate(contenido_por_fuente, start=1):
            #print(f"{i}. {fragmento}\n")
        return contenido_por_fuente
    else:
        print("No se encontró contenido relacionado con fuentes en formato APA.")

'''         