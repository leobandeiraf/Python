import random as rd

options = [
            "javascript", "python", "java", "php", "c++", "ruby",
            "typescript", "swift", "scala", "shell", "powershell",
            "perl", "kotlin", "haskell"
]

optionSplit = []

randomOption = rd.choice(options)
for i in range(0, len(randomOption)):
    optionSplit.append(randomOption[i])

optionHash = []
for i in  optionSplit:
    optionHash.append("_ ")

print(optionHash)