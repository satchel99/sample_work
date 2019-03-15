package calculator.model


class Calculator() {
    
  var entered_nums : List[Int] = List()
  var display_string : String = ".0"
  var index_add : Int = 0
    var add_amt : Int = 1
    var currVal : Double = 0.0
    var secondVal : Double = 0.0
    var operation : (Double, Double) =>Double = non_it;
    var calc_func : () => Unit = equal_one
    var stay : Double = 0.0
    var type_mush : () => Unit = mush
  
  def displayNumber(): Double = {
    return display_string.toDouble
  }
    def add_it(a: Double, b: Double) : Double = {
        return a + b;
    }
    def sub_it(a: Double, b: Double) : Double = {
        return a - b;
    }
    def mult_it(a: Double, b: Double) : Double = {
        return a * b;
    }
    def div_it(a: Double, b: Double) : Double = {
        return a / b;
    }
    def non_it(a: Double, b: Double) : Double = {
        return display_string.toDouble;
    }
  def displayNumberHelper(index : Int): Double = {
    0.0
  }
 def equal_one() : Unit = {
      currVal = secondVal
      secondVal = displayNumber()
      println(currVal)
      println(secondVal)
      //calculator.currVal = calculator.operation(calculator.currVal, calculator.secondVal)
      display_string = "" + operation(currVal, secondVal)
      currVal = displayNumber()
        stay = secondVal
       println("stay is " + stay)
      calc_func = equal_two
        secondVal = displayNumber()
        currVal = 0
      type_mush = mush_two
       
  }
    def equal_two() : Unit = {
      println("function 2 now")
      display_string = "" + operation(displayNumber(), stay)
      currVal = displayNumber()
      secondVal = displayNumber()
  }
    
    def mush() : Unit = {
      println("mush")
      this.calc_func = this.equal_one
      println(this.secondVal)
      println(this.currVal)
      this.currVal = this.secondVal
      this.secondVal = this.displayNumber()
      this.secondVal = this.operation(this.currVal, this.secondVal)
      println(this.secondVal)
      println(this.currVal)
      this.display_string = ".0"
      this.index_add = 0
       this.type_mush = mush_two
    }
    
    def mush_two() : Unit = {
      println("mush2")
      this.calc_func = this.equal_one
      println(this.secondVal)
      println(this.currVal)
      this.display_string = ".0"
      this.index_add = 0
    }
}
