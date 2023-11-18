

class Typewriter:
    def __init__(self):
        self._current_indent = 0
        self.INDENTATION = "... "

        print("")
    
    def __del__(self):
        print("")
    
    def type(self, text: str):
        """Standart output: treat as a paragraph"""
        print(text)

    def type_text(self, text: str):
        """Output for text in one paragraph"""
        print(text, end=" ")
    
    def ind_type(self, text: str):
        """Ouptut for text with some indentation before it"""
        for _ in range(self._current_indent):
            print(self.INDENTATION, end="")
        
        print(text)

    def type_new_line(self):
        pass

    def type_matrix(self):
        pass

    def type_formula(self):
        pass

    def type_image(self):
        pass


class new_indent:
    def __init__(self, twr: Typewriter) -> None:
        self.twr = twr

    def __enter__(self):
        self.twr._current_indent += 1
        
        return self.twr

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.twr._current_indent -= 1



