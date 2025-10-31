def sao_anagramas(string1: str, string2: str) -> bool:
    """
    Verifica se duas strings são anagramas.
    Duas strings são consideradas anagramas se contiverem os mesmos caracteres 
    com as mesmas quantidades, independentemente da ordem.
    Args:
        string1 (str): A primeira string a ser comparada.
        string2 (str): A segunda string a ser comparada.
    Returns:
        bool: Retorna True se as strings forem anagramas, caso contrário, False.
    Raises:
        ValueError: Se algum dos argumentos não for uma string.
    Examples:
        >>> sao_anagramas("listen", "silent")
        True
        >>> sao_anagramas("hello", "world")
        False
        >>> sao_anagramas("As  tro nomer", "MOon sTarEr")
        True
    """

    if not isinstance(string1, str) or not isinstance(string2, str):
        raise ValueError("Ambos os argumentos devem ser strings.")
    
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    if len(string1) != len(string2):
        return False
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    return sorted_string1 == sorted_string2

def cifra_de_cesar(texto, deslocamento):
    # TODO: implementar a lógica

    pass

def encontrar_maior_palavra(frase):
    # TODO: implementar a lógica

    pass

