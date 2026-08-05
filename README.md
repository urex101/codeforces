# Codeforces Solutions

My solutions to [Codeforces](https://codeforces.com/) competitive programming problems, written in Python 3.

Codeforces is a competitive programming platform where you solve algorithmic problems against a fixed time and memory
limit. Every problem reads its input from **stdin** and writes its answer to **stdout**, so each file here is a small
standalone script. Run it, feed it the sample input from the problem statement, and compare the output.

## Solutions

| Problem | Solution | Idea |
| --- | --- | --- |
| [4A - Watermelon](https://codeforces.com/problemset/problem/4/A) | [watermelon.py](watermelon.py) | A weight splits into two even parts iff it is even and greater than 2. |
| [71A - Way Too Long Words](https://codeforces.com/problemset/problem/71/A) | [toolongwords.py](toolongwords.py) | Words longer than 10 characters become `first letter + count of middle letters + last letter`. |
| [158A - Next Round](https://codeforces.com/problemset/problem/158/A) | [nextround.py](nextround.py) | Count contestants with a positive score that is at least the k-th place score. |
| [231A - Team](https://codeforces.com/problemset/problem/231/A) | [ATeam.py](ATeam.py) | A problem is implemented when at least 2 of the 3 friends are sure of the solution. |
| [282A - Bit++](https://codeforces.com/problemset/problem/282/A) | [ABit++.py](ABit++.py) | Scan each statement for `++` or `--` and adjust the counter accordingly. |

All of these are 800-rated introductory problems (Div. 2 A), focused on parsing input correctly and translating a
statement into a couple of conditions.

## Running a solution

Each script reads from standard input, so you can either type the input by hand:

```bash
python watermelon.py
```

or pipe a sample in from a file:

```bash
python watermelon.py < sample.txt
```

Example (`4A Watermelon`):

```
Input:  8
Output: YES
```

## Requirements

Python 3.x. No external dependencies; everything uses the standard library only.

## Repository layout

```
.
├── ABit++.py         # 282A Bit++
├── ATeam.py          # 231A Team
├── nextround.py      # 158A Next Round
├── toolongwords.py   # 71A Way Too Long Words
└── watermelon.py     # 4A Watermelon
```

New solutions get added as I work through more of the problemset.
