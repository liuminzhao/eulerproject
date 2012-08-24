sum1 <- sum2 <- 0

for (i in 1:100){
  sum1 <- sum1+i^2
  sum2 <- sum2+i
}
sum2^2-sum1
