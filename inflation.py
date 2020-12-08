

def Average(l):
  return (sum(l)/len(l))

def future_interest_rate(future_year,past_year):
  
  if past_year == 2019:
    i = df['Inflation Rate (%)'][df.Year == year].values
    return i

  else:
    n = past_year
    lst = []

    while n != future_year+1:
      x = df['Inflation Rate (%)'][df.Year == n].values
      lst.append(x)
      n += 1

    return Average(lst)

def past_interest_rate(future_year,past_year):
  
  if past_year == 2019:
    i = df['Inflation Rate (%)'][df.Year == past_year].values
    return i

  else:
    n = past_year
    lst = []

    while n != future_year+1:
      x = df['Inflation Rate (%)'][df.Year == n].values
      lst.append(x)
      n += 1

    return Average(lst)


def calculation(principal,end_year,start_year):
  p = principal
  n = start_year - end_year
  if start_year > end_year:
    i = future_interest_rate(end_year,start_year)
    result = p/((1+(i/100))**n)
    return result
  elif start_year < end_year:
    i = past_interest_rate(end_year,start_year)
    result = p*((1+(i/100))**n)
    return result