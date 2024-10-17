# Fractional BODMAS

Combine the ten digits, 0-9, into five valid fractions. Using each of the four operations once, and no brackets, what's the largest number you can make?

I took some shortcuts: 

* You always want to subtract 0
* Division is the same as multiplication
* So you can create four fractions (and discard the remaining number as the denominator of 0), then either:
  * Multiply three of them and add the fourth; or
  * Multiply two pairs of them and add the result.
 
`python fractions.py` solves the no-brackets version.

`python rpn.py` solves the version where brackets are allowed.
