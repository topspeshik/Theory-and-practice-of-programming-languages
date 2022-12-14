

class PlocException: Exception()

class Ploc(private val specialHashMap: SpecialHashMap) {

    operator fun get(condition: String): Map<String, Int?> {
        val del = delimetr(condition)
        val newCon = condition.replace(" ", "").split(del)
        val result: MutableMap<String, Int?> = mutableMapOf()
        for (key in specialHashMap.keys) {
            var count = 0
            val newKey = keyParser(key)
            if (newKey.size > 0) {
                if (newCon.size == newKey.size) {
                    for (i in newCon.indices) {
                        if (checkCon(conParser(newCon[i]), newKey[i]))
                            count += 1

                    }
                }
                if (count == newCon.size)
                    result[key] = specialHashMap[key]
            }

        }

        return result
    }

    private fun delimetr(condition: String) : Char{
        val newCon = condition.replace(" ", "")
        val operators : CharArray = charArrayOf('=','>','<')
        for (i in 1 .. newCon.length-2){
            if (isNumeric(newCon[i-1].toString()) && newCon[i+1] in operators)
                if (!isNumeric(newCon[i].toString()) && newCon[i] !in operators)
                    return newCon[i]
                else throw PlocException()
        }
        return ' '
    }

    private fun keyParser(key: String): ArrayList<String> {
        val newKeys: ArrayList<String> = ArrayList()
        val tKeys = key
            .replace(" ", "")
            .replace("(", "")
            .replace(")", "")
            .split(',')
        return if (tKeys.size == 1 && isNumeric(tKeys[0])) {
            newKeys.add(tKeys[0])
            newKeys
        } else {
            for (k in tKeys) {
                if (isNumeric(k))
                    newKeys.add(k)
            }
            newKeys
        }
    }

    private fun conParser(con: String): ArrayList<String> {
        val newCon: ArrayList<String> = ArrayList()
        if (con.contains("<>")) {
            newCon.add("<>")
            newCon.add(con.split("<>")[1])

        } else if (con.contains(">=")) {
            newCon.add(">=")
            newCon.add(con.split(">=")[1])

        } else if (con.contains(">")) {
            newCon.add(">")
            newCon.add(con.split(">")[1])

        } else if (con.contains("<=")) {
            newCon.add("<=")
            newCon.add(con.split("<=")[1])

        } else if (con.contains("<")) {
            newCon.add("<")
            newCon.add(con.split("<")[1])

        }  else{
            throw PlocException()
        }
        return newCon
    }

    private fun checkCon(con: ArrayList<String>, dig: String): Boolean {
        if (isNumeric(con[1])){
            return when (con[0]) {
                ">=" -> dig.toFloat() >= con[1].toFloat()
                ">" -> dig.toFloat() > con[1].toFloat()
                "<" -> dig.toFloat() < con[1].toFloat()
                "<=" -> dig.toFloat() <= con[1].toFloat()
                "<>" -> dig.toFloat() != con[1].toFloat()
                else -> return false
            }
        } else throw PlocException()

    }

    private fun isNumeric(toCheck: String): Boolean {
        val regex = "-?[0-9]+(\\.[0-9]+)?".toRegex()
        return toCheck.matches(regex)
    }

}