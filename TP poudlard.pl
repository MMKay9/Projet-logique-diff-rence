suspect(drago).
suspect(neville).
suspect(ginny).

verify_statements(Guilty) :-
    (Guilty = drago -> \+ verify_statements(neville); true),
    (Guilty = drago -> \+ verify_statements(ginny); true),
    (Guilty = ginny -> (\+ verify_statements(drago), \+ verify_statements(neville)); true).

find_culprit(X) :-
    suspect(X),
    verify_statements(X),
    forall((suspect(Y), Y \= X), \+ verify_statements(Y)).
