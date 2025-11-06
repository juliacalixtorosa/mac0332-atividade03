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
    
    return sorted(string1) == sorted(string2)

def cifra_de_cesar(texto: str, deslocamento: int) -> str:
    """Aplica a cifra de César a uma string.

    A função desloca apenas letras ASCII (A-Z, a-z), preservando maiúsculas/minúsculas.
    Caracteres que não sejam letras são mantidos inalterados. O deslocamento pode ser
    positivo ou negativo; valores maiores que 26 são reduzidos módulo 26.

    Args:
        texto (str): texto de entrada a ser cifrado.
        deslocamento (int): número de posições para deslocar as letras. Pode ser negativo.

    Returns:
        str: texto resultante após aplicação da cifra de César.

    Raises:
        TypeError: se `texto` não for uma string ou `deslocamento` não for um inteiro.

    Examples:
        >>> cifra_de_cesar("abc", 3)
        'cde'
        >>> cifra_de_cesar("xyz", 3)
        'abc'
        >>> cifra_de_cesar("Ataque à Noite!", 5) # caracteres não-ASCII permanecem inalterados
        'Fyfvzj à Stynj!'
    """
    if not isinstance(texto, str):
        raise TypeError("O parâmetro 'texto' deve ser uma str")
    if not isinstance(deslocamento, int):
        raise TypeError("O parâmetro 'deslocamento' deve ser um int")

    desloc = deslocamento % 26  # mapeia pro intervalo [0, 25]

    def _desloca_char(ch: str) -> str:
        o = ord(ch)
        if 'A' <= ch <= 'Z':
            base = ord('A')
            return chr(base + (o - base + desloc) % 26)
        if 'a' <= ch <= 'z':
            base = ord('a')
            return chr(base + (o - base + desloc) % 26)
        # outros caracteres não são modificados
        return ch

    return ''.join(_desloca_char(c) for c in texto)

def encontrar_maior_palavra(frase):
    # TODO: implementar a lógica

    pass

