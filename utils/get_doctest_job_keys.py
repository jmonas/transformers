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

sorted_test_collection = defaultdict(str)
K = sorted(test_collection.keys())
for k in K:
    if k in ["docs/source/en/model_doc", "docs/source/en/tasks"]:
        for v in sorted(test_collection[k]):
            sorted_test_collection[v] = v
    else:
        sorted_test_collection[k] = " ".join(sorted(test_collection[k]))

K = sorted(sorted_test_collection.keys())
print(K[0:4])

num_splits = 2
num_jobs = len(K)
num_jobs_per_splits = num_jobs // num_splits

job_splits = []
end = 0
for idx in range(num_splits):
    start = end
    end = start + num_jobs_per_splits + (1 if idx < num_jobs % num_splits else 0)
    job_splits.append(K[start:end])
print(job_splits)


# for k in K:
    # print(k)
    # print(sorted_test_collection[k])
    # print("-" * 80)


# print(len(sorted_test_collection))
