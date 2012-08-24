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

# 2,3,5,7
count <- 4
n <- 9
while (count!=10001) {
  if (IsPrime(n)) count <- count+1
  n <- n+2
}
n-2
