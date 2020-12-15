def short_pattern():
  pattern = {"sequence":"101","occurrences":5}
  return pattern
def mediume_pattern():
  pattern = {"sequence":"11001","occurrences":25}
  return pattern
def longe_pattern():
  pattern = {"sequence":"1100110011001100","occurrences":50}
  return pattern
def run():
  print("Analysing patterns...")
  patterns = {
   "short sequence":short_pattern(),
   "medium sequence":mediume_pattern(),
   "longe sequence":longe_pattern()
  }

  for key , value in patterns.items():
    print(f"{key}: {value}")


run()