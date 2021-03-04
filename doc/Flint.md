# Flint
Flint is a project and asset management software. Which uses `json` files as  database.

## [[Flint-terminal]]
Flint terminal is a terminal version of flint.

## ILM Structure
- $SHOW
	- assets
		- $TYPE
			- $NAME
				- modeling
				- rigging
				- surfaceing
				- mattePainting
				- shaderDevelopment
	- sequences
		- tools
		- shaders
		- common( a sequence with data common to all sequences)
		- $SEQ
			- $SHOT
				- common (a shot with data common to shots in the seq)
				- capture
				- animation
				- charaterFinaling
				- lighting
				- compositing
				- mattePainting
				- dynamics (oter than charFin, eg dirt, splashes, flames)
				- rotoscoping