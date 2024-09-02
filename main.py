import turtle
import random
import math
import time

def draw_firework_launch(turtle_obj, x, y, launch_height):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color("white")
    turtle_obj.goto(x, y + launch_height)
    return x, y + launch_height

def draw_fireworks(turtle_obj, x, y):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    
    colors = ["red", "yellow", "blue", "green", "purple", "orange", "white", "pink"]
    
    num_petals = 20  # Số lượng cánh hoa
    radius = random.randint(30, 70)  # Độ dài của các tia pháo hoa
    
    for _ in range(num_petals):
        angle = random.uniform(0, 360)  # Góc ngẫu nhiên
        distance = radius + random.uniform(-15, 15)  # Độ dài ngẫu nhiên của cánh hoa
        turtle_obj.color(random.choice(colors))
        turtle_obj.begin_fill()
        
        # Tính toán điểm đầu và điểm cuối của tia
        x_end = x + distance * math.cos(math.radians(angle))
        y_end = y + distance * math.sin(math.radians(angle))
        
        # Vẽ tia pháo hoa
        turtle_obj.goto(x_end, y_end)
        turtle_obj.end_fill()
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.pendown()

# Khởi tạo cửa sổ
screen = turtle.Screen()
screen.title("Quốc kỳ Việt Nam")
screen.bgcolor("black")  # Đặt nền thành màu đen

# Khởi tạo turtle để vẽ lá cờ
flag = turtle.Turtle()
flag.speed(3)  # Tăng tốc độ vẽ

# Vẽ nền cờ đỏ
flag.penup()
flag.goto(-150, 100)
flag.pendown()
flag.color("red")
flag.begin_fill()
for _ in range(2):
    flag.forward(300)
    flag.right(90)
    flag.forward(200)
    flag.right(90)
flag.end_fill()

# Vẽ ngôi sao vàng
flag.penup()
flag.goto(23, 30)  # Điều chỉnh vị trí ngôi sao
flag.pendown()
flag.color("yellow")
flag.begin_fill()

side_length = 60  # Điều chỉnh độ dài cạnh
angle = 144

for _ in range(5):
    flag.forward(side_length)
    flag.right(angle)
    flag.forward(side_length)
    flag.left(72)

flag.end_fill()

# Ẩn turtle sau khi vẽ xong lá cờ
flag.hideturtle()

# Tạo một turtle mới để viết chữ
text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.color("white")  # Đổi màu chữ thành trắng

# Dòng chữ cần hiển thị
message = "Chúc mừng Ngày Quốc khánh Việt Nam! Đảng Cộng sản Việt Nam quang vinh muôn năm!"

# Đặt vị trí của turtle ở giữa màn hình và xuống thấp hơn
text_turtle.goto(0, -200)  # Vị trí điều chỉnh

# Hiển thị dòng chữ từ từ
for i in range(len(message)):
    text_turtle.clear()
    text_turtle.write(message[:i+1], align="center", font=("Arial", 16, "bold"))
    screen.update()  # Cập nhật màn hình sau mỗi ký tự

text_turtle.write(message, align="center", font=("Arial", 16, "bold"))

# Khởi tạo hai turtle để vẽ pháo hoa
left_firework_turtle = turtle.Turtle()
right_firework_turtle = turtle.Turtle()
left_firework_turtle.speed(0)  # Tăng tốc độ vẽ pháo hoa
right_firework_turtle.speed(0)  # Tăng tốc độ vẽ pháo hoa
left_firework_turtle.hideturtle()
right_firework_turtle.hideturtle()

# Vẽ pháo hoa nổ liên tục ở hai bên của lá cờ
while True:
    left_firework_turtle.clear()  # Xóa các tia pháo hoa cũ bên trái
    right_firework_turtle.clear()  # Xóa các tia pháo hoa cũ bên phải
    
    # Bắn pháo hoa từ dưới lên
    left_x, left_y = draw_firework_launch(left_firework_turtle, -300, -200, random.randint(50, 150))
    right_x, right_y = draw_firework_launch(right_firework_turtle, 300, -200, random.randint(50, 150))
    
    # Tạo hiệu ứng nổ pháo hoa
    draw_fireworks(left_firework_turtle, left_x, left_y)  # Pháo hoa bên trái
    draw_fireworks(right_firework_turtle, right_x, right_y)  # Pháo hoa bên phải
    
    screen.update()
    time.sleep(0.5)  # Độ trễ giữa các lần nổ (0.5 giây)

# Kết thúc chương trình
turtle.done()
