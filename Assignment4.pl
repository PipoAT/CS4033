% Generate a random list with N elements
randomList(N, LIST) :-
    length(LIST, N),
    maplist(random(1, 100), LIST).  % Adjust the range as needed

% swap the first two elements if they are not in order
swap([X, Y|T], [Y, X | T]) :-
    Y =< X.
% swap elements in the tail
swap([H|T], [H|T1]) :-
    swap(T, T1).

% repeatedly steps through the list comparing adjacent elements and swaps
% them if they are in the wrong order. Repeat process until list is sorted
bubbleSort(L, SL) :-
    swap(L, L1),
    !,
    bubbleSort(L1, SL).
bubbleSort(L, L).

% Ordered: Checks that two consecutive elements are ordered, and recurse on the tail.
ordered([]).
ordered([_X]).
ordered([H1, H2|T]) :-
    H1 =< H2,
    ordered([H2|T]).

% Insert: Insert an element E into a sorted list SL to get SLE
% 1st clause: Insert into an empty list. Then, Insert E into the
% list if E is smaller or equal to the first element
insert(X, [], [X]).
insert(E, [H|T], [E, H|T]) :-
    ordered(T),
    E =< H,
    !.
% 2nd clause: Insert E into the list recursively
insert(E, [H|T], [H|T1]) :-
    ordered(T),
    insert(E, T, T1).

% Insertion Sort: This takes an unsorted list 'L' and returns the sorted 'SL'.
% The algorithm iterates through each element in the unsorted list, placing it
% in the correct position within the already sorted part of the list.
insertionSort([], []).
insertionSort([H|T], SORTED) :-
    insertionSort(T, T1),
    insert(H, T1, SORTED).

% Merge Sort: Takes list L and returns SL. It splits the list into
% smaller halves, recursively sorts them, and then merges the sorted
% halves to produce the final sorted list.
mergeSort([], []).
mergeSort([X], [X]) :- !.
mergeSort(L, SL) :-
    split_in_half(L, L1, L2),
    mergeSort(L1, S1),
    mergeSort(L2, S2),
    merge(S1, S2, SL).

% Integer division of N by N1 to calculate the midpoint index.
% This predicate takes two integers, N and N1, and calculates their integer division,
% unifying the result with R. It is used to determine the midpoint index for splitting lists
intDiv(N, N1, R) :- R is div(N, N1).
split_in_half([], [], []).
split_in_half([X], [], [X]).
split_in_half(L, L1, L2) :-
    length(L, N),
    intDiv(N, 2, N1),
    length(L1, N1),
    append(L1, L2, L).

% Merge Sort: Merge two sorted lists into one sorted list
merge([], L, L). % Merge an empty list with another list results in the other list
merge(L, [], L). % Merge a list with an empty list results in the first list (no changes)
merge([H1|T1], [H2|T2], [H1|T]) :-
    H1 =< H2,
    merge(T1, [H2|T2], T).
merge([H1|T1], [H2|T2], [H2|T]) :-
    H1 > H2,
    merge([H1|T1], T2, T).


% Quick Sort Split: Split a list into elements smaller or equal to X (SMALL) and elements larger than X (BIG)
split(_, [], [], []).
split(X, [H|T], [H|SMALL], BIG) :-
    H =< X,
    split(X, T, SMALL, BIG).
split(X, [H|T], SMALL, [H|BIG]) :-
    X =< H,
    split(X, T, SMALL, BIG).

% Quick Sort: Base case for an empty list, already sorted.
% Then use recursive case to sort a list by dividing it into elements smaller
% or equal to the pivot (SMALL) and elements larger than the pivot (BIG).
% Recursively sort both SMALL and BIG, then append them together with the pivot.
quickSort([], []).
quickSort([H|T], LS) :-
    split(H, T, SMALL, BIG),
    quickSort(SMALL, S),
    quickSort(BIG, B),
    append(S, [H|B], LS).

% Hybrid Sort: When the length of a list is less than the THRESHOLD,
% hybridSort calls a SMALL sort (either bubbleSort or insertionSort)to sort the list.
% When the list length is greater than the THRESHOLD, hybridSort behaves like a BIG sort,
% (but does not call one) and splits the list into smaller sizes until said size
% is smaller than the THRESHOLD, where a SMALL sort is called. The small sorted lists are
% then combined.

