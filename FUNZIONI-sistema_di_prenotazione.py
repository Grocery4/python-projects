# Immagina un'applicazione di prenotazione di hotel che consenta di definire una funzione per registrare una 
# prenotazione, con vari parametri che comprendono i dettagli del cliente, la camera scelta, e altre opzioni. 
# Utilizzeremo tutti i concetti sopra descritti per costruire questo esempio.

from enum import Enum

class Camera(Enum):
    ECONOMY = 0
    STANDARD = 1
    BUSINESS = 2
    LUXURY = 3
    

class Prenotazione:
	def __init__(self, nc, tc, ds, *oe, **dp):
		self.nc = nc
		self.tc = tc
		self.ds = ds
		self.oe = oe # tuples
		self.dp = dp # dictionary

		calcola_prezzi() # TODO

def prenota_camera(nome_cliente, tipo_camera = Camera.STANDARD, durata_soggiorno = 3, *opzioni_extra, **dettagli_pagamento):

	# Gestione prezzi
	prezzo_base = 0

	if tipo_camera == Camera.LUXURY:
		prezzo_base = 150
	else:
		prezzo_base = 100

	prezzo_totale = prezzo_base
	
	# Inserimento opzioni extra
	for op in opzioni_extra:
		prezzo_totale += 10

	
	
	print("Riepilogo prenotazione:")
	print("Costo totale: ", prezzo_totale, "€")

	print('\n', "Opzioni extra:")
	for op in opzioni_extra:
		print("- ", op)	

	# Gestione dettagli pagamento
	print('\n', "Dettagli pagamento:")
	if dettagli_pagamento != None:
		for dt, val in dettagli_pagamento.items():
			print("- ", dt, ": ", val)
	

prenota_camera("Judd Russel Kalalo", Camera.LUXURY, 5, "Bagno Privato", "Vista panoramica", "Servizio in camera", metodo="Carta di Credito", numero_transazione = 1137124)
