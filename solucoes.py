def sao_anagramas(string1, string2):
    # TODO: implementar a lógica

    pass

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