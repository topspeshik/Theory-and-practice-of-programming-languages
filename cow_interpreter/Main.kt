import java.io.File

//Это вроде чуть чуть работает, kotlin я решил выбрать не потому что я его хорошо знаю, а наоборот, чтобы подтянуть)

fun main(args: Array<String>) {

    //Вывод Hello, World! Через цикл moo MOO
    var file = File("helloCycle.cow")
    var lines = file.readLines()
    var f = lines.joinToString(" ").replace("  "," ")


    var inter = Interpreter()
    inter.eval(f)

    println()
    //Вывод Hello, World! без цикла
    file = File("hello.cow")
    lines = file.readLines()
    f = lines.joinToString(" ").replace("  "," ")


    var inter1 = Interpreter()
    inter1.eval(f)


}