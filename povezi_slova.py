print('Odaberite tezinu igre:\nunesite broj 1 za LAGANO\nunesti broj 2 za SREDNJE TESKO\nodaberite broj 3 za TESKO')

#varijabla za odabir tezine
odabir_tezine = 0

#petlja koja provjerava je li odabrana tezina tocna
while odabir_tezine not in (1, 2, 3):
	odabir_tezine = int(input())
	if odabir_tezine not in (1, 2, 3):
		print('Broj koji ste unijeli nije ponuden, pokusajte ponovo')

#bodovi koje imamo
bodovi = 0

#lagana razina
if odabir_tezine == 1:
	#isprintaj slova
	print('  I\nM   A\n  L')
	#moguc broj bodova
	ukupno_bodova_lagano = 3
	#moguce rijeci
	rijeci_lagano = ['ima', 'lim', 'mali']
	#dok ne pronademo sve rijeci, igra ne prestaje
	while bodovi < ukupno_bodova_lagano:
		pokusaj = input()
		#ako smo pogodili rijec
		if pokusaj in rijeci_lagano:
			bodovi += 1
			rijeci_lagano.remove(pokusaj)
		#ako smo pogrjesili rijec
		else:
			print('Molimo pokusajte ponovo')
	print('Cestitamo presli ste laganu razinu')

#srednja razina
elif odabir_tezine == 2:
	#isprintaj slova
	print('  D\nO   M\n A H')
	#moguc broj bodova
	ukupno_bodova_srednje = 7
	#moguce rijeci
	rijeci_srednje = ['odmah', 'do', 'od', 'dom', 'doma', 'moda', 'mah']
	#dok ne pronademo sve rijeci, igra ne prestaje
	while bodovi < ukupno_bodova_srednje:
		pokusaj = input()
		#ako smo pogodili rijec
		if pokusaj in rijeci_srednje:
			bodovi += 1
			rijeci_srednje.remove(pokusaj)
		#ako smo pogrjesili rijec
		else:
			print('Molimo pokusajte ponovo')
	print('Cestitamo presli ste srednju razinu')

#teska razina
else:
	#isprintaj slova
	print(' D\nO K\nM A\n O')
	#moguc broj bodova
	ukupno_bodova_tesko = 10
	#moguce rijeci
	rijeci_tesko = ['dok', 'do', 'od', 'dom', 'doma', 'moda', 'komad', 'komoda', 'koma', 'kod']
	#dok ne pronademo sve rijeci, igra ne prestaje
	while bodovi < ukupno_bodova_tesko:
		pokusaj = input()
		#ako smo pogodili rijec
		if pokusaj in rijeci_tesko:
			bodovi += 1
			rijeci_tesko.remove(pokusaj)
		#ako smo pogrjesili rijec
		else:
			print('Molimo pokusajte ponovo')
	print('Cestitamo presli ste tesku razinu')