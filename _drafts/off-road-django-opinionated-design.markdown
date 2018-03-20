## Translation Files

En fait, quand on utilise "My text", on utilise aussi la commande `python manage.py makemessages`. Cela va mettre à jour les fichiers `.po`. Malheureusement, ce mécanisme change beaucoup les fichiers `.po` au point d'avoir des conflits si au moins 2 développeurs mettent à jour les traductions. Comme ça arrivé tout le temps, tout le temps, on a décidé de gérer les fichiers `.po` manuellement.

Avec une clé, il y a moins de risque de se tromper. Par exemple: "My text" peux être ajouté dans le fichier `.po` comme "My Text" ou "My  text" (deux espaces). Avec tout minuscule et souligner pour les espaces ce risque est réduit.

En anglais c'est "My Text", mais c'est plutôt un problème de traduction du terme, pas lié à la façon que les traductions sont organisés, non ?


[9:38]
MY_TEXT c'est utilisé pour traduire les énumérations. Comme ça, un lowercase n'est pas nécessaire avant de le traduire.
