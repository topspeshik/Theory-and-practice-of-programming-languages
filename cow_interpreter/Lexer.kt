class Lexer {
    private var pos = arrayOf(0, 3)
    private var text: String = ""
    private var currentStr: String = ""

    fun initLexer(text_: String) {
        text = text_
        currentStr = text.slice(pos[0] until pos[1])
    }

    fun currentTok(): Token = Token(currentStr)

    fun next(): Token {
        while (currentStr != "") {
            if (" " in currentStr) {
                throw Exception("Bad string, a lot of spaces")
            } else {
                forward()
                return Token(currentStr)
            }
        }
        return Token("EOL")

    }

    fun back(): Token {
        while (currentStr != "") {
            if (" " in currentStr) {
                throw Exception("Bad string, a lot of spaces")
            } else {
                goBack()
                return Token(currentStr)
            }
        }
        return Token("EOL")

    }

    private fun forward() {

        pos[0] = (pos[1] + 1).also { pos[1] = pos[1] + 4 }

        if (pos[1] > text.length)
            currentStr = ""
        else
            currentStr = text.slice(pos[0] until pos[1])
    }

    private fun goBack() {
        pos[1] = (pos[0] - 1).also { pos[0] = pos[0] - 4 }

        if (pos[0] > text.length)
            currentStr = ""
        else
            currentStr = text.slice(pos[0] until pos[1])
    }

}