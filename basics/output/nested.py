print("hello")
print("please choice tyeps of books from belove options\n1.soft.\n2.hard.")
book=input()
if (book=="soft"):
  print("is the book perfect bound?")
  perfect_bound=input()
  if(perfect_bound=="yes"):
   print("Soft cover, perfect bound books are very popular!" )
  else:
    print("Soft covers with coils or stitches are great for short books")

elif(book=="hard"):
  print("Books with hard covers can be more expensive!" )

else:
  print("please choise one between 1 and 2.")

  
