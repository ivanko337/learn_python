#!/usr/bin/env python

import re

phone1 = re.compile(r"((?:[(]\\d+[)])?\\s*\\d+(?:-\\d+)?)$")
print(phone1)
