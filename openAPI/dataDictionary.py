from collections import defaultdict

def makeDataDic(isRequest, n, m=-1, s=''):
  dataDic = defaultdict(lambda: -1)

  if n != "" and isRequest:
    dataDic[f"Strg{n}"] = f"""type: string
{s}minLength: 1
{s}maxLength: {n}
"""
  else:
    dataDic[f"Strg"] = f"""type: string
{s}format: Strg\n"""
    dataDic[f"Strg{n}"] = f"""type: string
{s}format: Strg{n}\n"""

  if isRequest:
    dataDic[f"Char{n}"] = f"""type: string
{s}minLength: 1
{s}maxLength: {n}
"""
    dataDic[f"Strg{n}toStrg{m}"] = f"""type: string
{s}minLength: {n}
{s}maxLength: {m}
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
  else:
    dataDic[f"Char{n}"] = f"""type: string
{s}format: Char{n}\n"""
    dataDic[f"Strg{n}toStrg{m}"] = f"""type: string
{s}format: Strg{m}\n"""
    dataDic[f"N{n}"] = f"""type: string
{s}format: N{n}\n"""
    dataDic[f"N{n}toN{m}"] = f"""type: string
{s}format: N{m}\n"""


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
{s}format: Date
"""

  dataDic[f"N{n},{m}"] = f"""type: number
{s}format: N{n},{m}
"""

  dataDic[f"N{n}_N{m}"] =  f"""type: number
{s}format: N{n},N{m}"""

  dataDic[f"A{n}"] =  f"""type: string
{s}format: A{n}"""

  dataDic[f"XN{n}"] =  f"""type: string
{s}format: XN{n}"""

  dataDic["DateTime"] =  f"""type: string
{s}format: DateTime
"""

  dataDic["DateTime"] =  f"""type: string
{s}format: A1
"""

  dataDic[f"INT"] = f"""type: integer
"""

  dataDic[f"Time"] = f"""type: string
{s}format: Time
"""

  dataDic[f"N{n}"] = f"""type: string
{s}format: N{n}
"""

  return dataDic
