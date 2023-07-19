# Password Generator

This Python program generates secure passwords with customizable options for the number of letters, symbols, and numbers included. The order of characters can be randomized to enhance password security.

## Acknowledgment

This project draws inspiration from Angela Yu's [100 Days of Python](https://100daysofpython.dev/) bootcamp, which provides comprehensive Python programming training and offers a variety of educational resources, including projects, exercises, and tutorials.

## How to Use

1. Run the program using a Python interpreter.
2. You will be prompted to enter the desired parameters for your password:
   - `nr_letters`: The number of letters to include in the password.
   - `nr_symbols`: The number of symbols to include in the password.
   - `nr_numbers`: The number of numbers to include in the password.
3. After entering the parameters, the program will generate a password with the specified number of letters, symbols, and numbers.
4. The password will be displayed on the screen.

## Dependencies

This program does not rely on any external libraries or dependencies. It utilizes only the built-in `random` module in Python.

## Example

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
6
How many symbols would you like?
3
How many numbers would you like?
2
```

Output:
```
Generated Password: 1c!CaD#b@B@
```

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as needed.

While this password generator can provide random and varied passwords, it is always recommended to follow best security practices, such as using unique passwords for each account and regularly updating them.
