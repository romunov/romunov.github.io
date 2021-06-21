Title: Next generation testing?
Date: 2018-12-08
Category: Random
Status: draft
Tags: R, testing, package, development

Testing package functionality is always a hurdle, yet essential part of delivering predictable results to your users. An also important point of testing is keeping you at easy knowing that any change in code pertaining functionality will be caught by the tests if changes appear to break it.

From what I can gather, R is supported by `RUnit` and `testthat` packages which perform unit testing. What his means is that you create snippets of code which test different aspects of your code. These files are neatly located inside a separate folder, files structured in a (non) logical manner which are put to use at user's behest or when checking a package for inconsistencies.

But what if we had a new kind of testing framework which would not require us to write tests manually into separate location. What if we could just test code inline? Here's what I mean.

```
testing.x <- 1:5  # input predefined at the beginning of function or roxygen2 header?

myFunction <- function(input) {
  len <- length(input)
  sm <- sum(input)

  # Testing part
  inline_test(len > 0)  # length cannot be zero or less

  return(sm/len)
}
```

First I setup a testing string. This could be perhaps placed in roxygen2 header, perhaps it would have its own tag e.g. `#' @testInput` (?)
