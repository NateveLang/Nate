import  nate.grammar as     gr
from    nate.token import   get_token_ID, Token, TokenType
from    nate.zones import   Zone

# Main code

def parser(tokens, file_name = "root", errors = 0):
    n = len(tokens)
    expected_types = gr.ALL
    expecting = False
    errors = 0
    function_declaration = False
    class_declaration = False
    
    last_line = tokens.last_line
    eof_token = TokenType().EOF(last_line[0], last_line[1])
    tokens.append(eof_token)

    #Initialize the tree
    tree = Zone(file_name, 0, "class")
    tk = [Token('(', get_token_ID('('), -1, 2, 1), Token(')', get_token_ID(')'), -1, 3, 1), Token(':', ':', -1, 1, 1)]
    
    for t in tk:
        tree.declaration.append(t)
    
    zone = tree
    declaration, statements = False, True

    if errors > 0:
        return tree, tokens, errors

    i = 0
    while i < n:
        token = tokens[i]
        """
        # SyntaxError, doen't work well with the new lexer
        if expecting:

            if token.is_expected(expected_types):
                expecting = False
            else:
                errors += 1
                break
            
        else:
            expected_types = gr.ALL
            expecting = True
        """
        assert len(token) > 3

        if function_declaration:
            declaration = True
            statements = False
            zone = Zone(token.symbol, token.line, type = "function", parent = zone)
            function_declaration = False

        elif class_declaration:
            declaration = True
            statements = False
            zone = Zone(token.symbol, token.line, type = "class", parent = zone)
            class_declaration = False

        if token.equal(gr.USE):
            expected_types = [gr.STRING]
            expecting = True

        elif token.equal(gr.USE):
            expected_types = [gr.STRING]
            expecting = True
        
        #elif token.equal(gr.WAIT):
        #    expected_types = [gr.INT, gr.FLOAT]
        #    expecting = True

        elif token.equal(gr.INCLUDE):
            expected_types = [gr.STRING]
            expecting = True

        elif token.symbol in gr.conditionals + [gr.WHILE, gr.FOR]:
            zone = Zone(token.symbol, token.line, parent = zone)
            declaration = True
            statements = False

        elif token.symbol == gr.OPERATOR:
            function_declaration = True

        elif token.symbol == gr.CLASS:
            class_declaration = True
        
        elif declaration:

            if token.symbol != zone.name:
                zone.declaration.append(token) # It includes ":"
            if token.symbol == "{":
                declaration = False
                statements = True
                token[0] = ":" # set symbol to ":"
                token[1] = ":" # set ID to ":"

        elif statements:

            if token.symbol == "}":
                eoz_token = TokenType().EOZ(last_line[0], last_line[1])
                zone.statements.append(eoz_token)
                
                closed_zone = zone
                zone = zone.parent
                zone.statements.append(closed_zone) # closed_zone.name added to zone.name
            else:
                zone.statements.append(token)
        
        i += 1
    
    tree.statements.append(eof_token)

    return tree, tokens, errors
        