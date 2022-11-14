class SpecialHashMap : HashMap<String, Int>() {

    val iloc: ArrayList<Int> = ArrayList()
    val ploc = Ploc(this)


    override fun put(key: String, value: Int): Int? {
        super.put(key, value)

        val sortedKeys = keys.toSortedSet { a, b ->
            a.compareTo(b)
        }

        iloc.clear()
        for (k in sortedKeys)
            iloc.add(this[k]!!.toInt())


        return super.put(key, value)

    }
}


fun main() {

    println("Iloc")

    val map1 = SpecialHashMap()
    map1["value1"] = 1
    map1["value2"] = 2
    map1["value3"] = 3
    map1["1"] = 10
    map1["2"] = 20
    map1["3"] = 30
    map1["1, 5"] = 100
    map1["5, 5"] = 200
    map1["10, 5"] = 300

    println(map1.iloc[0])  // >>> 10
    println(map1.iloc[2])  // >>> 300
    println(map1.iloc[5])  // >>> 200
    println(map1.iloc[8])  // >>> 3

    println("Ploc")

    val map = SpecialHashMap()
    map["value1"] = 1
    map["value2"] = 2
    map["value3"] = 3
    map["1"] = 10
    map["2"] = 20
    map["3"] = 30
    map["(1, 5)"] = 100
    map["(5, 5)"] = 200
    map["(10, 5)"] = 300
    map["(1, 5, 3)"] = 400
    map["(5, 5, 4)"] = 500
    map["(10, 5, 5)"] = 600

    println(map.ploc[">=1"]) // >>> {1=10, 2=20, 3=30}
    println(map.ploc["<3"]) // >>> {1=10, 2=20}

    println(map.ploc[">0, >0"]) // >>> {(1, 5)=100, (5, 5)=200, (10, 5)=300}
    println(map.ploc[">=10, >0"]) // >>> {(10, 5)=300}

    println(map.ploc["<5, >=5, >=3"]) // >>> {(1, 5, 3)=400}
}