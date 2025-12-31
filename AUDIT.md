# Black Box Audit

## Observed Behavior
- Input: list of numbers
- Output: rounded float
- Threshold behavior at value > 10

## Technical Debt
- Hardcoded business rules
- No configuration
- No tests
- Logic coupled to execution

## Risk
- Any change could silently alter calculations
- Business intent undocumented
