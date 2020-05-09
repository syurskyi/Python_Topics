c_ Robot:
	___  -   name, battery_100, skills_[]
		name _ name
		battery _ battery
		skills _ skills

	___ charge
		battery _ 100
		r_ self

	___ say_name
		__ battery > 0:
			battery -_ 1
			r_ f"BEEP BOOP BEEP BOOP.  I AM {name.upper()}"
		r_ "Low power.  Please charge and try again"

	___ learn_skill  new_skill, cost_to_learn
		__ battery >_ cost_to_learn:
			battery -_ cost_to_learn
			skills.append(new_skill)
			r_ f"WOAH. I KNOW {new_skill.upper()}"
		r_ "Insufficient battery. Please charge and try again"

		

