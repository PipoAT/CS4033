:- set_prolog_stack(global,  limit(8 000 000 000)).

% Define the blocks in your world
blocks([a, b, c, d, e, f]).

% A block X is a member of the list of blocks
block(X) :-
    blocks(BLOCKS),  % Extract the list BLOCKS
    member(X, BLOCKS).

% Given predicates
% move(X, Y, Z, S1, S2) holds true when the state S2 is obtained from the state S1 by moving the block X from the block Y onto the block Z.
move(X, Y, Z, S1, S2) :-
    select([on, X, Y], S1, [on, X, Z], TempS1),
    select([clear, Z], TempS1, [clear, Y], S2),
    X \= Y, % Ensure X and Y are different blocks
    X \= Z. % Ensure X and Z are different blocks

% clear(X, S) holds true when the block X is clear in the state S.
clear(X, S):-
    \+ member([on, _, X], S).


% notequal(X1, X2) holds true when X1 and X2 are not equal.
notequal(X, Y) :- X \= Y.
notequal(_, _).

% Substitute X with Y in a list
substitute(_, _, [], []).
substitute(X, Y, [X|T], [Y|T1]):-
    substitute(X, Y, T, T1).
substitute(X, Y, [H|T], [H|T1]):-
    X \= H,
    substitute(X, Y, T, T1).


% ...

% (i) move from a block onto the table
move_onto_table(X, Y, S1, S2):-
    member([clear, X], S1),
    member([on, X, Y], S1),
    substitute([on, X, Y], [on, X, 'table'], S1, INT),
    substitute([clear, X], [clear, Y], INT, S2).

% (ii) move from the table onto a block
move_onto_block(X, Y, S1, S2):-
    member([clear, X], S1),
    member([on, X, 'table'], S1),
    substitute([on, X, 'table'], [on, X, Y], S1, INT),
    (   member([clear, Y], S1) ->  % If Y was clear on the table
        substitute([clear, X], [clear, Y], INT, S2)
    ;   % If Y was not clear on the table
        substitute([clear, X], [clear], INT, INT2),
        substitute([clear, Y], [clear, 'table'], INT2, S2)
    ).

% Define start and goal states
start([[on, d, 'table'], [on, c, d], [on, a, c], [on, b, 'table'], [clear, a], [clear, b]]).
goal([[on, d, 'table'], [on, c, 'table'], [on, a, b], [on, b, 'table'], [clear, a], [clear, c], [clear, d]]).

% Define notYetVisited

notYetVisited(State, PathSoFar):-
    permutation(State, PermuteState),
    notmember(PermuteState, PathSoFar).

% Define path and connect predicates
path(S1, S2):-
    move(X, Y, Z, S1, S2).
path(S1, S2):-
    move_onto_table(X, Y, S1, S2).
path(S1, S2):-
    move_onto_block(X, Y, S1, S2).

connect(S1, S2) :- path(S1, S2).
connect(S1, S2) :- path(S2, S1).

% DFS with explicit tracking of visited states
dfs(X, Path, _):-
    goal(X),
    reverse(Path, ReversedPath),
    write('Goal reached. Path: '), write(ReversedPath), nl.
% else expand X by Y and find a path from Y
dfs(X, [X|Path], VISITED):-
    connect(X, Y),
    \+ member(Y, VISITED),
    write('Current state: '), write(X), nl,
    write('Moving to: '), write(Y), nl,
    dfs(Y, Path, [X|VISITED]).


% Define DFS with initial empty path and visited list
dfs(X, Path):-
    dfs(X, Path, []).

% Run the test
test_dfs:-
    start(StartState),
    dfs(StartState, Path),
    write('Final Path: '), write(Path), nl.

:- test_dfs.
