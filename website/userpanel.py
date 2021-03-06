from flask import Blueprint, render_template, request, flash

userpanel = Blueprint('userpanel', __name__)
#----------------------------------------------------------------------------------------------------------------------------------------------------

@userpanel.route('/', methods=['GET', 'POST'])
def user_panel():
    if request.method == 'POST':
        numero_siret = request.form.get('numero_siret')
        nom_etablissement = request.form.get('nom_etablissement')
        adresse_etablissement = request.form.get('adresse_etablissement')
        code_postal_etablissement = request.form.get('code_postal_etablissement')
        commune_etablissement = request.form.get('commune_etablissement')
        geores_etablissement = request.form.get('géoloc_etablissement')
        metier = request.form.get('metier')

        if len(numero_siret) < 9:
            flash("Le numéro SIRET doit comporter 9 chiffres", category='error')
        elif len(nom_etablissement) < 2:
            flash("Le nom de l'établissement doit comporter plus de 1 caractère", category='error')
        elif len(adresse_etablissement) < 6:
            flash("L'adresse de l'établissement doit comporter plus de 5 caractère", category='error')
        elif len(code_postal_etablissement) < 5:
            flash("Le code postal doit comporter 5 chiffres", category='error')
        elif len(commune_etablissement) < 4:
            flash("Le nom de la commune doit comporter plus de 4 caractères", category='error')
        elif len(geores_etablissement) < 6:
            flash("La géolocalisation doit contenir plus de 6 chiffres", category='error')
        elif len(metier) < 4:
            flash("Le métier doit comporter plus de 3 caractères", category='error')
        else:
            flash("Prédiction réalisée !", category='success')

    return render_template('userpanel.html')