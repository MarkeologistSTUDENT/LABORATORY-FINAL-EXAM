
% recommender_example.pl -- load predicted_stress_facts.pl and produce recommendations
:- initialization(main).

recommendation('Low', ['Maintain current schedule', 'Monitor workload']).
recommendation('Medium', ['Prioritize tasks', 'Delegate where possible', 'Ensure 7+ hours sleep']).
recommendation('High', ['Reduce course load if possible', 'Request admin support', 'Schedule regular breaks', 'Seek wellness resources']).

main :-
    consult('predicted_stress_facts.pl'),
    forall(predicted_stress(F, S), (
        recommendation(S, Recs),
        format("~w: ~w -> Recommendations: ~w~n", [F, S, Recs])
    )),
    halt.
