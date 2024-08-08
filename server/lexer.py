from typing import List, NamedTuple



# Define a Token class using NamedTuple
class Token(NamedTuple):
    type: str
    value: str
    position: int


# Define a lexer class
class HtmlLexer:
    def __init__(self, input_text: str):
        self.input_text = input_text
        self.position = 0
        self.tokens: List[Token] = []

    def lex(self) -> List[Token]:
        while self.position < len(self.input_text):
            current_char = self.input_text[self.position]

            if current_char == '<':
                self._lex_tag_open()
            elif current_char == '>':
                self._lex_tag_close()
            elif current_char == '/':
                self._lex_slash()
            elif current_char == '=':
                self._lex_equals()
            elif current_char in '"\'':
                self._lex_string()
            elif current_char.isspace():
                self._lex_whitespace()
            else:
                self._lex_identifier()
        
        return self.tokens

    def _lex_tag_open(self):
        self.tokens.append(Token(type='TAG_OPEN', value='<', position=self.position))
        self.position += 1

    def _lex_tag_close(self):
        self.tokens.append(Token(type='TAG_CLOSE', value='>', position=self.position))
        self.position += 1

    def _lex_slash(self):
        self.tokens.append(Token(type='SLASH', value='/', position=self.position))
        self.position += 1

    def _lex_equals(self):
        self.tokens.append(Token(type='EQUALS', value='=', position=self.position))
        self.position += 1

    def _lex_string(self):
        quote_type = self.input_text[self.position]
        self.position += 1
        start_position = self.position

        while self.position < len(self.input_text) and self.input_text[self.position] != quote_type:
            self.position += 1

        string_value = self.input_text[start_position:self.position]
        self.tokens.append(Token(type='STRING', value=string_value, position=start_position))
        self.position += 1  # Skip the closing quote

    def _lex_whitespace(self):
        start_position = self.position
        while self.position < len(self.input_text) and self.input_text[self.position].isspace():
            self.position += 1
        whitespace_value = self.input_text[start_position:self.position]
        self.tokens.append(Token(type='WHITESPACE', value=whitespace_value, position=start_position))

    def _lex_identifier(self):
        start_position = self.position
        while (self.position < len(self.input_text) and
               (self.input_text[self.position].isalnum() or self.input_text[self.position] in '-_')):
            self.position += 1
        identifier_value = self.input_text[start_position:self.position]
        self.tokens.append(Token(type='IDENTIFIER', value=identifier_value, position=start_position))
