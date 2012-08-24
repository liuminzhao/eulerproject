for (a in 1:333){
  for (b in a:500) {
    if (a^2==(1000-a)*(1000-a-2*b) )
      print(a*b*(1000-a-b))
  }
}

    
