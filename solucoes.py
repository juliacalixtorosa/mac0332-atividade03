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

def encontrar_maior_palavra(sentenca):
    """
    Encontra a palavra mais longa em uma sentença, ignorando pontuação.
    
    Esta função analisa uma sentença e retorna a palavra com o maior número de 
    caracteres alfabéticos, removendo automaticamente sinais de pontuação.
    Em caso de empate, retorna a primeira palavra encontrada com o comprimento máximo.
    
    Args:
        sentenca (str): A sentença a ser analisada.
        
    Returns:
        str: A palavra mais longa sem pontuação, ou string vazia se não houver palavras válidas.
        
    Raises:
        TypeError: Se o parâmetro sentenca não for uma string.
        
    Examples:
        >>> encontrar_maior_palavra("O gato subiu no telhado!")
        'telhado'
        >>> encontrar_maior_palavra("Python é uma linguagem incrível.")
        'linguagem'
        >>> encontrar_maior_palavra("a, b, c!")
        'a'
        >>> encontrar_maior_palavra("")
        ''
    """
    if not isinstance(sentenca, str):
        raise TypeError("O parâmetro 'sentenca' deve ser uma string")
    
    pontuacao = {'.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '"', "'"}
    
    def limpar_palavra(palavra):
        """Remove pontuação de uma palavra."""
        return ''.join(char for char in palavra if char not in pontuacao)
    
    # Divide a sentença em palavras e processa cada uma
    palavras = sentenca.split()
    maior_palavra = ""
    maior_comp = 0
    
    for palavra in palavras:
        palavra_limpa = limpar_palavra(palavra)
        if len(palavra_limpa) > maior_comp:
            maior_comp = len(palavra_limpa)
            maior_palavra = palavra_limpa
    
    return maior_palavra
