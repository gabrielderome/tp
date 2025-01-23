generate_data <- function(n) {
  # Generate n random values for x from N(12, 2)
  x <- rnorm(n, mean = 12, sd = 2)
  
  # Generate n random values for the error term e from N(0, 1)
  e <- rnorm(n, mean = 0, sd = 1)
  
  # Calculate y using the formula y = 18 + 0.75 * x + e
  y <- 18 + 0.75 * x + e
  
  # Return a data frame containing x and y
  data <- data.frame(x = x, y = y)
  return(data)
}
set.seed(123)
data <- generate_data(100)
# summerise data
summary(data)
# print number of rows in df
print(nrow(data))
# plot the distribution of x, y and e
par(mfrow=c(1,3))
hist(data$x, main="Distribution of x", xlab="x")
hist(data$y, main="Distribution of y", xlab="y")   
hist(data$y - 18 - 0.75 * data$x, main="Distribution of e", xlab="e")
# regress y on x
reg <- lm(y ~ x, data = data)
summary(reg)

