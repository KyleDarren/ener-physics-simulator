# ENER - a python physics simulator [UNFINISHED]

## Finsihed Concepts
1. Circle Collision Detection
The circle collision detection is done by comparing the current distance of the circles by its reference distance (I don't know if this is the right term). The current distance is calulated using the distance formula and the inputs are the coordinates of each of the circle's origin (located in the middle of the circle by default). In the other hand the reference distance is calculated by adding the radius of the each of the circles. The reference distance is the distance of the origin where the circles touch each other circumference. If the current distance is less than the reference distance, then collision is detected