hybridSort(LIST, bubbleSort, BIGALG, THRESHOLD, SLIST):-
	length(LIST, N), N=< THRESHOLD,
	bubbleSort(LIST, SLIST).

hybridSort(LIST, insertionSort, BIGALG, THRESHOLD, SLIST):-
	length(LIST, N), N=<T,
	insertionSort(LIST, SLIST).

hybridSort(LIST, SMALL, mergeSort, THRESHOLD, SLIST):-
	length(LIST, N), N> THRESHOLD,
	split_in_half(LIST, L1, L2),
	hybridSort(L1, SMALL, mergeSort, THRESHOLD, S1),
	hybridSort(L2, SMALL, mergeSort, THRESHOLD, S2),
	merge(S1,S2, SLIST).

hybridSort([H|T], SMALL, quickSort, THRESHOLD, SLIST):-
	length(LIST, N), N > THRESHOLD,
	split(H, T, L1, L2),
	hybridSort(L1, SMALL, quickSort, THRESHOLD, S1),
    hybridSort(L1, SMALL, quickSort, THRESHOLD, S2),
	append(S1, [H|S2], SLIST).

hybridSort([H|T], SMALL, quickSort, THRESHOLD, SLIST):-
	length([H|T], N), N > THRESHOLD,
	split(H, T, L1, L2),
	hybridSort(L1, SMALL, quickSort, THRESHOLD, S1),
    hybridSort(L1, SMALL, quickSort, THRESHOLD, S2),
	append(S1, [H|S2], SLIST).


% Define a predicate to time the execution of a goal
time_goal(Goal, Time) :-
    get_time(Start),
    Goal,
    get_time(End),
    Time is End - Start.

% The Result of 8 Runs:
% Bubble Sort with a list of length 50

randomList(50, LIST).
time_goal(bubbleSort(LIST, BubbleSorted), Time),
write('Original List: '), write(LIST), nl,
write('Bubble Sorted List: '), write(BubbleSorted), nl,
format('Time taken for Bubble Sort: ~3f seconds', [Time]), nl.

% Insertion Sort with a list of length 50

time_goal(insertionSort(LIST, InsertionSorted), Time),
write('Original List: '), write(LIST), nl,
write('Insertion Sorted List: '), write(InsertionSorted), nl,
format('Time taken for Insertion Sort: ~3f seconds', [Time]), nl.


% Merge Sort with a list of length 50

time_goal(mergeSort(LIST, MergeSorted), Time),
write('Original List: '), write(LIST), nl,
write('Merge Sorted List: '), write(MergeSorted), nl,
format('Time taken for Merge Sort: ~3f seconds', [Time]), nl.


% Quick Sort with a list of length 50

time_goal(quickSort(LIST, QuickSorted), Time),
write('Original List: '), write(LIST), nl,
write('Quick Sorted List: '), write(Quickorted), nl,
format('Time taken for Quick Sort: ~3f seconds', [Time]), nl.


% Hybrid Sort with a list of length 50
time_goal(hybridSort(LIST, bubbleSort, mergeSort, 10, SLIST), Time),
write('Original List: '), write(LIST), nl,
write('Hybrid Sorted List: '), write(SLIST), nl,
format('Time taken for Hybrid Sort: ~3f seconds', [Time]), nl.

% Bubble Sort Performance:
% Bubble sort with time complexity of O(n^2) in the worst case, making it
% slow for larger lists.
% Best Case: O(n) if the list is sorted already
% Worst Case: O(n^2) when the list is sorted in reverse order

% Insertion Sort Performance:
% Best Case: O(n) when the list is already sorted
% Worst Case: O(n^2) when the list is sorted in reverse order
% It's efficient for small lists and works by inserting elements into their correct positions within sorted part of the list.

% Merge Sort Performance:
% Best Case: O(n log n)
% Worst Case: O(n log n)
% Merge sort is an efficient sorting algorithm that works by recursively dividing the list into smaller halves, sorting them, and then merging them back together.

% Quick Sort Performance:
% Best Case: O(n log n)
% Worst Case: O(n^2)
% Quick sort is efficient on average. It works by partitioning the list based on a pivot element and recursively sorting the partitions.

% Hybrid Sort Performance:
% The hybrid sort combines insertion and quicksort algorithms to improve its performance.




