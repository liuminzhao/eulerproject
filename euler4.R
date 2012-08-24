a <- 999:900
b <- 999:900

maxm <- 0
for (i in 1:length(a))
  for ( j in 1:length(b))
     if (grepl( '^([0-9])([0-9])([0-9])\\3\\2\\1$', tmp <- a[i]*b[j])) if (tmp>maxm) {print(tmp);maxm <- tmp}
