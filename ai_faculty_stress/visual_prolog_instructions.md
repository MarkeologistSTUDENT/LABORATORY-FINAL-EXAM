Visual Prolog integration instructions

This short guide shows two easy ways to use the `predicted_stress_facts.pl` information in a Visual Prolog Console Application.

Option A (recommended, easiest): Copy facts into a Visual Prolog source file

1. Open Visual Prolog IDE and create a new Console Application project.
2. Add a new source file (e.g., `data.pred`) to your project and paste the contents of `predicted_stress_facts.pl` into it. Make sure to define the fact predicate in the project sources according to Visual Prolog templates.
3. Add a predicate implementation that maps stress labels to recommendations. You can copy the recommendation clauses below into an implementation file.

Option B: Parse the `predicted_stress_facts.pl` at runtime (if you prefer to keep it external)

Visual Prolog doesn't have `consult/1` like SWI-Prolog. Instead, read the file line by line and assert facts. Example pseudo-code:

implement main predicate:
 - open_file('predicted_stress_facts.pl')
 - while not end_of_file:
     read line
     parse FacultyID and Stress
     assert(predicted_stress(FacultyID, Stress))
 - close file
 - iterate predicted_stress facts and print recommendations

Copy-paste-ready recommendation clauses (logical mapping):

recommendation('Low') -> ["Maintain current schedule", "Monitor workload"].
recommendation('Medium') -> ["Prioritize tasks", "Delegate where possible", "Aim for 7+ hours sleep"].
recommendation('High') -> ["Reduce course load if possible", "Request administrative support", "Schedule regular breaks", "Seek wellness resources"].

Visual Prolog notes:
- Exact syntax for asserting facts and lists is different from SWI-Prolog. If you want, provide your Visual Prolog version (e.g., Visual Prolog 7.4) and I will produce a ready-to-import `.pro` project and properly formatted `.pred` source files.
