IsPrime <- function(n){
  flag <- FALSE
  t <- floor(sqrt(n))
  for (i in 2:t){
    if (n%%i==0)  return(i) }
  flag <- TRUE
  return(flag)
}

n <- 600851475143

while (IsPrime(n)!=TRUE){
  n <- n/IsPrime(n)
}
n

      
