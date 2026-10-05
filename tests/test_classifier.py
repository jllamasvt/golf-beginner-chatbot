from app.services.classifier import classify
def test_equipment(): assert classify('¿Qué palos necesito?')['category']=='equipment'
def test_rules():
 r=classify('¿Cuál es la regla para una bola provisional?'); assert r['category']=='rules' and r['priority_source']=='USGA'
def test_swing(): assert classify('¿Cómo mejoro mi grip?')['category']=='swing'
def test_unknown(): assert classify('¿Quién ganará un torneo en 2030?')['category']=='unknown'
