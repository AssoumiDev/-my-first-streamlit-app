import streamlit as st
import numpy as np
import time

# إعدادات الصفحة
st.set_page_config(page_title="Snake Game | Assoumi", page_icon="🐍")

st.title("🐍 لعبة الثعبان 2D")
st.write("استخدم الأزرار للتحكم في الثعبان. حاول ألا تصطدم بالجدران!")

# إعدادات اللعبة
width, height = 15, 15

if 'snake' not in st.session_state:
    st.session_state.snake = [[5, 5], [5, 4], [5, 3]]
    st.session_state.food = [10, 10]
    st.session_state.direction = "Right"
    st.session_state.score = 0

# أزرار التحكم
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⬆️"): st.session_state.direction = "Up"
with col1:
    if st.button("⬅️"): st.session_state.direction = "Left"
with col3:
    if st.button("➡️"): st.session_state.direction = "Right"
with col2:
    if st.button("⬇️"): st.session_state.direction = "Down"

# تحديث مكان الثعبان
head = st.session_state.snake[0].copy()
if st.session_state.direction == "Up": head[0] -= 1
elif st.session_state.direction == "Down": head[0] += 1
elif st.session_state.direction == "Left": head[1] -= 1
elif st.session_state.direction == "Right": head[1] += 1

# إضافة الرأس الجديد
st.session_state.snake.insert(0, head)

# التحقق من الأكل
if head == st.session_state.food:
    st.session_state.score += 1
    st.session_state.food = [np.random.randint(0, height), np.random.randint(0, width)]
else:
    st.session_state.snake.pop()

# رسم الملعب
grid = np.zeros((height, width))
for r, c in st.session_state.snake:
    if 0 <= r < height and 0 <= c < width:
        grid[r, c] = 1 # جسم الثعبان
grid[st.session_state.food[0], st.session_state.food[1]] = 2 # الأكل

# عرض اللعبة بالرموز التعبيرية (مناسب للرام 2 جيجا)
game_str = ""
for row in grid:
    for cell in row:
        if cell == 1: game_str += "🟩"
        elif cell == 2: game_str += "🍎"
        else: game_str += "⬛"
    game_str += "\n"

st.text(game_str)
st.write(f"🍎 النقاط: {st.session_state.score}")

if st.button("إعادة اللعب 🔄"):
    del st.session_state.snake
    st.rerun()

