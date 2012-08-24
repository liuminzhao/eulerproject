dat <-  read.table('names.txt', header=FALSE, sep=',')
y <- as.vector(dat)

r <- rank(y)

x <- c('COLIN')

subscore <- function(x){
  which(LETTERS==x)
}

score <- function(x){
  splitx <- as.matrix(unlist(strsplit(x,"")))
  sum(apply(splitx, 1, subscore))
}  

e22 <- function(y){
  y.score <- apply(as.matrix(y), 2, score)
  finalscore <- y.score*rank(y)
  sum(finalscore)
}

e22(y)

