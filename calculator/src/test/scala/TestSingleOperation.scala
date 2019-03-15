package calculator.tests

import calculator.controller._
import calculator.model.Calculator
import org.scalatest._

class TestSingleOperation extends FunSuite {

  val EPSILON: Double = 0.000001

  def equalDoubles(d1: Double, d2: Double): Boolean = {
    (d1 - d2).abs < EPSILON
  }

  test("Sample testing of the calculator") {
    var calculator: Calculator = new Calculator()

    // Since we don't need event information f0r (edit to avoid keyword) this program, setting the event to null
    // to test is fine. This allows us to automate testing without using the GUI
    new NumberAction(calculator, 8).handle(null)
    new AdditionAction(calculator).handle(null)
    new NumberAction(calculator, 5).handle(null)

    new EqualAction(calculator).handle(null)

    var expected: Double = 13.0
    var actual: Double = calculator.displayNumber()
    assert(equalDoubles(actual, expected), actual)
    
    calculator = new Calculator()

    new NumberAction(calculator, 9).handle(null)
    new SubtractionAction(calculator).handle(null)
    new NumberAction(calculator, 3).handle(null)
    new EqualAction(calculator).handle(null)
    
    expected = 6.0
    actual = calculator.displayNumber()
    assert(equalDoubles(actual, expected), actual)  
    
    calculator = new Calculator()
    
    new NumberAction(calculator, 7).handle(null)
    new MultiplicationAction(calculator).handle(null)
    new NumberAction(calculator,3).handle(null)
    new EqualAction(calculator).handle(null)
    
    expected = 21.0
    actual = calculator.displayNumber()
    assert(equalDoubles(actual, expected), actual)
    
    calculator = new Calculator()
      
    new NumberAction(calculator, 8).handle(null)
    new DivisionAction(calculator).handle(null)
    new NumberAction(calculator, 3).handle(null)
    new EqualAction(calculator).handle(null)
      
    expected = 2.6666666666666665
    actual = calculator.displayNumber()
    assert(equalDoubles(actual, expected), actual)    
      
    
    
  }

}