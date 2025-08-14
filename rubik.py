from ursina import *
from ursina import Ursina
import random
import copy
import kociemba
#Please ignore this file, it is not used in the game.
#It is only used to create a Python implementation of the Rubik's Cube
#It is used only for comparative study with the Rubik.js file
class RubiksCube(Entity):
    def __init__(self):
        super().__init__()
        
        # Initialize a solved cube
        # Each face is represented by a 3x3 matrix
        # 0: White, 1: Yellow, 2: Red, 3: Orange, 4: Green, 5: Blue
        self.faces = {
            'U': [[0 for _ in range(3)] for _ in range(3)],  # White (Up)
            'D': [[1 for _ in range(3)] for _ in range(3)],  # Yellow (Down)
            'F': [[2 for _ in range(3)] for _ in range(3)],  # Red (Front)
            'B': [[3 for _ in range(3)] for _ in range(3)],  # Orange (Back)
            'R': [[4 for _ in range(3)] for _ in range(3)],  # Green (Right)
            'L': [[5 for _ in range(3)] for _ in range(3)]   # Blue (Left)
        }
        
        self.move_count = 0
        self.solution_moves = []
        
        # Define the colors for each face
        self.colors = {
            0: color.white,    # White
            1: color.yellow,   # Yellow
            2: color.red,      # Red
            3: color.orange,   # Orange
            4: color.green,    # Green
            5: color.blue      # Blue
        }
        
        # Create the cube visual
        self.cube_parent = Entity(parent=self)
        self.create_cube_visual()
        
    def create_cube_visual(self):
        """Create the visual representation of the cube"""
        # Clear existing visual
        for child in self.cube_parent.children:
            destroy(child)
        
        # Size of each sticker
        sticker_size = 0.95
        gap = 0.05
        
        # Create each sticker
        for face_name, face in self.faces.items():
            for i in range(3):
                for j in range(3):
                    # Calculate position based on face and position within face
                    if face_name == 'U':  # Up face
                        x = (j - 1) * (sticker_size + gap)
                        y = 1.5
                        z = (1 - i) * (sticker_size + gap)
                        rotation = (90, 0, 0)
                    elif face_name == 'D':  # Down face
                        x = (j - 1) * (sticker_size + gap)
                        y = -1.5
                        z = (i - 1) * (sticker_size + gap)
                        rotation = (90, 0, 0)
                    elif face_name == 'F':  # Front face
                        x = (j - 1) * (sticker_size + gap)
                        y = (1 - i) * (sticker_size + gap)
                        z = 1.5
                        rotation = (0, 0, 0)
                    elif face_name == 'B':  # Back face
                        x = (1 - j) * (sticker_size + gap)
                        y = (1 - i) * (sticker_size + gap)
                        z = -1.5
                        rotation = (0, 180, 0)
                    elif face_name == 'R':  # Right face
                        x = 1.5
                        y = (1 - i) * (sticker_size + gap)
                        z = (1 - j) * (sticker_size + gap)
                        rotation = (0, 90, 0)
                    elif face_name == 'L':  # Left face
                        x = -1.5
                        y = (1 - i) * (sticker_size + gap)
                        z = (j - 1) * (sticker_size + gap)
                        rotation = (0, -90, 0)
                    
                    # Create the sticker
                    sticker = Entity(
                        parent=self.cube_parent,
                        model='quad',
                        color=self.colors[face[i][j]],
                        position=(x, y, z),
                        rotation=rotation,
                        scale=(sticker_size, sticker_size, 1)
                    )
                    
                    # Add a black border to the sticker
                    border = Entity(
                        parent=sticker,
                        model='quad',
                        color=color.black,
                        position=(0, 0, -0.001),
                        scale=(1.05, 1.05, 1)
                    )
    
    def rotate_face_clockwise(self, face):
        """Rotate a face 90 degrees clockwise"""
        n = len(face)
        return [[face[n - j - 1][i] for j in range(n)] for i in range(n)]
    
    def rotate_face_counterclockwise(self, face):
        """Rotate a face 90 degrees counterclockwise"""
        n = len(face)
        return [[face[j][n - i - 1] for j in range(n)] for i in range(n)]
    
    def U(self):
        """Rotate Up face clockwise"""
        self.faces['U'] = self.rotate_face_clockwise(self.faces['U'])
        
        # Save the front top row
        temp = self.faces['F'][0][:]
        
        # Front top = Right top
        self.faces['F'][0] = self.faces['R'][0][:]
        
        # Right top = Back top (reversed)
        self.faces['R'][0] = self.faces['B'][0][::-1]
        
        # Back top = Left top (reversed)
        self.faces['B'][0] = self.faces['L'][0][::-1]
        
        # Left top = saved temp
        self.faces['L'][0] = temp
        
        self.move_count += 1
        self.solution_moves.append("U")
        self.create_cube_visual()
    
    def U_prime(self):
        """Rotate Up face counterclockwise"""
        self.faces['U'] = self.rotate_face_counterclockwise(self.faces['U'])
        
        # Save the front top row
        temp = self.faces['F'][0][:]
        
        # Front top = Left top
        self.faces['F'][0] = self.faces['L'][0][:]
        
        # Left top = Back top (reversed)
        self.faces['L'][0] = self.faces['B'][0][::-1]
        
        # Back top = Right top (reversed)
        self.faces['B'][0] = self.faces['R'][0][::-1]
        
        # Right top = saved temp
        self.faces['R'][0] = temp
        
        self.move_count += 1
        self.solution_moves.append("U'")
        self.create_cube_visual()
    
    def U2(self):
        """Rotate Up face 180 degrees"""
        self.U()
        self.U()
        self.solution_moves.pop()  # Remove the extra U
        self.solution_moves.pop()  # Remove the extra U
        self.solution_moves.append("U2")
        self.move_count -= 1  # Adjust move count
    
    def D(self):
        """Rotate Down face clockwise"""
        self.faces['D'] = self.rotate_face_clockwise(self.faces['D'])
        
        # Save the front bottom row
        temp = self.faces['F'][2][:]
        
        # Front bottom = Left bottom
        self.faces['F'][2] = self.faces['L'][2][:]
        
        # Left bottom = Back bottom (reversed)
        self.faces['L'][2] = self.faces['B'][2][::-1]
        
        # Back bottom = Right bottom (reversed)
        self.faces['B'][2] = self.faces['R'][2][::-1]
        
        # Right bottom = saved temp
        self.faces['R'][2] = temp
        
        self.move_count += 1
        self.solution_moves.append("D")
        self.create_cube_visual()
    
    def D_prime(self):
        """Rotate Down face counterclockwise"""
        self.faces['D'] = self.rotate_face_counterclockwise(self.faces['D'])
        
        # Save the front bottom row
        temp = self.faces['F'][2][:]
        
        # Front bottom = Right bottom
        self.faces['F'][2] = self.faces['R'][2][:]
        
        # Right bottom = Back bottom (reversed)
        self.faces['R'][2] = self.faces['B'][2][::-1]
        
        # Back bottom = Left bottom (reversed)
        self.faces['B'][2] = self.faces['L'][2][::-1]
        
        # Left bottom = saved temp
        self.faces['L'][2] = temp
        
        self.move_count += 1
        self.solution_moves.append("D'")
        self.create_cube_visual()
    
    def D2(self):
        """Rotate Down face 180 degrees"""
        self.D()
        self.D()
        self.solution_moves.pop()  # Remove the extra D
        self.solution_moves.pop()  # Remove the extra D
        self.solution_moves.append("D2")
        self.move_count -= 1  # Adjust move count
    
    def F(self):
        """Rotate Front face clockwise"""
        self.faces['F'] = self.rotate_face_clockwise(self.faces['F'])
        
        # Save the top right column
        temp = [self.faces['U'][2][i] for i in range(3)]
        
        # Top right = Left bottom (reversed)
        for i in range(3):
            self.faces['U'][2][i] = self.faces['L'][2 - i][2]
        
        # Left bottom = Down left
        for i in range(3):
            self.faces['L'][i][2] = self.faces['D'][0][i]
        
        # Down left = Right top (reversed)
        for i in range(3):
            self.faces['D'][0][i] = self.faces['R'][2 - i][0]
        
        # Right top = saved temp
        for i in range(3):
            self.faces['R'][i][0] = temp[i]
        
        self.move_count += 1
        self.solution_moves.append("F")
        self.create_cube_visual()
    
    def F_prime(self):
        """Rotate Front face counterclockwise"""
        self.faces['F'] = self.rotate_face_counterclockwise(self.faces['F'])
        
        # Save the top right column
        temp = [self.faces['U'][2][i] for i in range(3)]
        
        # Top right = Right top
        for i in range(3):
            self.faces['U'][2][i] = self.faces['R'][i][0]
        
        # Right top = Down left (reversed)
        for i in range(3):
            self.faces['R'][i][0] = self.faces['D'][0][2 - i]
        
        # Down left = Left bottom
        for i in range(3):
            self.faces['D'][0][i] = self.faces['L'][i][2]
        
        # Left bottom = saved temp (reversed)
        for i in range(3):
            self.faces['L'][i][2] = temp[2 - i]
        
        self.move_count += 1
        self.solution_moves.append("F'")
        self.create_cube_visual()
    
    def F2(self):
        """Rotate Front face 180 degrees"""
        self.F()
        self.F()
        self.solution_moves.pop()  # Remove the extra F
        self.solution_moves.pop()  # Remove the extra F
        self.solution_moves.append("F2")
        self.move_count -= 1  # Adjust move count
    
    def B(self):
        """Rotate Back face clockwise"""
        self.faces['B'] = self.rotate_face_clockwise(self.faces['B'])
        
        # Save the top left column
        temp = [self.faces['U'][0][i] for i in range(3)]
        
        # Top left = Right top (reversed)
        for i in range(3):
            self.faces['U'][0][i] = self.faces['R'][2 - i][2]
        
        # Right top = Down right
        for i in range(3):
            self.faces['R'][i][2] = self.faces['D'][2][i]
        
        # Down right = Left bottom (reversed)
        for i in range(3):
            self.faces['D'][2][i] = self.faces['L'][2 - i][0]
        
        # Left bottom = saved temp
        for i in range(3):
            self.faces['L'][i][0] = temp[i]
        
        self.move_count += 1
        self.solution_moves.append("B")
        self.create_cube_visual()
    
    def B_prime(self):
        """Rotate Back face counterclockwise"""
        self.faces['B'] = self.rotate_face_counterclockwise(self.faces['B'])
        
        # Save the top left column
        temp = [self.faces['U'][0][i] for i in range(3)]
        
        # Top left = Left bottom
        for i in range(3):
            self.faces['U'][0][i] = self.faces['L'][i][0]
        
        # Left bottom = Down right (reversed)
        for i in range(3):
            self.faces['L'][i][0] = self.faces['D'][2][2 - i]
        
        # Down right = Right top
        for i in range(3):
            self.faces['D'][2][i] = self.faces['R'][i][2]
        
        # Right top = saved temp (reversed)
        for i in range(3):
            self.faces['R'][i][2] = temp[2 - i]
        
        self.move_count += 1
        self.solution_moves.append("B'")
        self.create_cube_visual()
    
    def B2(self):
        """Rotate Back face 180 degrees"""
        self.B()
        self.B()
        self.solution_moves.pop()  # Remove the extra B
        self.solution_moves.pop()  # Remove the extra B
        self.solution_moves.append("B2")
        self.move_count -= 1  # Adjust move count
    
    def R(self):
        """Rotate Right face clockwise"""
        self.faces['R'] = self.rotate_face_clockwise(self.faces['R'])
        
        # Save the front right column
        temp = [self.faces['F'][i][2] for i in range(3)]
        
        # Front right = Down right
        for i in range(3):
            self.faces['F'][i][2] = self.faces['D'][i][2]
        
        # Down right = Back left (reversed)
        for i in range(3):
            self.faces['D'][i][2] = self.faces['B'][2 - i][0]
        
        # Back left = Up right
        for i in range(3):
            self.faces['B'][i][0] = self.faces['U'][i][2]
        
        # Up right = saved temp
        for i in range(3):
            self.faces['U'][i][2] = temp[i]
        
        self.move_count += 1
        self.solution_moves.append("R")
        self.create_cube_visual()
    
    def R_prime(self):
        """Rotate Right face counterclockwise"""
        self.faces['R'] = self.rotate_face_counterclockwise(self.faces['R'])
        
        # Save the front right column
        temp = [self.faces['F'][i][2] for i in range(3)]
        
        # Front right = Up right
        for i in range(3):
            self.faces['F'][i][2] = self.faces['U'][i][2]
        
        # Up right = Back left (reversed)
        for i in range(3):
            self.faces['U'][i][2] = self.faces['B'][2 - i][0]
        
        # Back left = Down right
        for i in range(3):
            self.faces['B'][i][0] = self.faces['D'][i][2]
        
        # Down right = saved temp
        for i in range(3):
            self.faces['D'][i][2] = temp[i]
        
        self.move_count += 1
        self.solution_moves.append("R'")
        self.create_cube_visual()
    
    def R2(self):
        """Rotate Right face 180 degrees"""
        self.R()
        self.R()
        self.solution_moves.pop()  # Remove the extra R
        self.solution_moves.pop()  # Remove the extra R
        self.solution_moves.append("R2")
        self.move_count -= 1  # Adjust move count
    
    def L(self):
        """Rotate Left face clockwise"""
        self.faces['L'] = self.rotate_face_clockwise(self.faces['L'])
        
        # Save the front left column
        temp = [self.faces['F'][i][0] for i in range(3)]
        
        # Front left = Up left
        for i in range(3):
            self.faces['F'][i][0] = self.faces['U'][i][0]
        
        # Up left = Back right (reversed)
        for i in range(3):
            self.faces['U'][i][0] = self.faces['B'][2 - i][2]
        
        # Back right = Down left
        for i in range(3):
            self.faces['B'][i][2] = self.faces['D'][i][0]
        
        # Down left = saved temp
        for i in range(3):
            self.faces['D'][i][0] = temp[i]
        
        self.move_count += 1
        self.solution_moves.append("L")
        self.create_cube_visual()
    
    def L_prime(self):
        """Rotate Left face counterclockwise"""
        self.faces['L'] = self.rotate_face_counterclockwise(self.faces['L'])
        
        # Save the front left column
        temp = [self.faces['F'][i][0] for i in range(3)]
        
        # Front left = Down left
        for i in range(3):
            self.faces['F'][i][0] = self.faces['D'][i][0]
        
        # Down left = Back right (reversed)
        for i in range(3):
            self.faces['D'][i][0] = self.faces['B'][2 - i][2]
        
        # Back right = Up left
        for i in range(3):
            self.faces['B'][i][2] = self.faces['U'][i][0]
        
        # Up left = saved temp
        for i in range(3):
            self.faces['U'][i][0] = temp[i]
        
        self.move_count += 1
        self.solution_moves.append("L'")
        self.create_cube_visual()
    
    def L2(self):
        """Rotate Left face 180 degrees"""
        self.L()
        self.L()
        self.solution_moves.pop()  # Remove the extra L
        self.solution_moves.pop()  # Remove the extra L
        self.solution_moves.append("L2")
        self.move_count -= 1  # Adjust move count
    
    def scramble(self, num_moves=20):
        """Scramble the cube with random moves"""
        moves = [self.U, self.U_prime, self.U2, 
                 self.D, self.D_prime, self.D2,
                 self.F, self.F_prime, self.F2,
                 self.B, self.B_prime, self.B2,
                 self.R, self.R_prime, self.R2,
                 self.L, self.L_prime, self.L2]
        
        # Reset move count and solution moves
        self.move_count = 0
        self.solution_moves = []
        
        # Apply random moves
        for _ in range(num_moves):
            random.choice(moves)()
        
        # Reset move count and solution moves after scrambling
        scramble_moves = self.solution_moves.copy()
        self.move_count = 0
        self.solution_moves = []
        
        return scramble_moves
    
    def is_solved(self):
        """Check if the cube is solved (each face has a single color)"""
        for face_name, face in self.faces.items():
            color = face[1][1]  # Center color
            for row in face:
                for cell in row:
                    if cell != color:
                        return False
        return True
    
    def to_kociemba_string(self):
        """Convert the cube state to a string format for the Kociemba solver"""
        # Kociemba uses a specific string format:
        # UB...UR...UF...UL...DB...DR...DF...DL...FR...FL...BR...BL...UFR...UFL...UBL...UBR...DFR...DFL...DBL...DBR
        
        # Create the Kociemba string
        kociemba_str = ""
        
        # Add the edge pieces
        # UB edge
        kociemba_str += "U" if self.faces['U'][0][1] == 0 else "D" if self.faces['U'][0][1] == 1 else "F" if self.faces['U'][0][1] == 2 else "B" if self.faces['U'][0][1] == 3 else "R" if self.faces['U'][0][1] == 4 else "L"
        kociemba_str += "B" if self.faces['B'][0][1] == 3 else "F" if self.faces['B'][0][1] == 2 else "U" if self.faces['B'][0][1] == 0 else "D" if self.faces['B'][0][1] == 1 else "L" if self.faces['B'][0][1] == 5 else "R"
        
        # UR edge
        kociemba_str += "U" if self.faces['U'][1][2] == 0 else "D" if self.faces['U'][1][2] == 1 else "F" if self.faces['U'][1][2] == 2 else "B" if self.faces['U'][1][2] == 3 else "R" if self.faces['U'][1][2] == 4 else "L"
        kociemba_str += "R" if self.faces['R'][0][1] == 4 else "L" if self.faces['R'][0][1] == 5 else "F" if self.faces['R'][0][1] == 2 else "B" if self.faces['R'][0][1] == 3 else "U" if self.faces['R'][0][1] == 0 else "D"
        
        # UF edge
        kociemba_str += "U" if self.faces['U'][2][1] == 0 else "D" if self.faces['U'][2][1] == 1 else "F" if self.faces['U'][2][1] == 2 else "B" if self.faces['U'][2][1] == 3 else "R" if self.faces['U'][2][1] == 4 else "L"
        kociemba_str += "F" if self.faces['F'][0][1] == 2 else "B" if self.faces['F'][0][1] == 3 else "U" if self.faces['F'][0][1] == 0 else "D" if self.faces['F'][0][1] == 1 else "R" if self.faces['F'][0][1] == 4 else "L"
        
        # UL edge
        kociemba_str += "U" if self.faces['U'][1][0] == 0 else "D" if self.faces['U'][1][0] == 1 else "F" if self.faces['U'][1][0] == 2 else "B" if self.faces['U'][1][0] == 3 else "R" if self.faces['U'][1][0] == 4 else "L"
        kociemba_str += "L" if self.faces['L'][0][1] == 5 else "R" if self.faces['L'][0][1] == 4 else "F" if self.faces['L'][0][1] == 2 else "B" if self.faces['L'][0][1] == 3 else "U" if self.faces['L'][0][1] == 0 else "D"
        
        # DB edge
        kociemba_str += "D" if self.faces['D'][0][1] == 1 else "U" if self.faces['D'][0][1] == 0 else "F" if self.faces['D'][0][1] == 2 else "B" if self.faces['D'][0][1] == 3 else "R" if self.faces['D'][0][1] == 4 else "L"
        kociemba_str += "B" if self.faces['B'][2][1] == 3 else "F" if self.faces['B'][2][1] == 2 else "U" if self.faces['B'][2][1] == 0 else "D" if self.faces['B'][2][1] == 1 else "L" if self.faces['B'][2][1] == 5 else "R"
        
        # DR edge
        kociemba_str += "D" if self.faces['D'][1][2] == 1 else "U" if self.faces['D'][1][2] == 0 else "F" if self.faces['D'][1][2] == 2 else "B" if self.faces['D'][1][2] == 3 else "R" if self.faces['D'][1][2] == 4 else "L"
        kociemba_str += "R" if self.faces['R'][2][1] == 4 else "L" if self.faces['R'][2][1] == 5 else "F" if self.faces['R'][2][1] == 2 else "B" if self.faces['R'][2][1] == 3 else "U" if self.faces['R'][2][1] == 0 else "D"
        
        # DF edge
        kociemba_str += "D" if self.faces['D'][2][1] == 1 else "U" if self.faces['D'][2][1] == 0 else "F" if self.faces['D'][2][1] == 2 else "B" if self.faces['D'][2][1] == 3 else "R" if self.faces['D'][2][1] == 4 else "L"
        kociemba_str += "F" if self.faces['F'][2][1] == 2 else "B" if self.faces['F'][2][1] == 3 else "U" if self.faces['F'][2][1] == 0 else "D" if self.faces['F'][2][1] == 1 else "R" if self.faces['F'][2][1] == 4 else "L"
        
        # DL edge
        kociemba_str += "D" if self.faces['D'][1][0] == 1 else "U" if self.faces['D'][1][0] == 0 else "F" if self.faces['D'][1][0] == 2 else "B" if self.faces['D'][1][0] == 3 else "R" if self.faces['D'][1][0] == 4 else "L"
        kociemba_str += "L" if self.faces['L'][2][1] == 5 else "R" if self.faces['L'][2][1] == 4 else "F" if self.faces['L'][2][1] == 2 else "B" if self.faces['L'][2][1] == 3 else "U" if self.faces['L'][2][1] == 0 else "D"
        
        # FR edge
        kociemba_str += "F" if self.faces['F'][1][2] == 2 else "B" if self.faces['F'][1][2] == 3 else "U" if self.faces['F'][1][2] == 0 else "D" if self.faces['F'][1][2] == 1 else "R" if self.faces['F'][1][2] == 4 else "L"
        kociemba_str += "R" if self.faces['R'][1][0] == 4 else "L" if self.faces['R'][1][0] == 5 else "F" if self.faces['R'][1][0] == 2 else "B" if self.faces['R'][1][0] == 3 else "U" if self.faces['R'][1][0] == 0 else "D"
        
        # FL edge
        kociemba_str += "F" if self.faces['F'][1][0] == 2 else "B" if self.faces['F'][1][0] == 3 else "U" if self.faces['F'][1][0] == 0 else "D" if self.faces['F'][1][0] == 1 else "R" if self.faces['F'][1][0] == 4 else "L"
        kociemba_str += "L" if self.faces['L'][1][2] == 5 else "R" if self.faces['L'][1][2] == 4 else "F" if self.faces['L'][1][2] == 2 else "B" if self.faces['L'][1][2] == 3 else "U" if self.faces['L'][1][2] == 0 else "D"
        
        # BR edge
        kociemba_str += "B" if self.faces['B'][1][2] == 3 else "F" if self.faces['B'][1][2] == 2 else "U" if self.faces['B'][1][2] == 0 else "D" if self.faces['B'][1][2] == 1 else "R" if self.faces['B'][1][2] == 4 else "L"
        kociemba_str += "R" if self.faces['R'][1][2] == 4 else "L" if self.faces['R'][1][2] == 5 else "F" if self.faces['R'][1][2] == 2 else "B" if self.faces['R'][1][2] == 3 else "U" if self.faces['R'][1][2] == 0 else "D"
        
        # BL edge
        kociemba_str += "B" if self.faces['B'][1][0] == 3 else "F" if self.faces['B'][1][0] == 2 else "U" if self.faces['B'][1][0] == 0 else "D" if self.faces['B'][1][0] == 1 else "R" if self.faces['B'][1][0] == 4 else "L"
        kociemba_str += "L" if self.faces['L'][1][0] == 5 else "R" if self.faces['L'][1][0] == 4 else "F" if self.faces['L'][1][0] == 2 else "B" if self.faces['L'][1][0] == 3 else "U" if self.faces['L'][1][0] == 0 else "D"
        
        # Add the corner pieces
        # UFR corner
        kociemba_str += "U" if self.faces['U'][2][2] == 0 else "D" if self.faces['U'][2][2] == 1 else "F" if self.faces['U'][2][2] == 2 else "B" if self.faces['U'][2][2] == 3 else "R" if self.faces['U'][2][2] == 4 else "L"
        kociemba_str += "F" if self.faces['F'][0][2] == 2 else "B" if self.faces['F'][0][2] == 3 else "U" if self.faces['F'][0][2] == 0 else "D" if self.faces['F'][0][2] == 1 else "R" if self.faces['F'][0][2] == 4 else "L"
        kociemba_str += "R" if self.faces['R'][0][0] == 4 else "L" if self.faces['R'][0][0] == 5 else "F" if self.faces['R'][0][0] == 2 else "B" if self.faces['R'][0][0] == 3 else "U" if self.faces['R'][0][0] == 0 else "D"
        
        # UFL corner
        kociemba_str += "U" if self.faces['U'][2][0] == 0 else "D" if self.faces['U'][2][0] == 1 else "F" if self.faces['U'][2][0] == 2 else "B" if self.faces['U'][2][0] == 3 else "R" if self.faces['U'][2][0] == 4 else "L"
        kociemba_str += "F" if self.faces['F'][0][0] == 2 else "B" if self.faces['F'][0][0] == 3 else "U" if self.faces['F'][0][0] == 0 else "D" if self.faces['F'][0][0] == 1 else "R" if self.faces['F'][0][0] == 4 else "L"
        kociemba_str += "L" if self.faces['L'][0][2] == 5 else "R" if self.faces['L'][0][2] == 4 else "F" if self.faces['L'][0][2] == 2 else "B" if self.faces['L'][0][2] == 3 else "U" if self.faces['L'][0][2] == 0 else "D"
        
        # UBL corner
        kociemba_str += "U" if self.faces['U'][0][0] == 0 else "D" if self.faces['U'][0][0] == 1 else "F" if self.faces['U'][0][0] == 2 else "B" if self.faces['U'][0][0] == 3 else "R" if self.faces['U'][0][0] == 4 else "L"
        kociemba_str += "B" if self.faces['B'][0][2] == 3 else "F" if self.faces['B'][0][2] == 2 else "U" if self.faces['B'][0][2] == 0 else "D" if self.faces['B'][0][2] == 1 else "L" if self.faces['B'][0][2] == 5 else "R"
        kociemba_str += "L" if self.faces['L'][0][0] == 5 else "R" if self.faces['L'][0][0] == 4 else "F" if self.faces['L'][0][0] == 2 else "B" if self.faces['L'][0][0] == 3 else "U" if self.faces['L'][0][0] == 0 else "D"
        
        # UBR corner
        kociemba_str += "U" if self.faces['U'][0][2] == 0 else "D" if self.faces['U'][0][2] == 1 else "F" if self.faces['U'][0][2] == 2 else "B" if self.faces['U'][0][2] == 3 else "R" if self.faces['U'][0][2] == 4 else "L"
        kociemba_str += "B" if self.faces['B'][0][0] == 3 else "F" if self.faces['B'][0][0] == 2 else "U" if self.faces['B'][0][0] == 0 else "D" if self.faces['B'][0][0] == 1 else "L" if self.faces['B'][0][0] == 5 else "R"
        kociemba_str += "R" if self.faces['R'][0][2] == 4 else "L" if self.faces['R'][0][2] == 5 else "F" if self.faces['R'][0][2] == 2 else "B" if self.faces['R'][0][2] == 3 else "U" if self.faces['R'][0][2] == 0 else "D"
        
        # DFR corner
        kociemba_str += "D" if self.faces['D'][2][2] == 1 else "U" if self.faces['D'][2][2] == 0 else "F" if self.faces['D'][2][2] == 2 else "B" if self.faces['D'][2][2] == 3 else "R" if self.faces['D'][2][2] == 4 else "L"
        kociemba_str += "F" if self.faces['F'][2][2] == 2 else "B" if self.faces['F'][2][2] == 3 else "U" if self.faces['F'][2][2] == 0 else "D" if self.faces['F'][2][2] == 1 else "R" if self.faces['F'][2][2] == 4 else "L"
        kociemba_str += "R" if self.faces['R'][2][0] == 4 else "L" if self.faces['R'][2][0] == 5 else "F" if self.faces['R'][2][0] == 2 else "B" if self.faces['R'][2][0] == 3 else "U" if self.faces['R'][2][0] == 0 else "D"
        
        # DFL corner
        kociemba_str += "D" if self.faces['D'][2][0] == 1 else "U" if self.faces['D'][2][0] == 0 else "F" if self.faces['D'][2][0] == 2 else "B" if self.faces['D'][2][0] == 3 else "R" if self.faces['D'][2][0] == 4 else "L"
        kociemba_str += "F" if self.faces['F'][2][0] == 2 else "B" if self.faces['F'][2][0] == 3 else "U" if self.faces['F'][2][0] == 0 else "D" if self.faces['F'][2][0] == 1 else "R" if self.faces['F'][2][0] == 4 else "L"
        kociemba_str += "L" if self.faces['L'][2][2] == 5 else "R" if self.faces['L'][2][2] == 4 else "F" if self.faces['L'][2][2] == 2 else "B" if self.faces['L'][2][2] == 3 else "U" if self.faces['L'][2][2] == 0 else "D"
        
        # DBL corner
        kociemba_str += "D" if self.faces['D'][0][0] == 1 else "U" if self.faces['D'][0][0] == 0 else "F" if self.faces['D'][0][0] == 2 else "B" if self.faces['D'][0][0] == 3 else "R" if self.faces['D'][0][0] == 4 else "L"
        kociemba_str += "B" if self.faces['B'][2][2] == 3 else "F" if self.faces['B'][2][2] == 2 else "U" if self.faces['B'][2][2] == 0 else "D" if self.faces['B'][2][2] == 1 else "L" if self.faces['B'][2][2] == 5 else "R"
        kociemba_str += "L" if self.faces['L'][2][0] == 5 else "R" if self.faces['L'][2][0] == 4 else "F" if self.faces['L'][2][0] == 2 else "B" if self.faces['L'][2][0] == 3 else "U" if self.faces['L'][2][0] == 0 else "D"
        
        # DBR corner
        kociemba_str += "D" if self.faces['D'][0][2] == 1 else "U" if self.faces['D'][0][2] == 0 else "F" if self.faces['D'][0][2] == 2 else "B" if self.faces['D'][0][2] == 3 else "R" if self.faces['D'][0][2] == 4 else "L"
        kociemba_str += "B" if self.faces['B'][2][0] == 3 else "F" if self.faces['B'][2][0] == 2 else "U" if self.faces['B'][2][0] == 0 else "D" if self.faces['B'][2][0] == 1 else "L" if self.faces['B'][2][0] == 5 else "R"
        kociemba_str += "R" if self.faces['R'][2][2] == 4 else "L" if self.faces['R'][2][2] == 5 else "F" if self.faces['R'][2][2] == 2 else "B" if self.faces['R'][2][2] == 3 else "U" if self.faces['R'][2][2] == 0 else "D"
        
        return kociemba_str
    
    def solve_with_kociemba(self):
        """Solve the cube using the Kociemba algorithm"""
        try:
            # Convert the cube state to Kociemba's format
            cube_string = self.to_kociemba_string()
            
            # Get the solution from Kociemba
            solution = kociemba.solve(cube_string)
            
            # Split the solution into individual moves
            moves = solution.split()
            
            return moves
        except Exception as e:
            print(f"Error solving with Kociemba: {e}")
            print(f"Cube string: {cube_string}")
            return []
    
    def apply_kociemba_move(self, move):
        """Apply a move from Kociemba's solution"""
        if move == "U":
            self.U()
        elif move == "U'":
            self.U_prime()
        elif move == "U2":
            self.U2()
        elif move == "D":
            self.D()
        elif move == "D'":
            self.D_prime()
        elif move == "D2":
            self.D2()
        elif move == "F":
            self.F()
        elif move == "F'":
            self.F_prime()
        elif move == "F2":
            self.F2()
        elif move == "B":
            self.B()
        elif move == "B'":
            self.B_prime()
        elif move == "B2":
            self.B2()
        elif move == "R":
            self.R()
        elif move == "R'":
            self.R_prime()
        elif move == "R2":
            self.R2()
        elif move == "L":
            self.L()
        elif move == "L'":
            self.L_prime()
        elif move == "L2":
            self.L2()


