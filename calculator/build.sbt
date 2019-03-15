javaHome := {
  var s = System.getenv("JAVA_HOME")
  if (s==null) {
    // tbd. try to detect JDK location on multiple platforms
    //
    // OS X: "/Library/Java/JavaVirtualMachines/jdk1.xxx.jdk/Contents/Home" with greatest id (i.e. "7.0_10")
    //
    s= "/Library/Java/JavaVirtualMachines/jdk1.7.0_10.jdk/Contents/Home"
  }
  //
  val dir = new File(s)
  if (!dir.exists) {
    throw new RuntimeException( "No JDK found - try setting 'JAVA_HOME'." )
  }
  //
  Some(dir)  // 'sbt' 'javaHome' value is ': Option[java.io.File]'
}
unmanagedJars in Compile += Attributed.blank(
  file(System.getenv("JAVA_HOME") + "/lib/javafx-mx.jar"))
fork in run := true
externalPom()