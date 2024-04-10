import json
from pathlib import Path
from collections import defaultdict

with open("doctest-list.json") as fp:
    L = json.load(fp)

test_collection = defaultdict(list)

for x in L:
    y = Path(x)
    z = "/".join(y.parents[0].parts)
    test_collection[z].append(x)

sorted_test_collection = defaultdict(list)
K = sorted(test_collection.keys())
for k in K:
    if k in ["docs/source/en/model_doc", "docs/source/en/tasks"]:
        for v in sorted(test_collection[k]):
            sorted_test_collection[v] = v
    else:
        sorted_test_collection[k] = " ".join(sorted(test_collection[k]))

K = sorted(sorted_test_collection.keys())
print(dict(sorted_test_collection))


# for k in K:
    # print(k)
    # print(sorted_test_collection[k])
    # print("-" * 80)


# print(len(sorted_test_collection))
