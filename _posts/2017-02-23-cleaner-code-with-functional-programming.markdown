---
layout: post
title: "Cleaner Code With Functional Programming"
date: 2017-02-23 21:34:55 +0200
categories: development algorithm python workspace
---

I’m a Technical Team Leader at <a href="https://www.uclouvain.be" target="_blank">Université catholique de Louvain</a> and one of my responsibilities is to analyse pull requests sent by my team mates and all other contributors of <a href="http://uclouvain.github.io/osis/about/" target="_blank">OSIS project</a>. Each pull request is analysed according to some acceptance criteria, which determine if the pull request is accepted right away, accepted after completing requests for changes or refused. This process was taking too long because of excessive requests for changes, revealing too many problems to be fixed before the merges.

To gain some time on pull requests, I’ve decided to invest part of my time training the team to improve the general sense of maintainability, stability and reusability of the code. We’ve started with some pressure to change the established culture by following Robert C. Martin’s Clean Code video series. Uncle Bob, as he’s well known, seems to have radical ideas, but he is quite good at convincing us that he is not that radical at all. This initiative has been very valuable and the quality of recent pull requests has increased substantially.

Training sessions are now a weekly commitment. Nowadays, I’m reinforcing what we have learned during the clean code training, but more focused on the technologies we use. Recently, I’ve brought an interesting problem to be solved in Python using Test-Driven Development (TDD):

> Given a list of programmers and the maximum number of team members, let’s write an algorithm to randomly distribute programmers into teams. The maximum number of members is greater than 1. The minimum number of members is implicitly equal to 2. The list of programmers should contain at least two elements. A programmer can be member of only one team or no team at all but never member of 2 or more teams. The return should be a list of lists where the lists represent the teams.


We started writing a failing test and then just enough code to pass it. In this loop we ended up writing 7 tests to check the algorithm. Here is what we’ve got:

```

import random
import unittest

class TeamBuildingTest(unittest.TestCase):
  def test_list_contains_programmers(self):
    programmers = []
    teams = build_teams(programmers, 2)
    self.assertFalse(teams)

  def test_list_with_a_single_programmer(self):
    programmers = ['John']
    teams = build_teams(programmers, 2)
    self.assertFalse(teams)

  def test_minimal_team_size(self):
    programmers = ['John', 'Mary']
    teams = build_teams(programmers, 1)
    self.assertEqual(len(teams), 1)
    teams = build_teams(programmers, 0)
    self.assertEqual(len(teams), 1)

  def test_multiple_teams(self):
    programmers = ['John', 'Mary', 'Carl', 'Smith']
    teams = build_teams(programmers, 2)
    self.assertEqual(len(teams), 2)

  def test_odd_size_of_programmers_teams(self):
    programmers = ['John', 'Mary', 'Carl', 'Smith', 'Luc', 
                   'Paul', 'Ringo']
    teams = build_teams(programmers, 3)
    self.assertEqual(len(teams), 2)

  def test_minimal_and_maximal_team_size(self):
    programmers = ['John', 'Mary', 'Carl', 'Smith', 'Luc', 
                   'Paul', 'Ringo', 'Adam']
    teams = build_teams(programmers, 3)
    self.assertEqual(len(teams), 3)
    self.assertEqual(len(teams[0]), 3)
    self.assertEqual(len(teams[1]), 3)
    self.assertEqual(len(teams[2]), 2)

  def test_random_teams(self):
    programmers = ['John', 'Mary', 'Carl', 'Smith', 'Luc', 
                   'Paul']
    first_round = build_teams(programmers, 2)
    second_round = build_teams(programmers, 2)
    self.assertNotEqual(first_round, second_round)

```

We arrived together to the following solution:

```

def build_teams(programmers, size):
  if not programmers or len(programmers) < 2:
    return []
  else:
    return partition_teams(shuffle_programmers(programmers),
                           size if size > 1 else 2)

def shuffle_programmers(programmers):
  shuffled_programmers = list(programmers)
  random.shuffle(shuffled_programmers)
  return shuffled_programmers

def partition_teams(programmers, size=2):
  teams = []
  team = []

  for i, programmer in enumerate(programmers):
    if i == 0 or i % size != 0:
      team.append(programmer)
    else:
      teams.append(team)
      team = []
      team.append(programmer)
  if len(team) > 1:
    teams.append(team)
  return teams

```

To run all of it yourself, just put all the code in a file named “team_building.py” and run the tests using the following command in the same folder of the file:

```
$ python3 -m unittest -f 'team_building.py'
```

When we were done with the code we realised we didn’t do a good job in the function `partition_teams()`. It was written in the imperative style, with more variables and less meaningful controls. It’s difficult to extract another function from it without breaking other programming rules. However, with a 100% test coverage, we could rethink the problem and refactor the code without breaking the algorithm. Look at what we’ve got:

```

def partition_teams(progs, s):
  return [progs[x:y] for x in range(0, len(progs), s)
                     for y in range(s, len(progs) + s, s)
                     if x < y and y - x == s and 
                        len(progs[x:y]) > 1]
```

The new `partition_teams()` function uses list comprehension, a functional programming concept implemented in Python and many other languages nowadays. We’ve initially thought about nesting maps, filters and reduces, but it seemed to be heading towards complexity. List comprehension was proposed to address exactly the nested cases of higher order list operations, making the code more expressive.

The point about this list comprehension is to manipulate list slicing intervals to get what we want from the list of programmers. Given a list of 9 programmers from which we expect to extract pair programming teams, the first `for` produces the sequence 0, 2, 4, 6, and 8 and the second `for` produces the sequence 2, 4, 6, 8, and 10. When they execute we have a `y` for each `x`, producing the combinations (0, 2), (0, 4), (0, 6), (0, 8) … (4, 2), (4, 4), (4, 6) … (8, 6), (8, 8), (8, 10). Considering the rules of slicing, combinations like (4, 2) and (8, 8) won’t help us to solve the problem. So we exclude them with the conditions `(x < y)` and `(y - x == s)`. It partitions the programmers properly, but it isn't immune to teams of 1 person. Since this kind of team doesn't exist, we include the condition  `(len(progs[x:y]) > 1)` to take them out.

Notice that it has more semantics than the imperative solution because we get a dataset and we keep working with datasets in mind, while the imperative solution is more value-oriented and requires more control. Functional programming fascinates me and I'm glad to work with such a powerful language.

<a href="http://www.hildeberto.com/wp-content/uploads/2017/02/sponge-bob-functional-programming.jpg">![sponge-bob-functional-programming.jpg](/images/posts/sponge-bob-functional-programming.jpg)</a>
