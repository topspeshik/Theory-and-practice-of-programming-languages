from ilib.interpreter import Interpreter, InterpreterException
from ilib.parser import ParserException
from ilib.lexer import LexerException

import pytest
import socket


class TestInterpreter:
    
    def test_interpreter(self):
        interp = Interpreter()
        assert interp.eval("BEGIN y:= 2; BEGIN a := 3; a := a; b := 10 + a + 10 * y / 4; c := a - b; END; x := 11; END.")\
               == {'y': 2.0, 'a': 3.0, 'b': 18.0, 'c': -15.0, 'x': 11.0}

        interp1 = Interpreter()
        assert interp1.eval("BEGIN END.")  == {}


        interp2 = Interpreter()
        assert interp2.eval("BEGIN x:= 2 + 3 * (2 + 3); y:= 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1)); END.")  == {'x': 17.0, 'y': 11.0}

        interp3 = Interpreter()
        assert interp3.eval("BEGIN a := -3; END.") == {'a': -3.0}

        with pytest.raises(ParserException):
            interp4 = Interpreter()
            assert interp4.eval("BEGGIN END.") == {}

        with pytest.raises(LexerException):
            interp5 = Interpreter()
            assert interp5.eval("BEGIN :: END.") == {}

