# Les API

Une **API** (Application Programming Interface) permet aux développeurs d'**intégrer** une application à une autre. Cela peut permettre par exemple de récupérer des données structurées depuis un site web pour les exploiter de manière automatisée dans un programme.

Il existe différents types d'API, notamment les **API Web** permettant d'**accéder à des données**.  
Pour ce type d'API, une méthode consiste à émettre une **requête HTTP** permettant de récupérer des **données** sur un serveur web.

Il existe différents formats structurants de données, notamment le format **XML** (proche du HTML) et le format **JSON**, qui sont devenus des standards.

Voici quelques exemples d'API :

- [https://openweathermap.org/api](https://openweathermap.org/api){ target="_blank" } - Diverses API concernant le climat et la météo,
- [https://openfoodfacts.org/data](https://openfoodfacts.org/data){ target="_blank" } - Base de données collaborative, libre et ouverte des produits alimentaires du monde entier,
- [https://openstreetmap.fr/](https://openstreetmap.fr/){ target="_blank" } - Un projet collaboratif de cartographie en ligne qui vise à constituer une base de données géographiques libre du monde, en utilisant le système GPS et d'autres données libres.

## Activité - Récupérer la météo dans un programme Python

Pour cette activité, on souhaite récupérer des données sur la **météo** de différentes villes en utilisant les données fournies par l'API de [openweathermap.org](https://openweathermap.org/){ target="_blank" }.

Plus précisément, on utilisera la **météo actuelle**, vous pouvez vous rendre sur [cette page](https://openweathermap.org/current){ target="_blank" } pour voir les différentes façons de faire un appel avec l'API. Vous pouvez notamment utiliser la **latitude**, la **longitude**, le **nom de la ville**, le **code postal**...  
**openweathermap** fournit des données en JSON, XML et HTML. Nous utiliserons ici le format **JSON**.

!!! success "À télécharger"
    - [meteo.py](src/meteo.py){ target="_blank" } : Programme initial à compléter

Le module `requests` de Python permet de récupérer des données sur le web **au format JSON** et de les intégrer dans un **dictionnaire**.

!!! tip "Utilisation du programme"
    Ouvrez le script `meteo.py` dans **Thonny** (ou dans votre IDE préféré), puis exécutez-le.

    En appelant `get_weather('Paris')`, vous devriez obtenir quelque chose comme ceci :
    ```python
    {'coord': {'lon': 2.3488, 'lat': 48.8534}, 
    'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 
    'base': 'stations', 
    'main': {'temp': 23.67, 'feels_like': 24, 'temp_min': 20.32, 'temp_max': 24.52, 'pressure': 1024, 'humidity': 73}, 
    'visibility': 10000, 
    'wind': {'speed': 5.14, 'deg': 60}, 
    'clouds': {'all': 0}, 
    'dt': 1693777827, 
    'sys': {'type': 2, 'id': 2041230, 'country': 'FR', 'sunrise': 1693717783, 'sunset': 1693765857}, 
    'timezone': 7200, 
    'id': 2988507, 
    'name': 'Paris', 
    'cod': 200}
    ```

!!! note "Exercice 1"
    Complétez la fonction `temperature_ressentie` permettant d'**afficher** la température ressentie (*feels_like*) dans une ville donnée en entrée.

!!! tip "Rappel"
    En bas du script, vous pouvez voir le bloc de code suivant :
    ```python
    if __name__ == '__main__':
        ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
        pass
    ```

    Les instructions saisies dans ce bloc ne seront prises en compte que si le script est exécuté directement. Si `meteo.py` est importé dans un autre script, ces instructions seront ignorées.

!!! note "Exercice 2"
    En vous inspirant des deux fonctions précédentes, complétez la fonction `get_temp_from_lat_long` permettant d'**afficher** la **température** (*temp*) d'un lieu localisé par sa valeur de **latitude** et de **longitude** (voir [documentation](https://openweathermap.org/current){ target="_blank" } si besoin).

    Faites le test avec `lat = 50.65243094755832, long = 3.0266403128894583` (localisation de Lambersart).

On souhaite maintenant obtenir les **prévisions météo** d'une ville de manière à **afficher une courbe d'évolution** de la **température** (*temp*) prévue.  
L'API permet d'obtenir les prévisions des **5 prochains jours**, à raison **d'une mesure toutes les 3 heures**. Ainsi, on obtiendra **40 mesures**, voir [cette page](https://openweathermap.org/forecast5){ target="_blank" } pour la documentation.

Voici un exemple de graphe affichant la comparaison entre l'évolution de la température de la ville de **Paris** et celle de la ville de **Lambersart**, sur les 5 prochains jours :

<figure markdown>
  ![Courbes d'évolution température](images/courbe_previsions.png){ width="500px" }
  <figcaption>Courbes d'évolution des températures</figcaption>
</figure>

!!! note "Exercice 3"
    Complétez la fonction `compare_two_cities` prenant deux noms de villes en entrée, et affichant un graphe contenant les courbes d'évolution de la température de ces deux villes.

    Faites le test avec deux villes de votre choix.

!!! tip "Aide exercice 3"
    Vous pouvez consulter [cette page](http://www.python-simple.com/python-matplotlib/pyplot.php){ target="_blank" } pour des rappels concernant le module **pyplot**. N'oubliez pas d'importer le module dans votre script !

    En l'occurence, vous n'aurez besoin que des fonctions `plot` et `show`, et éventuellement de `legend` si vous souhaitez afficher des légendes.