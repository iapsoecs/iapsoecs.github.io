from datetime import datetime
from pathlib import Path
import sys
from unidecode import unidecode

date = datetime.now().strftime("%Y-%m-%d")
job = input("job title (postoc, tenure, professor, PhD, etc):\n")
domain = input("domain (physical oceanography, chemistry, etc):\n")
city = input("city (Reading, Paris, etc):\n")
country = input("country (UK, USA, etc):\n")
lab = input("lab / university / institute (University of Reading, etc):\n")
print("Description / job advertisement:\n( Ctrl-D or Ctrl-Z ( windows ) to save it.)\n")
description = "".join(sys.stdin.readlines())


# filename
filename = unidecode(
    f"_posts/{date}-{job}-{lab}.md".replace(" ", "_").replace("'", "_")
)
while Path(filename).exists():
    filename += "_another"

to_write = f"""---
layout: post
title: {job.capitalize()} position in {domain} ({city}, {country})
subtitle: {lab.capitalize()}
tags: [{job}, {domain}, {country}]
comments: false
---
{description}
"""

with open(filename, "w") as f:
    f.write(to_write)
