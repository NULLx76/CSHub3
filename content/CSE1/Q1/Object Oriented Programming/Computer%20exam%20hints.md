+++
title = "Computer exam hints"
date = 2019-01-21
+++
<h2>File handling</h2><p>Reading a file is actually really easy. You can either do this with a relative path (which gets the path from the root of your project, so if your file is in the .<em>/src/</em><span> folder, you have to address your file by .</span><em><span>/src/filename.txt) </span></em><span>or an absolute path (which states a path starting from your disk)</span><em><span>.</span></em></p><br><p>Then, once you have your file path, you can make an instance of the <em>File </em><span>class, which you can pass into the </span><em><span>Scanner.</span></em><span> An example reading a file (make sure to import the </span><em><span>Scanner </span></em><span>and </span><em><span>File </span></em><span>classes, </span><em><span>Eclipse </span></em><span>will give you a hint if you don' t):</span></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-java">// This reads a file pointed to by its parameter, and returns the parsed object
// Make sure to actually edit this code according to what you want, returing something of the class 'Object' is probably a bad idea as you lose type information
public Object getFileContents(String filePath) {
    try {
      File file = new File(filePath);
      Scanner fileScanner = new Scanner(file);
      
      while(fileScanner.hasNextLine()) {
          String currentLine = fileScanner.nextLine();
          .... // Do something with the current line, for example create the object you need from the file
      }
  
      return yourObject; // This object will be what you actually created while reading the file
    } catch (IOException e) {
        e.printStackTrace(); // Catch the error if the file doesn't exist
        return null; // You must return something, or it won't compile
    }

}
</pre>
</div><br><p>Writing to files is also important. This can be done using a FileWriter:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-java">// This writes to a file given pointed to by its parameter, and sets the content which was also passed along
public void getFileContents(String filePath, String contents) {
    
    // Make sure to wrap it in a try-catch block
    try {
        File file = new File(filePath);
        FileWriter fileWriter = new FileWriter(file);
        fileWriter.write(contents); // Write to file
        fileWriter.close(); // Close the write
    } catch (IOException e) {
        e.printStackTrace(); // Catch the error if the file doesn't exist
    }
}
</pre>
</div><br><h2>Reading user input</h2><p>You will probably be asked to let a user input some data, most of the time in the form of strings of integers. It would be a pain to copy sort of the same code each time you have to ask input, and verifying whether that input is actually correct is even more of a hassle. </p><br><p>One way to do this is to create a wrapper class. I won't give the full code here as everybody will implement it differently, but in this wrapper class you create a few methods which return an integer or a string for example. Then the user creates an instance of that wrapper class for each question they want to ask the user, and call one of the methods (perhaps with some checking parameters, max number for example) and they get their inputted value returned. </p><br><p>Now what if the user types in the wrong thing? Just recursively call the method from within the method, and it will keep asking the same question until the user has finally given the correct input (a while loop is also possible, it just depends on what you actually prefer). </p><br><p>In order to actually read the user's input, you need a scanner object. You should use the same <em>Scanner</em><span> with the </span><em><span>System.in </span></em><span>input throughout the whole application (read why down below). Here a code example giving a few hints on how you might implement it:</span></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-java">public class ScannerWrapper {

    private String userQuestion;
    private Scanner inputScanner;

    // Create the constructor with the question and scanner

    // Perhaps create an overloaded method for if you don't want to actually have a maxValue

    // Return the int the user has input into the terminal
    public int getIntFromInput(int maxValue) {
        
        if (inputScanner.hasNextInt()) {
            int inputInt = inputScanner.nextInt();
            inputScanner.nextLine(); // As the scanner only reads 1 int and not the next line symbol, this has to be done to push the scanner to the correct line
            // Test if the input has the correct value, else call itself again (see below)
            return inputInt;
        } else {
            inputScanner.nextLine(); // If no int was input, it can read the nextline and call itself again, as then it must have been a string or some other input, which is unpreferable now
            return getIntFromInput(maxValue); // Call itself, make sure to actually use return, else nothing will be returned and the program (probably) won't compile
        }
    }

    // Create more methods for strings etc
}
</pre>
</div><br><p>A few things to denote from this example:</p><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>If you use <em>nextInt(), </em><span>you won't skip to the end of the line automatically, so make sure to call </span><em><span>nextLine() </span></em><span>as well, if the int is the only user input you want</span></li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>If you use recursion, don't forget to put the <strong>return </strong><span>statement in front of the to be called method, otherwise it won't do anything</span></li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>The <em>hasNext.. </em><span>and </span><em><span>next... </span></em><span>methods are </span><strong><span>blocking</span></strong><span>, meaning that if you use a single threaded program, the program won't do anything besides waiting for input from the end user.</span></li><li data-list="bullet"><span class="ql-ui" contenteditable="false"></span>Use one instance of the scanner with System.in, see <a href="https://stackoverflow.com/questions/29053580/cannot-use-multiple-scanner-objects-in-java/29053677" target="_blank">this</a><span> link for more explanation.</span></li><br><p>If you want to create a more advanced input scanning function, you can extend this wrapper class and use the input reading functionality to for example return an object of a set (if you ask the user to input 1, 2, 3 or 4, and that will be the item that is returned). For that you could use generics, but that might be for a later stage in your programming life...</p><h2></h2><h2>Converting lists and arrays</h2><p>You might have one of the following which you want to convert between <strong>int[]</strong><span>, </span><strong><span>Integer[]</span></strong><span> and </span><strong><span>List&lt;Integer&gt;. </span></strong><span>Here are some pieces of code which can accomplish that, mind you that these are individual pieces of code and might not work together.:</span></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-java">// integerArray (Integer[]) to the other types
List&lt;Integer&gt; integerList = Arrays.asList(integerArray);

