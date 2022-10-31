class Token(private val typeStr: String) {

   var type : TokenType = when (typeStr) {
        "MoO" -> TokenType.MoO
        "MOo" -> TokenType.MOo
        "moO" -> TokenType.moO
       "Moo"-> TokenType.Moo
       "OOO" ->TokenType.OOO
       "moo" ->TokenType.moo
       "MOO"->TokenType.MOO
       "OOM" -> TokenType.OOM
       "oom" -> TokenType.oom
       "mOo" -> TokenType.mOo
       "MMM" -> TokenType.MMM
       else -> TokenType.EOL
    }

    override fun toString(): String {
        return "Token $type"
    }
}
