# Codeforces Solutions

My solutions to [Codeforces](https://codeforces.com/) competitive programming problems, written in Python 3.

Codeforces is a competitive programming platform where you solve algorithmic problems against a fixed time and memory
limit. Every problem reads its input from **stdin** and writes its answer to **stdout**, so each file here is a small
standalone script. Run it, feed it the sample input from the problem statement, and compare the output.

## Solutions

| Problem | Solution | Idea |
| --- | --- | --- |
| [1A - Theatre Square](https://codeforces.com/problemset/problem/1/A) | [A.TheatreSquare.py](A.TheatreSquare.py) | Each side needs `ceil(n / a)` and `ceil(m / a)` flagstones; multiply the two. |
| [4A - Watermelon](https://codeforces.com/problemset/problem/4/A) | [A.Watermelon.py](A.Watermelon.py) | A weight splits into two even parts iff it is even and greater than 2. |
| [43A - Football](https://codeforces.com/problemset/problem/43/A) | [A.Football.py](A.Football.py) | Count the goals for each team in a dict and print the team with the most. |
| [50A - Domino piling](https://codeforces.com/problemset/problem/50/A) | [A.DominoPiling.py](A.DominoPiling.py) | Every domino covers 2 squares, so the answer is the board's area divided by 2, rounded down. |
| [58A - Chatroom](https://codeforces.com/problemset/problem/58/A) | [A.Chatroom.py](A.Chatroom.py) | "hello" has to appear as a subsequence, which the regex `h.*e.*l.*l.*o` checks directly. |
| [59A - Word](https://codeforces.com/problemset/problem/59/A) | [A.Word.py](A.Word.py) | Count uppercase and lowercase letters; switch to uppercase only if uppercase letters strictly outnumber lowercase ones. |
| [69A - Young Physicist](https://codeforces.com/problemset/problem/69/A) | [A.YoungPhysicist.py](A.YoungPhysicist.py) | Sum the x, y and z components of all the forces; the body is in equilibrium iff all three sums are 0. |
| [71A - Way Too Long Words](https://codeforces.com/problemset/problem/71/A) | [A.WayTooLongWords.py](A.WayTooLongWords.py) | Words longer than 10 characters become `first letter + count of middle letters + last letter`. |
| [110A - Nearly Lucky Number](https://codeforces.com/problemset/problem/110/A) | [A.NearlyLuckyNumber.py](A.NearlyLuckyNumber.py) | Count the digits that are 4 or 7; the number is nearly lucky iff that count is 4 or 7, the only lucky numbers small enough to be a digit count. |
| [112A - Petya and Strings](https://codeforces.com/problemset/problem/112/A) | [A.PetyaAndStrings.py](A.PetyaAndStrings.py) | Lowercase both strings and compare them letter by letter; the first position that differs decides the answer. |
| [118A - String Task](https://codeforces.com/problemset/problem/118/A) | [A.StringTask.py](A.StringTask.py) | Lowercase the word, drop the vowels (`y` counts as one), and put a `.` before each consonant that is left. |
| [122A - Lucky Division](https://codeforces.com/problemset/problem/122/A) | [A.LuckyDivision.py](A.LuckyDivision.py) | n is at most 1000, so it is enough to test divisibility by the 14 lucky numbers up to 777. |
| [131A - cAPS lOCK](https://codeforces.com/problemset/problem/131/A) | [A.CapsLock.py](A.CapsLock.py) | If every letter after the first is uppercase, Caps Lock was on, so swap the case of the whole word. |
| [158A - Next Round](https://codeforces.com/problemset/problem/158/A) | [A.NextRound.py](A.NextRound.py) | Count contestants with a positive score that is at least the k-th place score. |
| [158B - Taxi](https://codeforces.com/problemset/problem/158/B) | [B.Taxi.py](B.Taxi.py) | Groups of 4 ride alone, each 3 takes a 1 along, 2s share in pairs, a leftover 2 takes up to two 1s, and the remaining 1s ride four to a taxi. |
| [230A - Dragons](https://codeforces.com/problemset/problem/230/A) | [A.Dragons.py](A.Dragons.py) | Fight the dragons from weakest to strongest, collecting each bonus; fail as soon as one is at least as strong as Kirito. |
| [231A - Team](https://codeforces.com/problemset/problem/231/A) | [A.Team.py](A.Team.py) | A problem is implemented when at least 2 of the 3 friends are sure of the solution. |
| [236A - Boy or Girl](https://codeforces.com/problemset/problem/236/A) | [A.BoyOrGirl.py](A.BoyOrGirl.py) | Count the distinct characters in the username; an even count means female. |
| [263A - Beautiful Matrix](https://codeforces.com/problemset/problem/263/A) | [A.BeautifulMatrix.py](A.BeautifulMatrix.py) | Find the 1 and add up its row and column distances from the center cell. |
| [266A - Stones on the Table](https://codeforces.com/problemset/problem/266/A) | [A.StonesOnTheTable.py](A.StonesOnTheTable.py) | `itertools.groupby` splits the row into runs of one color; keep one stone per run and remove the rest. |
| [279B - Books](https://codeforces.com/problemset/problem/279/B) | [B.Books.py](B.Books.py) | Slide a window over the books, dropping books from the left whenever the total time goes over the limit; the answer is the longest window. |
| [281A - Word Capitalization](https://codeforces.com/problemset/problem/281/A) | [A.WordCapitalization.py](A.WordCapitalization.py) | Uppercase the first letter and leave the rest of the word unchanged. |
| [282A - Bit++](https://codeforces.com/problemset/problem/282/A) | [A.Bit++.py](A.Bit++.py) | Scan each statement for `++` or `--` and adjust the counter accordingly. |
| [339A - Helpful Maths](https://codeforces.com/problemset/problem/339/A) | [A.HelpfulMaths.py](A.HelpfulMaths.py) | Split the sum on `+`, sort the numbers, and join them back together with `+`. |
| [339B - Xenia and Ringroad](https://codeforces.com/problemset/problem/339/B) | [B.XeniaAndRingroad.py](B.XeniaAndRingroad.py) | Visit the houses in order around the one-way ring; reaching a lower-numbered house means wrapping around past house n. |
| [363B - Fence](https://codeforces.com/problemset/problem/363/B) | [B.Fence.py](B.Fence.py) | Slide a window of `k` planks along the fence, updating the sum as it moves, and keep the position with the smallest sum. |
| [456A - Laptops](https://codeforces.com/problemset/problem/456/A) | [A.Laptops.py](A.Laptops.py) | Prices and qualities are both permutations of 1 to n, so Alex is only wrong when every laptop has the same quality-to-price ratio. |
| [479A - Expression](https://codeforces.com/problemset/problem/479/A) | [A.Expression.py](A.Expression.py) | All values are 1 to 10, so the best expression depends on where the 1s are: add a 1 to its neighbor before multiplying, otherwise multiply everything. |
| [546A - Soldier and Bananas](https://codeforces.com/problemset/problem/546/A) | [A.SoldierAndBananas.py](A.SoldierAndBananas.py) | The i-th banana costs `i * k`; add up the cost of `w` bananas and borrow whatever goes over `n`, or 0. |
| [579A - Raising Bacteria](https://codeforces.com/problemset/problem/579/A) | [A.RaisingBacteria.py](A.RaisingBacteria.py) | Repeatedly take away the largest power of 2 that fits; the answer is the number of 1 bits in x. |
| [617A - Elephant](https://codeforces.com/problemset/problem/617/A) | [A.Elephant.py](A.Elephant.py) | Move 5 steps at a time, so the answer is `ceil(x / 5)`. |
| [706B - Interesting Drink](https://codeforces.com/problemset/problem/706/B) | [B.InterestingDrink.py](B.InterestingDrink.py) | Sort the prices once, then `bisect_right` counts how many shops each day's budget can afford. |
| [791A - Bear and Big Brother](https://codeforces.com/problemset/problem/791/A) | [A.BearAndBigBrother.py](A.BearAndBigBrother.py) | Simulate year by year (Limak triples, Bob doubles) until Limak is heavier. |
| [977A - Wrong Subtraction](https://codeforces.com/problemset/problem/977/A) | [A.WrongSubtraction.py](A.WrongSubtraction.py) | Simulate the subtractions directly: drop a trailing 0, otherwise subtract 1, `k` times. |
| [1374C - Move Brackets](https://codeforces.com/problemset/problem/1374/C) | [C.MoveBrackets.py](C.MoveBrackets.py) | Track the bracket balance from left to right; every `)` that would push it below 0 has to be moved, so count those. |
| [2276A - Perfect Sandwiches](https://codeforces.com/problemset/problem/2276/A) | [A.PerfectSandwiches.py](A.PerfectSandwiches.py) | Every sandwich needs at least one slice of sausage and more cheese than sausage, so the answer is `min(b, a - b)`, or -1 when `b >= a`. |
| [2278A - Fraction and Six](https://codeforces.com/problemset/problem/2278/A) | [A.FractionAndSix.py](A.FractionAndSix.py) | The numerator must hold every letter of the denominator plus exactly one extra `s`, `i` and `x`, and nothing else. |
| [2280A - Are They the Same?](https://codeforces.com/problemset/problem/2280/A) | [A.AreTheyTheSame.py](Codeforces%20Round%201133%20%28Div.%202%29/A.AreTheyTheSame.py) | Compare how many even numbers each array has: `a` can have at most as many as `b` when `k` is even, and at least as many when `k` is odd. |
| [2283A - Numbers on the Board](https://codeforces.com/problemset/problem/2283/A) | [A.NumbersOnTheBoard.py](Educational%20Codeforces%20Round%20196%20%28Rated%20for%20Div.%202%29/A.NumbersOnTheBoard.py) | Numbers that cancel out (`x` and `-x`, or 0) can stay, along with one extra number that then equals the board's sum; erase everything else. |
| [2283B - Rhythmic String](https://codeforces.com/problemset/problem/2283/B) | [B.RhythmicString.py](Educational%20Codeforces%20Round%20196%20%28Rated%20for%20Div.%202%29/B.RhythmicString.py) | For each distinct value, count the elements not divisible by it; the answer is the smallest count. |
| [2284A1 - 15K4JR3B (Easy Version)](https://codeforces.com/problemset/problem/2284/A1) | [A1.15K4JR3B(Easy Version).py](Codeforces%20Round%201132%20%28Div.%202%29%20%28virt.%20cont%29/A1.15K4JR3B%28Easy%20Version%29.py) | The doubled area is largest when the moves are split as evenly as possible between base and height, giving `floor(n / 2) * ceil(n / 2)`. |
| [2284A2 - 15K4JR3B (Hard Version)](https://codeforces.com/problemset/problem/2284/A2) | [A2.15K4JR3B(Hard Version).py](Codeforces%20Round%201132%20%28Div.%202%29%20%28virt.%20cont%29/A2.15K4JR3B%28Hard%20Version%29.py) | Take the moves from largest to smallest and add each one to the shorter of base and height, which keeps the two as equal as possible; the answer is their product. |
| [2284B - Introduction to the Niche Internet](https://codeforces.com/problemset/problem/2284/B) | [B.IntroductionToTheNicheInternet.py](Codeforces%20Round%201132%20%28Div.%202%29%20%28virt.%20cont%29/B.IntroductionToTheNicheInternet.py) | Put the largest `k` donations first in ascending order and the rest in descending order, so only the first `k` are very pleasant; it is impossible if the top `k + 1` values are all equal. |
| [2290A - Three Piles](https://codeforces.com/problemset/problem/2290/A) | [A.ThreePiles.py](Codeforces%20Round%201134%20%28Div.%204%29/A.ThreePiles.py) | One move changes two piles by 1 each, so the piles can only end up equal if they are three consecutive numbers, like 2, 3 and 4. |
| [2290B - Stubborn Pen](https://codeforces.com/problemset/problem/2290/B) | [B.StubbornPen.py](Codeforces%20Round%201134%20%28Div.%204%29/B.StubbornPen.py) | Track the pen's color; a letter of the other color costs one manual switch, after which the automatic switch puts the pen back where it was. |
| [2290C - Books on a Shelf](https://codeforces.com/problemset/problem/2290/C) | [C.BooksOnAShelf.py](Codeforces%20Round%201134%20%28Div.%204%29/C.BooksOnAShelf.py) | Sort the heights and deal them alternately to the left and right halves, so the shelf rises to the tallest book and falls again; each distinct height on each side is visible. |
| [2290D - Letters Down](https://codeforces.com/problemset/problem/2290/D) | [D.LettersDown.py](Codeforces%20Round%201134%20%28Div.%204%29/D.LettersDown.py) | Until the string is a palindrome, take the largest letter in any mismatched pair and lower every copy of it by one, counting the steps. |
| [2290E - Avalanche](https://codeforces.com/problemset/problem/2290/E) | [E.Avalanche.py](Codeforces%20Round%201134%20%28Div.%204%29/E.Avalanche.py) | Only every `(k + 1)`-th pile, starting from the first, matters; Alice wins iff those piles add up to an odd number. |

Most of these are A problems, the first and easiest problem in a round, focused on parsing input correctly and
translating a statement into a couple of conditions. The B and C problems ask for a little more: a greedy choice (Taxi,
Move Brackets), a simulation (Xenia and Ringroad), binary search (Interesting Drink) or a sliding window (Books, Fence).

## Running a solution

Each script reads from standard input, so you can either type the input by hand:

```bash
python A.Watermelon.py
```

or pipe a sample in from a file:

```bash
python A.Watermelon.py < sample.txt
```

Example (`4A Watermelon`):

```
Input:  8
Output: YES
```

## Requirements

Python 3.x. No external dependencies; everything uses the standard library only.

## Repository layout

Every solution is a single file named `<problem letter>.<ProblemName>.py`, for example `A.Team.py` for 231A Team or
`B.Taxi.py` for 158B Taxi. The table above maps each file to its problem.

Solutions written during a contest go in a folder named after that contest, for example
`Educational Codeforces Round 196 (Rated for Div. 2)/`.

New solutions get added as I work through more of the problemset.
