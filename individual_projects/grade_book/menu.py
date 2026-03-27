import tkinter as tk
import random

class DinoGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dino Jump - Press SPACE to Jump")
        self.root.resizable(False, False)

        # Canvas Setup
        self.canvas_w, self.canvas_h = 600, 200
        self.canvas = tk.Canvas(self.root, width=self.canvas_w, height=self.canvas_h, bg="white")
        self.canvas.pack()

        # Game State
        self.running = True
        self.score = 0
        self.gravity = 0.8
        self.jump_power = -12
        
        # Dino Stats
        self.dino_x, self.dino_y = 50, 150
        self.dino_w, self.dino_h = 30, 30
        self.dino_vel_y = 0
        self.is_jumping = False

        # Obstacles
        self.cacti = []
        self.cactus_speed = 7
        self.spawn_timer = 0

        # Draw Ground
        self.canvas.create_line(0, 180, 600, 180, fill="black", width=2)

        # Create Dino Sprite (Green Square)
        self.dino = self.canvas.create_rectangle(
            self.dino_x, self.dino_y, 
            self.dino_x + self.dino_w, self.dino_y + self.dino_h, 
            fill="#535353", outline="black"
        )

        # UI
        self.score_text = self.canvas.create_text(540, 20, text="Score: 0", font=("Courier", 12, "bold"))

        # Controls
        self.root.bind("<space>", self.jump)
        
        self.update_game()
        self.root.mainloop()

    def jump(self, event):
        if not self.is_jumping:
            self.dino_vel_y = self.jump_power
            self.is_jumping = True

    def update_game(self):
        if not self.running: return

        # 1. Dino Physics
        self.dino_vel_y += self.gravity
        self.dino_y += self.dino_vel_y

        if self.dino_y >= 150: # Floor hit
            self.dino_y = 150
            self.dino_vel_y = 0
            self.is_jumping = False

        self.canvas.coords(self.dino, self.dino_x, self.dino_y, 
                                     self.dino_x + self.dino_w, self.dino_y + self.dino_h)

        # 2. Spawn Cacti
        self.spawn_timer += 1
        if self.spawn_timer > random.randint(40, 80):
            h = random.randint(25, 50)
            c = self.canvas.create_rectangle(610, 180 - h, 630, 180, fill="green")
            self.cacti.append(c)
            self.spawn_timer = 0

        # 3. Move & Collision
        for c in self.cacti[:]:
            self.canvas.move(c, -self.cactus_speed, 0)
            coords = self.canvas.coords(c)
            
            # Simple Collision Box
            if (self.dino_x < coords[2] and self.dino_x + self.dino_w > coords[0] and
                self.dino_y < coords[3] and self.dino_y + self.dino_h > coords[1]):
                self.game_over()
            
            # Score & Cleanup
            if coords[2] < 0:
                self.canvas.delete(c)
                self.cacti.remove(c)
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                if self.score % 5 == 0: self.cactus_speed += 0.5 # Increase difficulty

        self.root.after(20, self.update_game)

    def game_over(self):
        self.running = False
        self.canvas.create_text(300, 100, text="GAME OVER", font=("Courier", 30, "bold"), fill="red")
        self.canvas.create_text(300, 130, text="Close and Rerun to Restart", font=("Courier", 10))

if __name__ == "__main__":
    DinoGame()
