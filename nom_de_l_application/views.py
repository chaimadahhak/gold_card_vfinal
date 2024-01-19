# views.py
import csv
import re
import webbrowser

from django.http import JsonResponse
from django.shortcuts import render
from PIL import Image
import pytesseract
from jinja2 import Template
from gold_card.forms import ImageProcessingForm

# views.py

from rest_framework import generics
from .models import MonFormulaire
from .serializers import MonFormulaireSerializer

class MonFormulaireListCreateView(generics.ListCreateAPIView):
    queryset = MonFormulaire.objects.all()
    serializer_class = MonFormulaireSerializer


def process_identity_card_web(request):
    # Définir le chemin vers l'exécutable Tesseract OCR
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    # Chemin de l'image à traiter
    image_path = "D:\\nom_du_projet\\gold_card\\nom_de_l_application\\test.png"

    # Extraire le texte de l'image
    text = pytesseract.image_to_string(Image.open(image_path))

    # Nom du fichier CSV de sortie
    csv_filename = 'resultat_texte.csv'

    # Écrire le texte dans le fichier CSV
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Écrire chaque ligne de texte dans le fichier CSV
        for line in text.split('\n'):
            csv_writer.writerow([line])

    print(f"Résultat enregistré dans {csv_filename}")

    # Initialize the variables outside the loop
    a = ''
    b = ''
    c = ''
    e = ''
    n = ''
    l = ''
    cleaned_text = ''
    for line in text.split('\n'):
        # Ignorer les lignes vides
        if line.strip() != '':
            cleaned_text += line.strip() + '\n'
    # Lire les données à partir du fichier CSV
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Ignorer les 4 premières lignes
        for _ in range(4):
            next(csv_reader)

        # Lire les données de la 5ème ligne
        for i, row in enumerate(csv_reader):
            if i == 0:
                a = row[0]
                print("Nom:", a)
            elif i == 3:
                b = row[0]
                print("Prénom:", b)
            elif i == 5:
                c = row[0]
                print("Adresse:", c)
                break  # Quitter après la 10ème ligne
            elif i == 9:
                date_naissance = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', cleaned_text)
                l = date_naissance.group(1) if date_naissance else 't'
                print("date fin de carte:", l)

    # Prétraitement de l'image (conversion en niveaux de gris)
    image = Image.open(image_path).convert('L')

    # Ajuster les paramètres Tesseract
    custom_config = r'--oem 3 --psm 6'  # Utiliser le mode OEM 3 (LSTM) et le mode PSM 6 (bloc de texte)

    # Extraire le texte de l'image avec les paramètres personnalisés
    text = pytesseract.image_to_string(image, config=custom_config)

    # Nettoyer le texte extrait

    # Afficher le texte nettoyé dans le terminal
    date_naissance = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', cleaned_text)
    e = date_naissance.group(1) if date_naissance else ''
    print("Date de naissance:", e)
    # Extract all occurrences of the date pattern
    date_naissance_matches = re.finditer(r'\b(\d{2}/\d{2}/\d{4})\b', cleaned_text)

    # Initialize an empty list to store extracted dates
    dates_list = []

    # Iterate over matches and extract dates
    for match in date_naissance_matches:
        dates_list.append(match.group(1))
        print('tyy', dates_list)

    d=dates_list[1]
    print('vvvvvcha',d)

    # Assuming the first date is the date of birth and the second is the date of expiration
    date_naissance = dates_list[0] if dates_list else ''
    date_fin_carte = dates_list[1] if len(dates_list) > 1 else ''

    # Print or use the extracted dates as needed
    print("Date de naissance:", date_naissance)
    print("Date de fin de la carte:", l)

    # Utiliser la recherche pour le CIN avec le format "U" suivi de chiffres
    cin_match = re.search(r'U(\d+)', cleaned_text)
    n = cin_match.group(1) if cin_match else ''
    print("CIN:", n)

    dates = re.findall(r'(\d{2}/\d{2}/\d{4})', cleaned_text)

    # Assuming the second date in the list is the date de fin
    date_fin_carte = dates[1] if len(dates) > 1 else ''

    # Enregistrer les informations dans un fichier CSV
    resultat_csv_filename = 'resu.csv'
    with open(resultat_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['nom', a])
        csv_writer.writerow(['prenom', b])
        csv_writer.writerow(['adresse', c])
        csv_writer.writerow(['date_naissance', e])
        csv_writer.writerow(['cin', n])
        csv_writer.writerow(['date_fin_carte',  d])

    print(f"Informations enregistrées dans {resultat_csv_filename}")
    # Pass the extracted information to the template
    return render(request, 'formulaire_sophistique.html', {'a': a, 'b': b, 'c': c, 'e': e,'date_fin_carte': d, 'numero_carte': n})