int[] intArray = Arrays.stream(integerArray).mapToInt(x -&gt; x).toArray(); // or mapToInt(Integer::intValue)

// integerList (List&lt;Integer&gt;) to the other types
int[] intArray = integerList.stream().mapToInt(x -&gt; x).toArray();

Integer[] integerArray = new Integer[integerList.size()];
integerList.toArray(integerArray);

// intArray (int[]) to the other types
Integer[] integerArray = Arrays.stream(intArray).boxed().toArray(Integer[]::new);

List&lt;Integer&gt; integerList = Arrays.stream(intArray).boxed().collect(Collectors.toList());
</pre>
</div><br><h2>Threads</h2><p>To create a multi threaded program, you should have something representing a Thread class, like this:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-java">public class ThreadExample extends Thread {

	private MyObject myObject;
	
	public Shuffle(Object myObject) {
		super();
		
		this.myObject= myObject; // Initialize myObject
	}
	
	@Override
	public void run() { // This method has to be there, it actually executes what the thread should do
		myObject.doSomething(); // This calls a synchronized method, which means only one thread can access this at a single moment
	}
	
}

// This does the same, but it is another (generally preferred) way of handling things
public class AnotherThreadExample implements Runnable {

    private Thread thread;
	private MyObject myObject;

    public ExampleThread(Object myObject) {
        this.thread = new Thread(this); // You pass "this" to the Thread, which is the current class. You register the current class as a thread. As this class contains the run() method (as specified by the Runnable interface), Java knows what to do with it.
        this.myObject= myObject; // Initialize myObject
    }

	@Override
    public void run() {
        myObject.doSomething();
    }
}

public class MyObject {

    public synchronized void doSomething() {
        // Do something, this can only be accessed by one thread at a time
    }
}
</pre>
</div><br><h2>Project structure</h2><p>When to create new classes and methods? Well, this depends on who you are asking this, but I'll give my personal preference. </p><br><p>First off, you shouldn't create classes, just to create classes. If you have to create a whole class for one method, just creating one method is (probably) better, certainly in the smaller programs you will build in the computer exam. Then, when do you create a new method? Pretty often actually, it is best to have little to no duplicated code in your application, so you would create reusable methods in your application. Also, the longer the method, the harder it will be to test.</p><br><p>For data types, for example a <strong>Song</strong><span>, which contains certain characteristics, it is probably easiest to create a </span><strong><span>Song </span></strong><span>class with its properties. Then you can create instances of this song and get its data accordingly. If you combine multiple songs in to an album, create an </span><strong><span>Album </span></strong><span>class, which contains an ArrayList of songs. </span></p><br><p>This are just a few examples of things that you might do, there are many possibilities here.</p><br><h2>Pair class</h2><p>You might want to create an ArrayList containing multiple objects per row, for example a string and an integer. The easiest way to create this is using a pair class. This can be created in multiple ways, first you could create a generic pair class like this:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-java">public class Pair&lt;L, R&gt; {

    private L leftElement;
    private R rightElement;
  
    public Pair(L leftElement, R rightElement) {
        this.leftElement = leftElement;
        this.rightElement = rightElement;
    }

    public L getLeft() {
        return leftElement;
    }

    public R getRight() {
        return rightElement;
    }

}

// Somewhere else in your code
ArrayList&lt;Pair&lt;String, Integer&gt;&gt; list = new ArrayList&lt;&gt;();
list.add(new Pair("Hi", 42));

