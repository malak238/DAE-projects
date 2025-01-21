using System;
using System.Collections.Generic;

class Program
{
    // Private variable
    private static string privateVariable = "I am private!";
    
    // Public variable
    public static int publicVariable = 10;
    
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
         
         
         // 4. Create a Function (Custom function)
        int sumResult = AddNumbers(10, 20);  // Calling the custom function
        Console.WriteLine($"\nThe sum of 10 and 20 is: {sumResult}");