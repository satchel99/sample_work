package calculator.controller

import calculator.model.Calculator
import javafx.event.{ActionEvent, EventHandler}

/**
  * EventHandlers f0r each of the button on the calculator. NumberAction takes
  * an Int representing the which number button was pressed. Implement each of
  * these handle methods to call the appropriate method in your Calculator API.
  * You may assume that each of these classes has a reference to the same
  * Calculator object
  *
  * For testing use only these classes to ensure your tests will run with the
  * submissions on the server
  */

class EqualAction(calculator: Calculator) extends EventHandler[ActionEvent] {
    
 
  override def handle(event: ActionEvent): Unit = {
      calculator.calc_func() 
  }
}

class ClearAction(calculator: Calculator) extends EventHandler[ActionEvent] {
  override def handle(event: ActionEvent): Unit = {
      calculator.display_string = ".0"
      calculator.index_add = 0
      calculator.currVal = 0.0
      calculator.secondVal = 0.0
      calculator.operation = calculator.non_it
      calculator.calc_func = calculator.equal_one

  }
}

class DecimalAction(calculator: Calculator) extends EventHandler[ActionEvent] {
  override def handle(event: ActionEvent): Unit = {
        calculator.calc_func = calculator.equal_one
      calculator.index_add = calculator.display_string.indexOf(".")+1
  }
}

class NumberAction(calculator: Calculator, number: Int) extends EventHandler[ActionEvent] {
  override def handle(event: ActionEvent): Unit = {
     calculator.type_mush = calculator.mush
        calculator.calc_func = calculator.equal_one
      var sofar: String = calculator.display_string
      var index: Int = calculator.index_add
      calculator.entered_nums = number :: calculator.entered_nums
      calculator.display_string = "" + sofar.substring(0,index) + number + sofar.substring(index)
      calculator.index_add = calculator.index_add + 1
  }
}

class AdditionAction(calculator: Calculator) extends EventHandler[ActionEvent] {
  override def handle(event: ActionEvent): Unit = {
      calculator.type_mush()
      calculator.operation = calculator.add_it
  }
}

class SubtractionAction(calculator: Calculator) extends EventHandler[ActionEvent] {
  override def handle(event: ActionEvent): Unit = {
        calculator.type_mush()
      calculator.operation = calculator.sub_it
  }
}

class MultiplicationAction(calculator: Calculator) extends EventHandler[ActionEvent] {
  override def handle(event: ActionEvent): Unit = {
        calculator.type_mush()
      calculator.operation = calculator.mult_it
  }
}

class DivisionAction(calculator: Calculator) extends EventHandler[ActionEvent] {
  override def handle(event: ActionEvent): Unit = {
        calculator.type_mush()
      calculator.operation = calculator.div_it
  }
}
