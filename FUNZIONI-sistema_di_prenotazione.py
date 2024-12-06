# Immagina un'applicazione di prenotazione di hotel che consenta di definire una funzione per registrare una 
# prenotazione, con vari parametri che comprendono i dettagli del cliente, la camera scelta, e altre opzioni. 
# Utilizzeremo tutti i concetti sopra descritti per costruire questo esempio.

from enum import Enum
class Camera(Enum):
    ECONOMY = 0
    STANDARD = 1
    BUSINESS = 2
    LUXURY = 3

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

class Prenotazione:
	def __init__(self, nc, ds, tc = Camera.STANDARD, *oe, **dp):
		self.nc = nc
		self.tc = tc
		self.ds = ds
		self.oe = oe # tuples
		self.dp = dp # dictionary

		self.calcola_prezzi()
		self.stampa_prenotazione()

	def calcola_prezzi(self):
		self.prezzo = 0
		if self.tc == Camera.LUXURY:
			self.prezzo = 150
		else:
			self.prezzo = 100

		for op in self.oe:
			self.prezzo += 10


	def stampa_prenotazione(self):
		print("Riepilogo prenotazione:")
		print("Costo totale: ", self.prezzo, "€")

		print('\n', "Tipologia camera: ")
		print("-", self.tc.name)

		print('\n', "Opzioni extra:")
		for op in self.oe:
			print("- ", op)	

		print('\n', "Dettagli pagamento:")
		if self.dp != None:
			for dt, val in self.dp.items():
				print("- ", dt.capitalize().replace("_", " "), ": ", val)

Prenotazione("Judd Russel Kalalo", 5, Camera.LUXURY, "Bagno Privato", "Vista panoramica", "Servizio in camera", metodo="Carta di Credito", numero_transazione = 1137124)
