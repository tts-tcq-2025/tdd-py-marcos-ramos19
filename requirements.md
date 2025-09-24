# TDD Driven StringCalculator

## Table of Contents

- [TDD Driven StringCalculator](#tdd-driven-stringcalculator)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements Specification](#requirements-specification)
    - [Functional Requirements](#functional-requirements)
    - [Non-Functional Requirements](#non-functional-requirements)
  - [Test Specification](#test-specification)
    - [Testing Strategy](#testing-strategy)
    - [Test Cases](#test-cases)
  - [Conclusion](#conclusion)

## Introduction

This project implements a StringCalculator that can sum up to two numbers separated by commas. It will be developed using a Test-Driven Development (TDD) approach.

## Requirements Specification

### Functional Requirements

1. **Sum of Numbers**

   - The `Add` function should accept an empty string and return 0.
   - The `Add` function should accept a single number and return its value.
   - The `Add` function should accept two numbers separated by commas and return their sum.
   - The `Add` function should handle an unknown amount of numbers, allowing both commas and new lines as separators.
   - The `Add` function should allow custom delimiters specified in the input.

2. **Error Handling**
   - The `Add` function should throw an exception if a negative number is passed, displaying all negatives in the error message.
   - Numbers greater than 1000 should be ignored in the sum.

### Non-Functional Requirements

1. **Cyclomatic Complexity**

   - The maximum cyclomatic complexity (CCN) per function should be 3.

2. **Test Coverage**
   - 100% line and branch coverage should be ensured at every step of development.

## Test Specification

### Testing Strategy

The testing strategy will be based on the TDD approach, starting with writing failing tests and then implementing the minimum code necessary to make the tests pass. Testing tools such as [name of testing tool] will be used to automate the process.

### Test Cases

| ID    | Description                         | Expected Result                       | Status  |
| ----- | ----------------------------------- | ------------------------------------- | ------- |
| TC-01 | Empty input                         | 0                                     | Pending |
| TC-02 | Input with a single number          | 1 (for input "1")                     | Pending |
| TC-03 | Input with two numbers              | 3 (for input "1,2")                   | Pending |
| TC-04 | Handling multiple numbers           | 6 (for input "1\n2,3")                | Pending |
| TC-05 | Handling custom delimiters          | 3 (for input "//;\n1;2")              | Pending |
| TC-06 | Handling negative numbers           | Exception "negatives not allowed: -1" | Pending |
| TC-07 | Ignoring numbers greater than 1000  | 2 (for input "2,1001")                | Pending |
| TC-08 | Handling variable length delimiters | 6 (for input "//[]\n12\*\*\*3")       | Pending |

## Conclusion

This document will serve as a guide for the development and testing of the TDD Driven StringCalculator project. It will be updated as changes are made to the requirements or testing strategy.
