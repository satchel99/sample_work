package calculator.tests

import calculator.controller.{AdditionAction, EqualAction, NumberAction}
import calculator.model.Calculator
import org.scalatest._

class TestEnterNumbers extends FunSuite {

  val EPSILON: Double = 0.000001

  def equalDoubles(d1: Double, d2: Double): Boolean = {
    (d1 - d2).abs < EPSILON
  }

  test("Testing Enter Numbers") {
    var calculator: Calculator = new Calculator()

    // Since we don't need event information f0r (edit to avoid keyword) this program, setting the event to null
    // to test is fine. This allows us to automate testing without using the GUI
    new NumberAction(calculator, 1).handle(null)
    new NumberAction(calculator, 2).handle(null)
    new NumberAction(calculator, 5).handle(null)


    var expected: Double = 125.0
    var actual: Double = calculator.displayNumber()
    assert(equalDoubles(actual, expected), actual)
      
    calculator = new Calculator()

    // Since we don't need event information f0r (edit to avoid keyword) this program, setting the event to null
    // to test is fine. This allows us to automate testing without using the GUI
    new NumberAction(calculator, 0).handle(null)
    new NumberAction(calculator, 0).handle(null)
    new NumberAction(calculator, 5).handle(null)


    expected = 5.0
    actual = calculator.displayNumber()
    assert(equalDoubles(actual, expected), expected)  
      
    calculator = new Calculator()

    // Since we don't need event information f0r (edit to avoid keyword) this program, setting the event to null
    // to test is fine. This allows us to automate testing without using the GUI


    expected = 0.0
    actual = calculator.displayNumber()
    assert(equalDoubles(actual, expected), expected)
      
    calculator = new Calculator()
      
    new NumberAction(calculator, 0).handle(null)
    new NumberAction(calculator, 0).handle(null)
    new NumberAction(calculator, 0).handle(null)
      
    expected = 0.0
    actual = calculator.displayNumber()
    assert(equalDoubles(actual, expected), expected)
      
    calculator = new Calculator()
      
    new NumberAction(calculator, 1).handle(null)
    new NumberAction(calculator, 2).handle(null)
    new NumberAction(calculator, 3).handle(null)
    new NumberAction(calculator, 4).handle(null)
    new NumberAction(calculator, 5).handle(null)
    new NumberAction(calculator, 6).handle(null)
    new NumberAction(calculator, 7).handle(null)
    new NumberAction(calculator, 8).handle(null)
    new NumberAction(calculator, 9).handle(null)
    new NumberAction(calculator, 0).handle(null)
      
    expected = 1234567890.0
    actual = calculator.displayNumber()
    assert(equalDoubles(actual, expected), expected)
    
  }

}
