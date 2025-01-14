using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            // Ask the user for their name
            Console.WriteLine("Please enter your name:");
            string userName = Console.ReadLine();
            
            // Greet the user
            Console.WriteLine($"Hello, {userName}! Welcome to the world of C#.");
        }
    }
}
