

with open("assets/countries.txt", "r") as file:
  countries = list()
  for item in file.read().splitlines():
    countries.append(item.replace("\n", ""))

  #countries = [item.replace("\n", "") for item in file.readlines()]
  print(*countries)
  countries = set(countries)
  print(*countries)

  ret = sorted(countries)
  print(*ret)
  with open("out.txt", "w") as out:
    #out.write("-".join(ret))
    print(*ret, sep="\n", file=out)

  ret = sorted(countries, key=len, reverse=True)
  with open("out.txt", "w") as out:
    #out.write("-".join(ret))
    print(*ret, sep="\n", file=out)

