class IlocException: Exception()

class Iloc(private val specialHashMap: SpecialHashMap)  {

    operator fun get(condition: Int): Int {
        val sortedKeys = specialHashMap.keys.toSortedSet { a, b ->
            a.compareTo(b)
        }

        var c = 0
        for (k in sortedKeys){
            if (c == condition)
                return specialHashMap[k]!!.toInt()
            c+=1
        }
        throw IlocException()

    }
}