System.out.println(list.get(0).getLeft()); // Prints "Hi"
</pre>
</div><br><p>Now what happens here? You created a generic class where there are 2 elements, a left and a right element (the naming doesn't really matter, it is just easy to remember). Now when you create an instance of this class, you specify what the types of the elements must be using generics, so you are sure you get elements of the right types back. </p><br><p>This can be considered bad practice, as reading this file later on might get you confused. Therefore it is most of the time a better idea to create a class without the generics, but just the direct types in there. This makes it a lot clearer to read later on.</p><br><h2>Strings</h2><p>Some things that might be nice to know about strings in Java (maybe not necessarily for this exam but certainly for later), is that strings are immutable. This means that you don't edit the values at the string's memory address, but you use a new memory address to save your string. So if you do a loop in which you change your string 50 times, you create new memory addresses for this string 50 times. Garbage collection will clean this up, but it is nicer to implement is correctly in the first place. This can be done through very handy classes Java gives you, for example the <strong>StringBuilder </strong><span>and </span><strong><span>StringJoiner </span></strong><span>classes.</span></p><br><p>You can create an instance of the <strong>StringBuilder </strong><span>class, and you can use its </span><em><span>append </span></em><span>method to add new strings to this object. Then in the end, you can use </span><em><span>yourStringBuilder.toString() </span></em><span>to convert it so string.</span></p><br><p>The <strong>StringJoiner </strong><span>class joins strings, unsurprisingly. You notate a divider (which can be a new line, space, whatever), and each time you add a string to this object, this divider is used. Again, you can use </span><em><span>toString()</span></em><span> to convert back to a string.</span></p><br><p>There are many more methods on these classes, for that you can read the JavaDoc. The <strong>StringBuilder </strong><span>is especially useful when doing loops.</span></p><br><h2>Unit tests</h2><p>Here will be an example file on how to create a unit test using <strong>jUnit 4. </strong><span>jUnit 5 works differently, but just make sure you run your test with the right jUnit version!</span></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-java">import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class ExampleTest {

  @Test
  public void myOwnTest() {
    // Initialize stuff
    assertEquals(6, 6); // Now my test works, but you should use real data of course
  }
}
</pre>
</div><p>As you will probably make multiple test classes, it might be useful to create another class with static fields that can be used in all test classes. This way you don't have to initialize everything with each test and you can use the same test data multiple times.</p><br><p>Here a list of asserts you can use in jUnit 4:</p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-java">assertArrayEquals("message you can (but don't have to) use per assert", expectedArray, actualArray);
assertEquals(expectedString, actualString); // You get the drill, fill in the expected and actual values from now on
assertFalse(); 
assertNotNull();
assertNotSame();
assertNull();
assertSame();
assertThat();
</pre>
</div><br><h2>Inheritance</h2><p>I won't explain inheritance here, as you can do that on your own (for the computer exam you probably don't need any complex constructs and a lot of knowledge on polymorphism et cetera though. Something I would like to add to your inheritance vocabulary is the <strong><em>@Override </em></strong><span>annotation. Annotations are hints for compilers or plugins to show you want some functionality in there, or just for waterproofing your application (in Java, there are other things in other languages, in TypeScript for example you have decorators, which adds a lot of  functionality). This annotation though tells the Java compiler that you are overriding a method of a super class. </span></p><br><p>Now why would this be useful? Imagine you override the <em>toString() </em><span>method of the </span><strong><span>Object </span></strong><span>class, so instead of </span><em><span>&lt;TestClass(3, 0)&gt; </span></em><span>you get </span><em><span>TestObject: 3 &amp; 0. </span></em><span>What if you mistype your </span><em><span>toString()?</span></em><span> Then it will just use the default </span><em><span>toString() </span></em><span>of the </span><strong><span>Object </span></strong><span>class when calling this method, which yields the incorrect result. It won't give any type of error, as you can create a </span><em><span>toSring() </span></em><span>method (notice the missing </span><em><span>t</span></em><span>?), and that is perfectly fine. But this behaviour you don't want, so that's where the </span><strong><em><span>@Override </span></em></strong><span>annotation comes in. If the method where you use it incorrectly overrides a parent method, the compiler will give you an error. Here's an example:</span></p><div style="white-space: normal;" class="markdown-body"><pre data-lang="text/x-java">// The method name is spelled wrong, so this will give you a compiler error
@Override
public String toSring() {
    return "";
}
</pre>
</div><br><p>This is a huge help to fix typos in your program, through which something might inexplicably not work anymore.</p>