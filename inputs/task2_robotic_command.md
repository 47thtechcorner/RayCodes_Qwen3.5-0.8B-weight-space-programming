# Autonomous CNC Machining & Pick-and-Place Instruction

## Natural Language Machine Command
Initialize the toolhead at rapid home position with millimeter units and absolute positioning. Spindle start clockwise at **4500 RPM** with flood coolant active. Rapid move to clearance height $Z = 10.0\text{ mm}$ above entry coordinate $(X=25.0\text{ mm}, Y=40.0\text{ mm})$. Plunge linearly to milling depth $Z = -2.5\text{ mm}$ at feedrate $250\text{ mm/min}$. Mill a rectangular contour of $50\text{ mm}$ in $X$ and $30\text{ mm}$ in $Y$ at feedrate $800\text{ mm/min}$ with continuous tool path compensation. Retract toolhead to safe $Z = 15.0\text{ mm}$, disable spindle and coolant, and issue program end with coordinate reset.

---

## Technical Constraints & Requirements
- Target Standard: **ISO / RS-274D Compliant G-Code**
- Working Plane: XY Plane (`G17`)
- Units: Millimeters (`G21`), Absolute Mode (`G90`)
- Required Annotations: Concise inline operator comments for each block
