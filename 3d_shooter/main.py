from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Player
player = FirstPersonController()
player.cursor.visible = True
player.speed = 8

# Ground
ground = Entity(model='plane', scale=100, collider='box', texture='white_cube', texture_scale=(100,100))

# UI
score = 0
score_text = Text(text=f'Score: {score}', position=(-0.85, 0.45), scale=2)

# Game lists
enemies = []
bullets = []


def spawn_enemy():
    x = random.uniform(-20, 20)
    z = random.uniform(20, 60)
    e = Entity(model='cube', color=color.red, scale=1.6, position=(x, 1, z))
    enemies.append(e)

# initial enemies
for _ in range(6):
    spawn_enemy()


def input(key):
    # Shoot on left mouse button down
    if key == 'left mouse down':
        origin = camera.world_position + camera.forward * 1.5
        b = Entity(model='sphere', color=color.yellow, scale=0.2, position=origin)
        b.direction = camera.forward
        bullets.append(b)


def update():
    global score
    # move bullets
    for b in bullets[:]:
        b.position += b.direction * time.dt * 60
        # remove bullets that flew far
        if distance(b.position, player.position) > 200:
            destroy(b)
            bullets.remove(b)
            continue

        # check collisions (simple distance check)
        for e in enemies[:]:
            if b.position.distance(e.position) < 1.2:
                destroy(e)
                enemies.remove(e)
                destroy(b)
                bullets.remove(b)
                score += 1
                score_text.text = f'Score: {score}'
                spawn_enemy()
                break

    # move enemies toward the player (z decreases)
    for e in enemies:
        e.position += Vec3(0, 0, -1) * 2 * time.dt
        # if an enemy passes the player, reset and penalize
        if e.position.z < -5:
            e.position = Vec3(random.uniform(-20, 20), 1, random.uniform(20, 60))
            score = max(0, score - 1)
            score_text.text = f'Score: {score}'


if __name__ == '__main__':
    app.run()
