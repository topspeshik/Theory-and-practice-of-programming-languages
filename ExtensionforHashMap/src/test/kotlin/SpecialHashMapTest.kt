import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test
import kotlin.test.assertFailsWith

internal class SpecialHashMapTest{
    @Test
    fun testIloc() {
        val specialHashMapTest = SpecialHashMap()
        specialHashMapTest["value1"] = 1
        specialHashMapTest["value2"] = 2
        specialHashMapTest["value3"] = 3
        specialHashMapTest["1"] = 10
        specialHashMapTest["2"] = 20
        specialHashMapTest["3"] = 30
        specialHashMapTest["1, 5"] = 100
        specialHashMapTest["5, 5"] = 200
        specialHashMapTest["10, 5"] = 300

        assertEquals(10,specialHashMapTest.iloc[0])
        assertEquals(300, specialHashMapTest.iloc[2])
        assertEquals(200, specialHashMapTest.iloc[5])
        assertEquals(3, specialHashMapTest.iloc[8])
    }

    @Test
    fun testPloc() {
        val specialHashMapTest = SpecialHashMap()
        specialHashMapTest["value1"] = 1
        specialHashMapTest["value2"] = 2
        specialHashMapTest["value3"] = 3
        specialHashMapTest["1"] = 10
        specialHashMapTest["2"] = 20
        specialHashMapTest["3"] = 30
        specialHashMapTest["(1, 5)"] = 100
        specialHashMapTest["(5, 5)"] = 200
        specialHashMapTest["(10, 5)"] = 300
        specialHashMapTest["(1, 5, 3)"] = 400
        specialHashMapTest["(5, 5, 4)"] = 500
        specialHashMapTest["(10, 5, 5)"] = 600

        assertEquals(mutableMapOf("1" to 10, "2" to 20, "3" to 30), specialHashMapTest.ploc[">=1"])
        assertEquals(mutableMapOf("1" to 10, "2" to 20), specialHashMapTest.ploc["<3"])
        assertEquals(mutableMapOf("(1, 5)" to 100, "(5, 5)" to 200, "(10, 5)" to 300), specialHashMapTest.ploc[">0, >0"])
        assertEquals(mutableMapOf("(10, 5)" to 300), specialHashMapTest.ploc[">=10, >0"])
        assertEquals(mutableMapOf("(1, 5, 3)" to 400), specialHashMapTest.ploc["<5, >=5, >=3"])

        assertEquals(mutableMapOf("1" to 10, "2" to 20, "3" to 30), specialHashMapTest.ploc["<>20"])
        assertEquals(mutableMapOf("1" to 10, "2" to 20, "3" to 30), specialHashMapTest.ploc["<=30"])
        assertFailsWith<PlocException> { specialHashMapTest.ploc["dsdasda"] }


    }
}
