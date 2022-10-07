from collections import defaultdict

def makeDataDic(n, m=-1, s=''):
  dataDic = defaultdict(lambda: -1)

  dataDic[f"Strg"] = f"""type: string"""

  dataDic[f"Strg{n}"] = f"""type: string
{s}minLength: 1
{s}maxLength: {n}
"""

  dataDic[f"Strg{n}"] = f"""type: string
{s}minLength: 1
{s}maxLength: {n}
"""

  dataDic[f"Strg{n}toStrg{m}"] = f"""type: string
{s}minLength: {n}
{s}maxLength: {m}
"""

  dataDic[f"AN{n}"] = f"""type: string
{s}format: AN{n}
"""

  dataDic[f"Date"] = f"""type: string
{s}format: Date
"""

  dataDic[f"DT"] = f"""type: string
{s}format: DT
"""

  dataDic[f"D"] = f"""type: string
{s}format: D
"""

  dataDic[f"N{n}"] = f"""type: string
{s}minLength: 1
{s}maxLength: {n}
"""

  dataDic[f"N{n}toN{m}"] = f"""type: string
{s}format: N{m}
{s}minLength: {n}
{s}maxLength: {m}
"""

  dataDic[f"N{n},{m}"] = f"""type: string
{s}format: N{n},{m}
"""

  dataDic[f"N{n}_N{m}"] =  f"""type: string
{s}format: N{n}_N{m}"""

  dataDic[f"A{n}"] =  f"""type: string
{s}format: A{n}"""

  dataDic[f"XN{n}"] =  f"""type: string
{s}format: XN{n}"""

  dataDic["DateTime"] =  f"""type: string
{s}format: DateTime
"""
  return dataDic
