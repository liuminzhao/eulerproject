IsPrime <- function(n){
  flag <- TRUE
  t <- floor(sqrt(n))
  for (i in 2:t){
    if (n%%i==0)  flag <- FALSE}
  if (n==2||n==3) flag <- TRUE
  return(flag)
}

result <- 1
for ( i in 2:20){
  if (IsPrime(i)) {
    print(i)
    k <- floor(log(20)/log(i))
    print(i^k)
    result <- result*i^k
  }
}
result
