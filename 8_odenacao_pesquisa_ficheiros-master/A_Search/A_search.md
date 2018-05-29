# Search algorithm

_... is any algorithm which solves the Search problem, namely, to __retrieve information stored within some data structure__ ..._

[Source](https://en.wikipedia.org/wiki/Search_algorithm)

## Linear search

_(...) or __sequential search__ is a method for finding a target value within a list._

_It sequentially checks each element of the list for the target value until a match is found or until all the elements have been searched._

[Source](https://en.wikipedia.org/wiki/Linear_search)

## Binary search

_(...) is a search algorithm that finds the position of a target value within a __sorted array__._

(...) compares the target value to the middle element of the array; if they are unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful. If the search ends with the remaining half being empty, the target is not in the array.

[Source](https://en.wikipedia.org/wiki/Binary_search_algorithm)

## Linear vs Binary Search

![Comparison](https://github.com/ESTG-CRSI-P1-1718/8_odenacao_pesquisa_ficheiros/blob/master/A_Search/imgs/ls_vs_bs.gif)

[Source](https://blog.penjee.com/binary-vs-linear-search-animated-gifs/)

## Comparisons

| Nb. of items (n) | Linear search | Binary search |
| - | :-: | :-: |
| 8 | n | 3 |
| 100| n | 7 |
| 4000000000 | n | 32 |
| **Time** | *linear* | *logarithmic* |
| Complexity  | O(n) |  O(log n) |

### [Logarithms](https://www.khanacademy.org/math/algebra2/exponential-and-logarithmic-functions/properties-of-logarithms/v/introduction-to-logarithm-properties)

|Log | ^ |
| - | - |
|log(10) 100 = 2 | 10^2 = 100 |
log(2) 32 = 5 | 2^5 = 32 |
log 8 = 3 | 2^3 = 8 |

### Linear vs logarithmic

![Comparison](https://github.com/ESTG-CRSI-P1-1718/8_odenacao_pesquisa_ficheiros/blob/master/A_Search/imgs/nlogn.png)
