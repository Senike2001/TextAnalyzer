def analyze_text(text):
    """
    Analyse un texte donné.
    :param text: Chaîne de caractères
    :return: Dictionnaire contenant des statistiques
    """
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    keywords = [word for word in words if len(word) > 5]

    return {
        "word_count": word_count,
        "char_count": char_count,
        "keywords": keywords,
    }

if __name__ == "__main__":
    sample_text = input("Entrez un texte à analyser : ")
    result = analyze_text(sample_text)
    print("Résultats de l'analyse :")
    print(f"Nombre de mots : {result['word_count']}")
    print(f"Nombre de caractères : {result['char_count']}")
    print(f"Mots clés (> 5 caractères) : {', '.join(result['keywords'])}")
