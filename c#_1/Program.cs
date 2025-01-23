using System;
using System.Collections.Generic;

class Program
{
    // Private variable
    private static string privateVariable = "I am private!";
    
    // Public variable
    public static int publicVariable = 10;
    
    // Public list accessible throughout the class
    public List<int> numbers;

    // Private list that can only be accessed by this class
    private List<int> evenNumbers;

    // Constructor to initialize the lists
    public Program()
    {
        numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        evenNumbers = new List<int>();
    }

    // Public method to call and print even numbers
    public void DisplayEvenNumbers()
    {
        evenNumbers.Clear(); // Clear the list before adding updated even numbers
        FindEvenNumbers();
        PrintEvenNumbers();
    }

    // Private function that finds even numbers from the 'numbers' list
    private void FindEvenNumbers()
    {
        foreach (int number in numbers)
        {
            if (number % 2 == 0)
            {
                evenNumbers.Add(number);
            }
        }
    }

    // Private function to print out the even numbers
    private void PrintEvenNumbers()
    {
        Console.WriteLine("Even numbers from the list:");
        foreach (var even in evenNumbers)
        {
            Console.WriteLine(even);
        }
    }

    static void Main(string[] args)
    {
        // 1. Creating Variables With Data Types
        int age = 25; // integer variable
        string name = "John Doe"; // string variable
        bool isStudent = true; // boolean variable
        double height = 5.9; // double variable

        // Display the values of the variables
        Console.WriteLine($"Name: {name}");
        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"Height: {height}");
        Console.WriteLine($"Is student: {isStudent}");

        // 2. Conditional Statement (if statement)
        if (age >= 18)
        {
            Console.WriteLine($"{name} is an adult.");
        }
        else
        {
            Console.WriteLine($"{name} is not an adult.");
        }

        // 3. Demonstrating Loops (for loop)
        Console.WriteLine("\nCounting from 1 to 5 using a loop:");
        for (int i = 1; i <= 5; i++)
        {
            Console.WriteLine(i);
        }

        // Create an instance of the Program class
        Program program = new Program();

        // Calling the public method to display even numbers
        program.DisplayEvenNumbers();

        Console.ReadLine();
    }
}
