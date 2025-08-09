from logic.lexer import lexical_analyzer, lexer_errors


def analyze_input(input_str: str):
    lexical_analyzer.input(input_str)
    tokens_list = []

    while True:
        tok = lexical_analyzer.token()
        if not tok:
            break
        token_info = {
            "type": tok.type,
            "value": tok.value,
            "line": tok.lineno,
        }
        tokens_list.append(token_info)

    return tokens_list, lexer_errors
