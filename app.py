import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(page_title="سيد الألغاز العالمي | Assoumi", page_icon="🧩")

# تصميم CSS احترافي (إضافة تنسيق الشعار)
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #38bdf8; }
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
        background: rgba(30, 41, 59, 0.5);
        padding: 15px;
        border-radius: 50px;
    }
    .logo-img {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        border: 3px solid #e94560;
    }
    .riddle-box { 
        background-color: #1e293b; padding: 25px; border-radius: 15px; 
        border-right: 5px solid #e94560; text-align: center; font-size: 22px;
        margin-bottom: 20px; color: white;
    }
    .review-card {
        background-color: #334155; padding: 15px; border-radius: 10px;
        margin-bottom: 10px; border: 1px solid #ef4444;
    }
    </style>
    """, unsafe_allow_html=True)

# --- قسم الشعار بالأعلى ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://dicebear.com" class="logo-img">
        <h1 style="color: white; margin: 0;">Assoumi Tech 🚀</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #38bdf8;'>🌍 تحدي ألغاز العالم الذكي</h3>", unsafe_allow_html=True)

# (بقية كود اللعبة الذي استخدمناه سابقاً يبدأ من هنا...)
if 'all_riddles' not in st.session_state:
    st.session_state.all_riddles = [
        {"q": "خريطة بلا مدن، جبال بلا أشجار، وبحار بلا سمك؟", "a": "الخريطة"},
        {"q": "ما هو الشيء الذي يكسر بمجرد نطق اسمه؟", "a": "الصمت"},
        {"q": "يمشي بلا أرجل ويدخل الأذن بلا استئذان؟", "a": "الصوت"},
        {"q": "شيء يوجد في وسط باريس؟", "a": "حرف الراء"},
        {"q": "له أسنان ولا يعض؟", "a": "المشط"},
        {"q": "له عين واحدة ولكنه لا يرى؟", "a": "الإبرة"},
        {"q": "يتحرك دائماً حولك لكنك لا تراه؟", "a": "الهواء"},
        {"q": "ما هو الشيء الذي يكتب ولا يقرأ؟", "a": "القلم"},
        {"q": "نبضه بلا قلب؟", "a": "الساعة"}
    ]

if 'lives' not in st.session_state:
    st.session_state.lives = 3
    st.session_state.score = 0
    st.session_state.wrong_answers = []
    st.session_state.current_riddle = random.choice(st.session_state.all_riddles)

# شاشة الخسارة والمراجعة
if st.session_state.lives <= 0:
    st.error("💔 انتهت المحاولات! راجع إجاباتك لتتعلم:")
    for item in st.session_state.wrong_answers:
        st.markdown(f'<div class="review-card"><b>اللغز:</b> {item["q"]}<br><span style="color: #4ade80;"><b>الإجابة:</b> {item["a"]}</span></div>', unsafe_allow_html=True)
    if st.button("🔄 العودة للعب"):
        st.session_state.lives = 3
        st.session_state.score = 0
        st.session_state.wrong_answers = []
        st.session_state.current_riddle = random.choice(st.session_state.all_riddles)
        st.rerun()

# شاشة اللعب
else:
    col1, col2 = st.columns(2)
    col1.metric("❤️ القلوب", st.session_state.lives)
    col2.metric("🏆 الرصيد", st.session_state.score)

    st.markdown(f'<div class="riddle-box">{st.session_state.current_riddle["q"]}</div>', unsafe_allow_html=True)
    user_ans = st.text_input("إجابتك هنا:")

    if st.button("تحقق ✅"):
        if user_ans.strip() == st.session_state.current_riddle["a"]:
            st.balloons()
            st.success("صحيح!")
            st.session_state.score += 1
            st.session_state.current_riddle = random.choice(st.session_state.all_riddles)
            st.rerun()
        else:
            st.session_state.lives -= 1
            st.session_state.wrong_answers.append(st.session_state.current_riddle)
            st.session_state.current_riddle = random.choice(st.session_state.all_riddles)
            st.rerun()
