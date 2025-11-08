def sao_anagramas(string1, string2):
    # TODO: implementar a lógica

    pass

def cifra_de_cesar(texto, deslocamento):
    # TODO: implementar a lógica

    pass

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