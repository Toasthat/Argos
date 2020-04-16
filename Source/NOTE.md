## Hexagonal architecture example
```
class Program
{
    static void Main(string[] args)
    {
        // 1. Instantiate right-side adapter ("go outside the hexagon")
        IObtainPoems fileAdapter = new PoetryLibraryFileAdapter(@".\Peoms.txt");

        // 2. Instantiate the hexagon
        IRequestVerses poetryReader = new PoetryReader(fileAdapter);

        // 3. Instantiate the left-side adapter ("I want ask/to go inside")
        var consoleAdapter = new ConsoleAdapter(poetryReader);

        System.Console.WriteLine("Here is some...");
        consoleAdapter.Ask();

        System.Console.WriteLine("Type enter to exit...");
        System.Console.ReadLine();
    }
}

```

The instantiation order is typically from right to left:

1. First we instantiate the Infrastructure side, here the fileAdapter which will read the file.
    
2. We instantiate the Domain class that will be driven by the application, the poetryReader in which we inject the fileAdapter by injection into the constructor.

3. Install the Application side, the consoleAdapter that will drive the poetryReader and write to the console. Here the poetryReader is injected into the consoleAdapter by injection into the constructor.


In practice, the PoetryReader does not depend on PoetryLibraryFileAdapter but on IObtainPoems, which is well defined in the Domain. You can check it by looking at the signature of its constructor.

```
public PoetryReader(IObtainPoems poetryLibrary)
{
    this.poetryLibrary = poetryLibrary;
}
```
