% predicted_stress_visual.pl
% Copy-paste-ready Prolog source that combines predicted_stress facts and recommendation rules.
% This file uses standard Prolog syntax and is intended to be easy to import into Visual Prolog projects
% by either copying the facts into a Visual Prolog source file or parsing them at runtime.

% --------------------- Predicted stress facts ---------------------
% (These will be overwritten when you re-run the Python exporter; copy the latest facts
%  from predicted_stress_facts.pl or replace these lines with its contents.)

% Example facts (the real file will have many lines like these)
predicted_stress('F001','Medium').
predicted_stress('F002','Low').
predicted_stress('F003','High').

% --------------------- Recommendation rules ---------------------
% Map stress label -> list of recommendations (as Prolog lists)
recommendation('Low', ['Maintain current schedule', 'Monitor workload']).
recommendation('Medium', ['Prioritize tasks', 'Delegate where possible', 'Aim for 7+ hours sleep']).
recommendation('High', ['Reduce course load if possible', 'Request administrative support', 'Schedule regular breaks', 'Seek wellness resources']).

% --------------------- Utility predicates ---------------------
% Print all recommendations for each predicted_stress fact.
print_all_recommendations :-
    forall(predicted_stress(Fac, Stress), (
        recommendation(Stress, Recs),
        format("~w: ~w -> Recommendations: ~w~n", [Fac, Stress, Recs])
    )).

% Example entry point for Prolog systems that support initialization hooks (SWI-Prolog):
% :- initialization(print_all_recommendations).

% For Visual Prolog: see `visual_prolog_instructions.md` for a small snippet you can paste into a
% Visual Prolog Console Application which loads this file and iterates the facts.
