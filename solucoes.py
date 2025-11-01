def sao_anagramas(string1, string2):
    # TODO: implementar a lógica

    pass

def cifra_de_cesar(texto, deslocamento):
    # TODO: implementar a lógica

    pass

def find_longest_word(sentence):
    """
    Encontra a palavra mais longa em uma sentença, ignorando pontuação.
    
    Esta função analisa uma sentença e retorna a palavra com o maior número de 
    caracteres alfabéticos, removendo automaticamente sinais de pontuação.
    Em caso de empate, retorna a primeira palavra encontrada com o comprimento máximo.
    
    Args:
        sentence (str): A sentença a ser analisada.
        
    Returns:
        str: A palavra mais longa sem pontuação, ou string vazia se não houver palavras válidas.
        
    Raises:
        TypeError: Se o parâmetro sentence não for uma string.
        
    Examples:
        >>> find_longest_word("O gato subiu no telhado!")
        'telhado'
        >>> find_longest_word("Python é uma linguagem incrível.")
        'linguagem'
        >>> find_longest_word("a, b, c!")
        'a'
        >>> find_longest_word("")
        ''
    """
    if not isinstance(sentence, str):
        raise TypeError("O parâmetro 'sentence' deve ser uma string")
    
    punctuation = {'.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '"', "'"}
    
    def clean_word(word):
        """Remove pontuação de uma palavra."""
        return ''.join(char for char in word if char not in punctuation)
    
    # Divide a sentença em palavras e processa cada uma
    words = sentence.split()
    longest_word = ""
    max_length = 0
    
    for word in words:
        cleaned_word = clean_word(word)
        if len(cleaned_word) > max_length:
            max_length = len(cleaned_word)
            longest_word = cleaned_word
    
    return longest_word

print(find_longest_word("O gato rato no !"))  # Exemplo de uso da função