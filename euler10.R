IsPrime <- function(n){
  flag <- TRUE
  t <- floor(sqrt(n))
  i <- 3
  while (n%%i !=0 && i<=t){
    i <- i+2
  }
  if (i<=t) flag <- FALSE 
  return(flag)
}

result <- 2+3+5+7
n <- 9
while (n<2000000){
  if (IsPrime(n)) result <- result+n
  n <- n+2
}
result

# quite slow
