
## What is a shell?

A shell is a command line interface (CLI) program that provides a user-friendly way to interact with an operating system (OS) or a computer system. It serves as a bridge between the user and the kernel (core of OS) by interpreting and executing commands entered by the user or scripts

## Different types of shells

### Bash

Bourne-Again Shell (bash) is one of the most widely used shells and is the default shell on manu linux distributions. It is a poweful and versatile shell that supports scripting, interactive use, and command-line automation.

### Zsh

Z Shell (Zsh) is known for its extensive customization options and interactive features. It offers advanced auto-completion, syntax highlighting, and theming. Many users prefer Zsh for its user-friendly experience

There’s many options of shell…

## Comments

To write comments in shell, use these syntax below

```bash
#!/bin/bash

echo "Before comments"

#Single line comment

<<comment
This
is
a
multi
line
comments

comment

echo "After comments"
```

## Variables

Setting variables in shell scripting

```bash
#!/bin/bash

#Script to show how to use variables

a=10 #do not use space in between

name="Joao"
age=26

echo "My name is $name and I'm $age years old"

name="Joao Victor" #variables are reassignable

echo "trying to scape characters: \"${name}\""

echo "my PC hostname is $(hostname)" #use the $() to get environment variables

echo "The current directory is $(pwd)"
```

## Arrays

The example below shows how to create and manipulating arrays in shell scripting

```bash
#!/bin/bash

#Creating an array...

fruits=("Banana" "Orange" "Apple")

echo "The first fruit is ${fruits[0]}" #use the ${} pattern to interpolation of items in an array
echo "The second fruit is ${fruits[1]}"
echo "The last one is \"${fruits[2]}\"" #using scape to set double quotes in the last item of the array

#arrays could have different types of items

items=("Hello" 2 true)
echo "The last value is ${items[2]}"

#getting length of arrays
echo "There are ${#fruits[*]} fruits in the array"

#trying to add new item in the array
fruits+=("Strawberry")

echo "printing all array: ${fruits[*]}"
```

## User input

Check how to read user input inside of a shell scripting

```bash
#!/bin/bash

#Taking user input

echo "Please, type your name: "
read name
echo "Your name is $name"

# Another way to take user input...
read -p "What is your name? " anothername
echo "Your name is $anothername"
```

## Arithmetic Operation

All the examples below show how to make arithmetic operations in shell scripting

```bash
#!/bin/bash

number1=10
number2=2

mul=$number1*$number2 #here we need to define a variable with the keyword let

echo The result is $mul #if we don't use the keyword "let" when we define the mul variable, the output here will be "10*2"

x=3
y=6

let result=$x*$y
echo "Result of multiplication: $result" #here the result will be 18 because we're using the keyword to define the result variable

#making the operation directly on the output command...
echo "The subtraction of $x and $y is $(($x-$y))" #use $(()) directive to make arithmetic operation directly
```

## Conditionals

Here we can get a table of conditionals when we writing code in shell scripting

| **Operator** | **Description** |
| --- | --- |
| -eq | Checks if two values are equal |
| -nt | Checks if two values are not equal |
| -lt | Checks if the value on the left is less than the value on the right |
| -le | Checks if the value on the left is less than or equal to the value on the right |
| -gt | Checks if the value on the left is greater than the value on the right |
| -ge | Checks if the value on the left is greater than or equal to the value on the right |

## If-Else conditional statement

```bash
#!/bin/bash

#let's see how does the if-else conditional statement work

#the code below verify if the user is major of age

read -p "Type your age: " myage

let defaultMajorAge=18

if [[ $myage -ge $defaultMajorAge ]]; then
        echo "You are major"
else
    	echo "You aren't major of age yet"
fi

#now let's get what is the correct stage of life from a person
# 0 - 12 # child
# 13 - 17 # teenager
# 18 - 29 # young adult
# 30 - 59 # adult
# > 59 # old

read -p "What is your age? " age
echo "Checking your stage of life..."
if [[ $age -ge 0 && $age -le 12 ]]; then
        echo "You are a child"
elif [[ $age -ge 13 && $age -lt 18 ]]; then
        echo "You are a teenager"
elif [[ $age -ge 18 && $age -lt 30 ]]; then
        echo "You are a young adult"
elif [[ $age -ge 30 && $age -lt 60 ]]; then
        echo "You are an adult"
else
    	echo "You are old"
fi
```

## Choice

Now let’s to learn how to use the choice syntax with the example below

```bash
#!/bin/bash

#let's write a program that reads an choice for a menu restaurant

echo "Provide an option to order in our restaurant: "
echo The options are: &&
echo 1. Pizza &&
echo 2. Hamburguer &&
echo 3. Milkshake &&
echo 4. Ice Cream

read choice

case $choice in
        1) echo "You've ordered pizza!! Nice choice";;
        2) echo "You've ordered hamburguer!! It's very taste";;
        3) echo "You've ordered Milkshake!! Excellent choice also";;
        4) echo "You've ordered Ice Cream!! Good";;
        *) echo "Please, set an valid option from menu. Type 1, 2, 3 or 4";;
esac
```

## Ternary Operator

Ternary operator is a short way to write a conditional statement.

The example will cover a script that reads a person age through the shell and returns if the person is Adult or Minor. The condition is: if the person has less than 18 years old, is minor. Otherwise, is adult

```bash
#!/bin/bash

read -p "Enter your age: " age
[[ $age -ge 18 ]] && echo "Adult" || echo "Minor"
```

## For loop

The for loop is a repetition statement to iterate over many of items like an array.

The program below iterate from 1 to 5 and makes an arithmetical operation to multiply by 2 the current number.

1 * 2

2* 2

3 * 2

until the number five

```bash
#!/bin/bash

# Iterating from 1 to 5...
for i in {1..5}; do
    let mult=2*$i
    echo "Value: $mult"
done
```

Now let’s iterate over an array of names

```bash
#!/bin/bash

# Iterating over an array of names

names=("Joao" "Pedro" "Maria")
lengthOfNames=${#names[*]}

for (( i=0;i<$lengthOfNames;i++ ));do
    echo "Current name: ${names[$i]}"
done
```