def showDemoPage(request):
    return render(request, 'index.html')





def process_identity_card(request):
    # Définir le chemin vers l'exécutable Tesseract OCR
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    # Chemin de l'image à traiter
    image_path = "D:\\nom_du_projet\\gold_card\\nom_de_l_application\\test.png"

    # Extraire le texte de l'image
    text = pytesseract.image_to_string(Image.open(image_path))

    # Nom du fichier CSV de sortie
    csv_filename = 'resultat_texte.csv'

    # Écrire le texte dans le fichier CSV
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Écrire chaque ligne de texte dans le fichier CSV
        for line in text.split('\n'):
            csv_writer.writerow([line])

    print(f"Résultat enregistré dans {csv_filename}")

    # Initialize the variables outside the loop
    a = ''
    b = ''
    c = ''
    e = ''
    n = ''
    l = ''
    cleaned_text = ''
    for line in text.split('\n'):
        # Ignorer les lignes vides
        if line.strip() != '':
            cleaned_text += line.strip() + '\n'
    # Lire les données à partir du fichier CSV
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Ignorer les 4 premières lignes
        for _ in range(4):
            next(csv_reader)

        # Lire les données de la 5ème ligne
        for i, row in enumerate(csv_reader):
            if i == 0:
                a = row[0]
                print("Nom:", a)
            elif i == 3:
                b = row[0]
                print("Prénom:", b)
            elif i == 5:
                c = row[0]
                print("Adresse:", c)
                break  # Quitter après la 10ème ligne
            elif i == 9:
                date_naissance = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', cleaned_text)
                l = date_naissance.group(1) if date_naissance else 't'
                print("date fin de carte:", l)

    # Prétraitement de l'image (conversion en niveaux de gris)
    image = Image.open(image_path).convert('L')

    # Ajuster les paramètres Tesseract
    custom_config = r'--oem 3 --psm 6'  # Utiliser le mode OEM 3 (LSTM) et le mode PSM 6 (bloc de texte)

    # Extraire le texte de l'image avec les paramètres personnalisés
    text = pytesseract.image_to_string(image, config=custom_config)

    # Nettoyer le texte extrait

    # Afficher le texte nettoyé dans le terminal
    date_naissance = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', cleaned_text)
    e = date_naissance.group(1) if date_naissance else ''
    print("Date de naissance:", e)
    # Extract all occurrences of the date pattern
    date_naissance_matches = re.finditer(r'\b(\d{2}/\d{2}/\d{4})\b', cleaned_text)

    # Initialize an empty list to store extracted dates
    dates_list = []

    # Iterate over matches and extract dates
    for match in date_naissance_matches:
        dates_list.append(match.group(1))
        print('tyy', dates_list)

    d = dates_list[1]
    print('vvvvvcha', d)

    # Assuming the first date is the date of birth and the second is the date of expiration
    date_naissance = dates_list[0] if dates_list else ''
    date_fin_carte = dates_list[1] if len(dates_list) > 1 else ''

    # Print or use the extracted dates as needed
    print("Date de naissance:", date_naissance)
    print("Date de fin de la carte:", l)

    # Utiliser la recherche pour le CIN avec le format "U" suivi de chiffres
    cin_match = re.search(r'U(\d+)', cleaned_text)
    n = cin_match.group(1) if cin_match else ''
    print("CIN:", n)

    dates = re.findall(r'(\d{2}/\d{2}/\d{4})', cleaned_text)

    # Assuming the second date in the list is the date de fin
    date_fin_carte = dates[1] if len(dates) > 1 else ''

    # Enregistrer les informations dans un fichier CSV
    resultat_csv_filename = 'resu.csv'
    with open(resultat_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['nom', a])
        csv_writer.writerow(['prenom', b])
        csv_writer.writerow(['adresse', c])
        csv_writer.writerow(['date_naissance', e])
        csv_writer.writerow(['cin', n])
        csv_writer.writerow(['date_fin_carte', d])

    print(f"Informations enregistrées dans {resultat_csv_filename}")

    results = {
        'nom': a,
        'prenom': b,
        'adresse': c,
        'date_naissance': e,
        'numero_carte': n,
        'date_fin_carte': date_fin_carte,
    }

    return JsonResponse(results)


