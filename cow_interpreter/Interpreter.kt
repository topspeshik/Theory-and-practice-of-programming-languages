class Interpreter {
    private lateinit var currentToken: Token
    private var lexer = Lexer()


    fun eval(s: String) {
        lexer.initLexer(s)
        currentToken = lexer.currentTok()
        var result = mutableMapOf<Int, Int>()
        var index = 0
        var mooC = 0
        while (currentToken.type != TokenType.EOL) {
            when (currentToken.type) {

                TokenType.moO -> index += 1

                TokenType.mOo -> index -= 1

                TokenType.MoO -> {
                    if (result[index] == null)
                        result[index] = 1
                    else
                        result[index] = result[index]!! + 1
                }

                TokenType.MOo -> {
                    if (result[index] == null)
                        result[index] = -1
                    else
                        result[index] = result[index]!! - 1
                }

                TokenType.Moo -> {
                    if (result[index] == 0)
                        result[index] = readLine()!!.toInt()
                    else
                        print(result[index]?.toChar())
                }

                TokenType.OOO -> result[index] = 0

                TokenType.MOO -> {

                    if (result[index] == 0 || result[index] == null) {

                        currentToken = lexer.next()
                        currentToken = lexer.next()

                        while (currentToken.type != TokenType.moo) {
                            currentToken = lexer.next()
                        }
                    }
                }

                TokenType.moo -> {
                    if (result[index]!! != 0) {

                        currentToken = lexer.back()
                        currentToken = lexer.back()

                        while (currentToken.type != TokenType.MOO || mooC != 0) {
                            currentToken = lexer.back()

                            if (mooC > 0) {
                                if (currentToken.type == TokenType.MOO) {
                                    mooC -= 1
                                }
                            }
                        }

                    } else {
                        if (mooC == 0)
                            mooC += 2
                        else if (result[index] == 0 && index == 0)
                            mooC = 1
                        else
                            mooC += 1
                    }
                }

                TokenType.OOM -> print(result[index]?.toChar())

                TokenType.oom -> result[index] = readLine()!!.toInt()
                else -> {
                    println(currentToken.type)
                    println("Error")
                    break
                }
            }
            currentToken = lexer.next()

        }

    }

}