import streamlit as st
import random

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="تحدي الأذكياء | Assoumi Dev", page_icon="🧩")

# تصميم CSS جذاب
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #38bdf8; }
    .word-box { 
        font-size: 40px; font-weight: bold; letter-spacing: 10px; 
        text-align: center; margin: 20px; color: #f1f5f9;
    }
    .status { text-align: center; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧩 تحدي ذكاء العباقرة")

# اختيار المستوى
level = st.sidebar.selectbox("اختر مستوى الصعوبة:", ["سهل (فواكه)", "متوسط (دول)", "صعب (برمجة)"])

# بيانات اللعبة
data = {
    "سهل (فواكه)": ["تفاح", "موز", "فراولة", "بطيخ", "برتقال"],
    "متوسط (دول)": ["الجزائر", "فلسطين", "تونس", "موريتانيا", "مصر"],
    "صعب (برمجة)": ["بايثون", "خوارزمية", "مصفوفة", "متغيرات", "دالة"]
}

# تهيئة اللعبة
if 'secret_word' not in st.session_state or st.sidebar.button("لعبة جديدة 🔄"):
    st.session_state.secret_word = random.choice(data[level])
    st.session_state.guessed_letters = []
    st.session_state.attempts = 6

# عرض الكلمة مشفرة
display_word = ""
for char in st.session_state.secret_word:
    if char in st.session_state.guessed_letters:
        display_word += char
    else:
        display_word += "_"

st.markdown(f'<div class="word-box">{display_word}</div>', unsafe_allow_html=True)

# إدخال الحروف
col1, col2 = st.columns([2, 1])
with col1:
    letter = st.text_input("خمن حرفاً واحداً:", max_chars=1).strip()
with col2:
    if st.button("تحقق ✅") and letter:
        if letter in st.session_state.guessed_letters:
            st.warning("لقد اخترت هذا الحرف من قبل!")
        elif letter in st.session_state.secret_word:
            st.session_state.guessed_letters.append(letter)
            st.success("أحسنت! حرف صحيح.")
        else:
            st.session_state.attempts -= 1
            st.error(f"خطأ! تبقى لك {st.session_state.attempts} محاولات.")

# التحقق من الفوز أو الخسارة
if "_" not in display_word:
    st.balloons()
    st.success(f"🎊 عبقري! الكلمة هي: {st.session_state.secret_word}")
    if st.button("العب مرة أخرى"):
        del st.session_state.secret_word
        st.rerun()

if st.session_state.attempts <= 0:
    st.error(f"💔 للأسف خسرنا! الكلمة كانت: {st.session_state.secret_word}")
    if st.button("حاول مجدداً"):
        del st.session_state.secret_word
        st.rerun()

st.sidebar.write(f"المحاولات المتبقية: {'❤️' * st.session_state.attempts}")
