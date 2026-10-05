RULES={'rules':['regla','reglas','usga','penalización','penalizacion','fuera de límites','fuera de limites','bunker','búnker','bola provisional','injugable','green','tee'],'equipment':['palo','palos','club','clubs','driver','hierro','híbrido','hibrido','wedge','putter','pelota','guante','zapatos','bolsa'],'swing':['swing','grip','agarre','postura','backswing','downswing','tempo','alineación','alineacion'],'benefits':['beneficio','beneficios','salud','mental','social','bienestar'],'etiquette':['etiqueta','seguridad','ritmo','pace','distracción','distraccion','cuidar el campo'],'fundamentals':['empezar','principiante','principios','fundamentos','clases','práctica','practica','driving range','primera ronda','tees']}
PRIORITY={'rules':'USGA','equipment':'Golf Digest','swing':'GOLF.com','benefits':'American Golf','etiquette':'USGA','fundamentals':'PGA'}
def classify(question):
    q=question.lower()
    for category,words in RULES.items():
        if any(w in q for w in words): return {'category':category,'subcategory':'general','priority_source':PRIORITY.get(category)}
    return {'category':'unknown','subcategory':'general','priority_source':None}
