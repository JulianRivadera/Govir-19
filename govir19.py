import sys 

respuestas_afirmativas = 'MA VALE,CLARO,POR SUPUESTO,AFIRMATIVO,SI,ASI ES,OBVIO'
respuestas_negativas = 'NO,NEGATIVO,LA VERDAD QUE NO,MAOMENO,MAS O MENOS,JAJAJAJA'

def _print_welcome():
    print('')
    print('')
    print('*' * 50 + 'BIENVENIDO AL SISTEMA DE AUTODIAGNOSTICO DEL GOVIR-19' + '*' * 50)
    print('')
    print('')
    print('A continuacion se le realiazara una serie de preguntas para ver si su situacion es compatible con un posible caso de Govir') 
    print('')
    print('')   


def _preguntar_si_entendio():
    global respuestas_afirmativas
    respuesta = None

    while not respuesta:

        si = respuestas_afirmativas.split(',')
        no = respuestas_negativas.split(',')
        
        respuesta = input('¿Entendido?')
        respuesta = respuesta.upper()
        print('')
        if respuesta in si:
            print('PERFECTO')
            print('')
        elif respuesta in no or 'NO' in respuesta:
            print('¿SOS BOLUDO VOS?')
            sys.exit()    


def _fiebre():
    global respuestas_afirmativas
    global respuestas_negativas
    si = respuestas_afirmativas.split(',')
    no = respuestas_negativas.split(',')
    
    respuesta = None
    tiene = False
    while not respuesta:
        
        respuesta = input('¿Usted tiene fiebre?').upper()
        print('')
        if respuesta in si:
            print('UUHHH mal ahí, tas complicado, igual capaz nada que ver y tenes otra cosa')
            
            tiene = True    
        elif respuesta in no or 'NO' in respuesta:
            print('Bien')
            tiene = False
        else:
            respuesta = None
            print('No estaria Entendido')

    return tiene



def _tos():
    global respuestas_afirmativas
    global respuestas_negativas
    si = respuestas_afirmativas.split(',')
    no = respuestas_negativas.split(',')
    
    respuesta = None
    tiene = False
    print('')
    while not respuesta:
        respuesta = input('¿Usted tiene tos seca?').upper()
        print('')
        if respuesta in si:
            print('Ah la pelota, Oremos')
            tiene = True    
        elif respuesta in no or 'NO' in respuesta:
            print('Joya pá')
            tiene = False
        else:
            respuesta = None
            print('No estaria Entendido')
            

    return tiene


def _cansancio():
    global respuestas_afirmativas
    global respuestas_negativas
    si = respuestas_afirmativas.split(',')
    no = respuestas_negativas.split(',')
    
    respuesta = None
    tiene = False
    print('')
    while not respuesta:
        respuesta = input('¿Usted ultimamente siente más cansancio de lo normal?').upper()
        print('')
        if respuesta in si:
            print('Que feo')
            tiene = True    
        elif respuesta in no or 'NO' in respuesta:
            print('Bien')
            tiene = False
        else:
            respuesta = None
            print('No estaria Entendido')    

    return tiene


def _anosmia():
    global respuestas_afirmativas
    global respuestas_negativas
    si = respuestas_afirmativas.split(',')
    no = respuestas_negativas.split(',')
    
    respuesta = None
    tiene = False
    print('')
    while not respuesta:
        respuesta = input('¿Usted ultimamente sufrio de perdida del olfato o del gusto?').upper()
        print('')
        if respuesta in si:
            print('Con razón tanto olor a chivo y no te das cuenta')
            tiene = True    
        elif respuesta in no or 'NO' in respuesta:
            print('Vamo papá')
            tiene = False
        else:
            respuesta = None
            print('No estaria Entendido')    
            

    return tiene



def _erupciones():
    global respuestas_afirmativas
    global respuestas_negativas
    si = respuestas_afirmativas.split(',')
    no = respuestas_negativas.split(',')
    
    respuesta = None
    tiene = False
    print('')
    while not respuesta:
        respuesta = input('¿Usted sufre de erupciones cutáneas o pérdida del color en los dedos de las manos o de los pies?').upper()
        print('')
        if respuesta in si:
            print('hmmmm.....')
            tiene = True    
        elif respuesta in no or 'NO' in respuesta:
            print('Menos mal')
            tiene = False
        else:
            respuesta = None
            print('No estaria Entendido')    

    return tiene



def _preguntar_sintomas():
    probalilidad = 0

    if _fiebre() == True:
        probalilidad += 5

    if _tos() == True:
        probalilidad += 4

    if _cansancio() == True:
        probalilidad += 3

    if _anosmia() == True:
       probalilidad += 2

    if _erupciones() == True:
       probalilidad += 2


    print('')
    
    return probalilidad


    
def _dar_resultado(probalilidad):

    if probalilidad >= 10:
        print('Muy posiblemente tenes el govir, deberias llamar al 120')
    elif probalilidad >= 7:
        print('Capaz que tenés, capaz no, tranqui')
    else:
        print('No pasa una, tas bien')


_print_welcome()
_preguntar_si_entendio()
_dar_resultado(_preguntar_sintomas())