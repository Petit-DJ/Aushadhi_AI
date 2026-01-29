You are building an AI‑assisted drug discovery web platform that guides a user through the entire early discovery pipeline, from selecting a disease to analyzing optimized drug candidates — all through a clean, explainable, step‑by‑step UI.

The platform:

Abstracts complex biology + ML behind a guided workflow

Uses public bioactivity data (IC50, targets, compounds)

Focuses on visualization, ranking, and decision support

Is frontend‑driven, with backend orchestration

Think of it as:

“An interactive, explainable drug discovery pipeline rather than a black‑box ML tool.”

🔹 End‑to‑end user flow (what the user experiences)
Select a disease

System identifies relevant biological targets

Known compounds for that target are screened

New molecular analogs are generated

Molecules are ranked using IC50 & other metrics

User inspects detailed analysis of top candidates

Final shortlist / report view

Each step = one page, one clear purpose.

🔹 What needs to be built (step‑by‑step)
Step 1: Landing + Disease Selection
Purpose: Entry point

Disease input + popular disease chips

Start screening CTA

No science yet — simple and friendly

Step 2: Processing / Transition State
Purpose: Explain that “thinking” is happening

Animated lab / molecular visuals

Step text (e.g. “Analyzing disease biology”)

Sets user expectations

Step 3: Target Identification Page
Purpose: Map disease → biology

Show target proteins related to disease

Let user understand what is being attacked

Select one or more targets

Step 4: Molecular Screening Page
Purpose: Show known chemistry

Fetch known compounds acting on the target

Display molecular cards (SMILES / abstract visuals)

Show confidence / affinity indicators

Step 5: Analog Generation Page
Purpose: Lead optimization

Generate new molecular analogs from top leads

Show “AI‑generated” but validated molecules

Emphasize scaffold‑based variation

Step 6: Ranking & Evaluation Page
Purpose: Decision making

Rank molecules by:

IC50

Affinity

Drug‑likeness

Toxicity (optional / mocked)

Highlight best candidates visually

Step 7: Detailed Molecule Analysis Page
Purpose: Deep dive

Expanded view of a selected molecule

Key metrics + AI insights

Confidence / risk indicators

Explain why it ranks well

Step 8: Summary / Report Page (optional but powerful)
Purpose: Closure

Final shortlisted molecules

Pipeline summary (what happened at each step)

Export / share (conceptual)

🔹 Technical build order (important)
Build in this order to avoid rework:

Frontend pages + routing (static / mocked data)

Reusable UI components (cards, steppers, tables)

Backend APIs (return mock → then real data)

Supabase schema + ChEMBL ingestion

AI/ML integration layer (generation + scoring)

Polish: animations, explanations, edge cases

🔹 Key principle to follow throughout
One page = one responsibility

One prompt = one page

User should never feel lost

Always explain what the system is doing and why

