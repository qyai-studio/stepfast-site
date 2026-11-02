# Decision records

Protocol: entries are append-only. The only mutable field is `status`; overturn a decision with a new entry and mark the old one superseded. Review entries on their stated date.

## Active

### D-261102-seo-batch — Implement the StepFast SEO plan as one complete release
- status: active
- decided-by: user-ratified (overrode staged rollout recommendation)
- alternatives: release P0 first and follow with glossary/P1/P2; implement and release the complete approved plan together
- reasoning@constraints: the user prefers one coordinated release and expects the scope to be manageable
- regret-when: a material defect in one of the new pages requires rolling back the complete release
- review: 2027-02-02