class RubiksCubeApp(Ursina):
    def __init__(self):
        super().__init__()
        
        # Set up the window
        window.title = "3D Rubik's Cube Solver"
        window.borderless = False
        window.fullscreen = False
        window.exit_button.visible = False
        window.fps_counter.enabled = True
        
        # Set up the camera
        camera.position = (0, 0, -10)
        camera.rotation_x = 20
        camera.rotation_y = -30
        
        # Create the cube
        self.cube = RubiksCube()
        
        # Create UI elements
        self.status_text = Text("Status: Ready", position=(-0.85, 0.45), scale=1.5)
        self.moves_text = Text("Moves: 0", position=(-0.85, 0.40), scale=1.5)
        self.solution_text = Text("Solution: ", position=(-0.85, 0.35), scale=1.5)
        
        # Create buttons
        self.scramble_button = Button("Scramble", position=(-0.85, 0.25), scale=(0.1, 0.05), color=color.azure)
        self.solve_button = Button("Solve", position=(-0.65, 0.25), scale=(0.1, 0.05), color=color.azure)
        self.reset_button = Button("Reset", position=(-0.45, 0.25), scale=(0.1, 0.05), color=color.azure)
        
        # Connect button events
        self.scramble_button.on_click = self.scramble_cube
        self.solve_button.on_click = self.solve_cube
        self.reset_button.on_click = self.reset_cube
        
        # Animation variables
        self.animating = False
        self.animation_queue = []
        self.current_animation = None
        self.animation_progress = 0
        self.animation_speed = 0.05
        
        # Mouse control variables
        self.mouse_down = False
        self.last_mouse_pos = (0, 0)
        
        # Instructions
        self.instructions = Text("Click and drag to rotate the cube", position=(-0.85, -0.45), scale=1.2, color=color.gray)
        
        # Title
        self.title = Text("3D Rubik's Cube Solver", position=(0, 0.47), scale=2, origin=(0, 0))
        
        # Enable mouse rotation
        self.mouse_sensitivity = 40
        
    def update(self):
        # Handle mouse rotation
        if mouse.left:
            if not self.mouse_down:
                self.mouse_down = True
                self.last_mouse_pos = mouse.position
            else:
                # Calculate mouse movement
                dx = mouse.position[0] - self.last_mouse_pos[0]
                dy = mouse.position[1] - self.last_mouse_pos[1]
                
                # Rotate the cube
                self.cube.cube_parent.rotation_y += dx * self.mouse_sensitivity * time.dt
                self.cube.cube_parent.rotation_x += dy * self.mouse_sensitivity * time.dt
                
                self.last_mouse_pos = mouse.position
        else:
            self.mouse_down = False
        
        # Update animation
        if self.animating and self.current_animation:
            self.animation_progress += self.animation_speed * time.dt
            
            if self.animation_progress >= 1.0:
                # Complete the animation
                self.apply_move(self.current_animation)
                self.current_animation = None
                self.animation_progress = 0
                
                # Start the next animation
                self.start_next_animation()
    
    def scramble_cube(self):
        """Scramble the cube and update the display"""
        if self.animating:
            return
        
        self.status_text.text = "Scrambling cube..."
        
        # Scramble the cube
        scramble_moves = self.cube.scramble(20)
        
        # Reset move count and solution moves
        self.cube.move_count = 0
        self.cube.solution_moves = []
        
        # Update the status
        self.status_text.text = f"Cube scrambled with {len(scramble_moves)} moves"
        self.moves_text.text = f"Moves: {self.cube.move_count}"
        self.solution_text.text = "Solution: "
    
    def solve_cube(self):
        """Solve the cube and animate the process"""
        if self.animating:
            return
        
        if self.cube.is_solved():
            self.status_text.text = "Cube is already solved!"
            return
        
        self.status_text.text = "Finding solution..."
        
        # Save the current state
        temp_cube = copy.deepcopy(self.cube)
        
        # Reset move count and solution moves
        self.cube.move_count = 0
        self.cube.solution_moves = []
        
        # Solve the cube using Kociemba
        solution_moves = self.cube.solve_with_kociemba()
        
        if not solution_moves:
            self.status_text.text = "Failed to find solution!"
            return
        
        # Restore the scrambled state
        self.cube = temp_cube
        
        # Set up the animation
        self.animation_queue = solution_moves.copy()
        self.cube.move_count = 0
        self.cube.solution_moves = []
        self.animating = True
        
        # Start the first animation
        self.start_next_animation()
    
    def start_next_animation(self):
        """Start the next animation in the queue"""
        if not self.animation_queue:
            self.animating = False
            self.status_text.text = f"Cube solved in {self.cube.move_count} moves!"
            return
        
        # Get the next move
        move = self.animation_queue.pop(0)
        self.current_animation = move
        self.animation_progress = 0
        
        # Add the move to the solution moves
        self.cube.solution_moves.append(move)
        self.cube.move_count += 1
        
        # Update UI
        self.moves_text.text = f"Moves: {self.cube.move_count}"
        
        # Update solution text
        solution_str = " ".join(self.cube.solution_moves[-10:])  # Show last 10 moves
        if len(self.cube.solution_moves) > 10:
            solution_str = "..." + solution_str
        self.solution_text.text = f"Solution: {solution_str}"
    
    def apply_move(self, move):
        """Apply a move to the cube"""
        self.cube.apply_kociemba_move(move)
    
    def reset_cube(self):
        """Reset the cube to its solved state"""
        if self.animating:
            return
        
        self.cube = RubiksCube()
        self.status_text.text = "Cube reset to solved state"
        self.moves_text.text = f"Moves: {self.cube.move_count}"
        self.solution_text.text = "Solution: "


# Main program
if __name__ == "__main__":
    app = RubiksCubeApp()
    app.run()