# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:29:17 2026

@author: Palesa Diako
"""

import pandas as pd

# Example data
data = {
"Author": ["Palesa Diako"],
"Year": [2025],
"Title": ["Fabrication of Bi-doped WO3/CFA for efficient photocatalytic degradation of CIP under visible light irradiation"],
"Journal": ["Open Access"],

}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("publications.csv", index=False)