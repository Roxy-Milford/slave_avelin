class AbstractTypewriter:
    def type(
            self,
            text: str,
            print_indent: bool=False,
            new_line: bool=False,
            last_in_line: bool=True
    ) -> None:
        """Standart output:

        Args:
            text (str): text for output
            print_indent (bool): print lines with aditional identation
                at start, default value = False
            new_line (bool): print gieven text in new line, if it dont ment
                by previous text output, default value = False
            last_in_line (bool): if True, the nex line could be writen in
                current line, default value = True

        Returns:
            None
        """
        pass

    def increase_indent(self) -> None:
        pass
    
    def decrease_indent(self) -> None:
        pass

class new_indent:
    def __init__(self, twr: AbstractTypewriter) -> None:
        self.twr = twr

    def __enter__(self) -> AbstractTypewriter:
        self.twr.increase_indent()
        
        return self.twr

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        self.twr.decrease_indent()

class Typewriter(AbstractTypewriter):
    """Standart console Typewriter"""
    def __init__(self) -> None:
        self._current_indent = 0
        self.INDENTATION = "... "
        self._is_on_new_line = True

        print("") # for space before any of typing sesion
    
    def __del__(self) -> None:
        print("")  # for space after any of typing sesion
    
    def type(
            self,
            text: str,
            print_indent: bool = False,
            new_line: bool = False,
            last_in_line: bool = True
    ) -> None:
        """Standart output:

        Args:
            text (str): text for output
            print_indent (bool): print lines with aditional identation
                at start, default value = False
            new_line (bool): print gieven text in new line, if it dont ment
                by previous text output, default value = False
            last_in_line (bool): if True, the nex line could be writen in
                current line, default value = True

        Returns:
            None
        """
        # TODO: create different print style for different objects, like table, image, etc..., use @overload
        if new_line and not self._is_on_new_line:  # become confident that you are on new line if needed
            print("")
            self._is_on_new_line = True
        
        if print_indent and self._is_on_new_line:  # only if we are on new line
            for _ in range(self._current_indent):
                print(self.INDENTATION, end="")

        # TODO: create check for long text messages
        print(text, end="")
        

        if last_in_line:
            print("")
            self._is_on_new_line = True
        else:
            self._is_on_new_line = False
    
    def increase_indent(self) -> None:
        self._current_indent += 1

    def decrease_indent(self) -> None:
        if self._current_indent != 0:
            self._current_indent -= 1

class EmptyTypewriter(AbstractTypewriter):
    pass



