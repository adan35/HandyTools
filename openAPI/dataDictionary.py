from collections import defaultdict

def makeDataDic(n, m=None):
  dataDic = defaultdict(lambda: -1)

  dataDic[f"Strg"] = f"""type: string"""

  dataDic[f"Strg{n}"] = f"""type: string
minLength: 1
maxLength: {n}
"""

  dataDic[f"Strg{n}"] = f"""type: string
minLength: 1
maxLength: {n}
"""

  dataDic[f"Strg{n}toStrg{m}"] = f"""type: string
minLength: {n}
maxLength: {m}
"""

  dataDic[f"AN{n}"] = f"""type: string
format: AN{n}
"""

  dataDic[f"Date"] = f"""type: string
format: Date
"""

  dataDic[f"DT"] = f"""type: string
format: DT
"""

  dataDic[f"D"] = f"""type: string
format: D
"""

  dataDic[f"N{n}"] = f"""type: string
minLength: 1
maxLength: {n}
"""

  dataDic[f"N{n}toN{m}"] = f"""type: string
format: N{m}
minLength: {n}
maxLength: {m}
"""

  dataDic[f"N{n},{m}"] = f"""type: string
format: N{n},{m}
"""

  dataDic[f"N{n}_N{m}"] =  f"""type: string
format: N{n}_N{m}
"""

  dataDic[f"A{n}"] =  f"""type: string
format: A{n}
"""

  dataDic[f"XN{n}"] =  f"""type: string
format: XN{n}
"""

  dataDic["DateTime"] =  f"""type: string
format: DateTime
"""
  return dataDic
