import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(page_title="سيد الألغاز العالمي | Assoumi", page_icon="🧩")

# تصميم احترافي متقدم
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #38bdf8; }
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

st.title("🌍 تحدي ألغاز العالم الذكي")

# قاعدة بيانات ضخمة للألغاز
if 'all_riddles' not in st.session_state:
    st.session_state.all_riddles = [
        {"q": "خريطة بلا مدن، جبال بلا أشجار، وبحار بلا سمك؟", "a": "الخريطة"},
        {"q": "ما هو الشيء الذي يكسر بمجرد نطق اسمه؟", "a": "الصمت"},
        {"q": "يمشي بلا أرجل ويدخل الأذن بلا استئذان؟", "a": "الصوت"},
        {"q": "شيء يوجد في وسط باريس؟", "a": "حرف الراء"},
        {"q": "ما هو الشيء الذي له أسنان ولا يعض؟", "a": "المشط"},
        {"q": "كلمة يبطل معناها إذا نطقنا بها؟", "a": "الصمت"},
        {"q": "سلم لا يصعد عليه أحد؟", "a": "سلم الرواتب"},
        {"q": "يسمع بلا أذن ويتكلم بلا لسان؟", "a": "الهاتف"},
        {"q": "له عين واحدة ولكنه لا يرى؟", "a": "الإبرة"},
        {"q": "يتحرك دائماً حولك لكنك لا تراه؟", "a": "الهواء"},
        {"q": "ما هو الشيء الذي يحوي مدناً بلا ناس؟", "a": "الخريطة"},
        {"q": "كلما زاد نقص، فما هو؟", "a": "العمر"},
        {"q": "ما هو الشيء الذي يكتب ولا يقرأ؟", "a": "القلم"},
        {"q": "ابن أمك وابن أبيك، وليس بأختك ولا بأخيك؟", "a": "أنت"},
        {"q": "ما هو الشيء الذي نبضه بلا قلب؟", "a": "الساعة"}
    ]

# تهيئة حالة اللعبة
if 'lives' not in st.session_state:
    st.session_state.lives = 3
    st.session_state.score = 0
    st.session_state.wrong_answers = [] # قائمة لتخزين الأخطاء
    st.session_state.current_riddle = random.choice(st.session_state.all_riddles)
    st.session_state.game_over = False

# شاشة الخسارة والمراجعة
if st.session_state.lives <= 0:
    st.error("💔 انتهت المحاولات! إليك الألغاز التي تعثرت فيها:")
    for item in st.session_state.wrong_answers:
        st.markdown(f"""
        <div class="review-card">
            <b>اللغز:</b> {item['q']}<br>
            <span style="color: #4ade80;"><b>الإجابة الصحيحة:</b> {item['a']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("🔄 حاول من جديد بنشاط"):
        st.session_state.lives = 3
        st.session_state.score = 0
        st.session_state.wrong_answers = []
        st.session_state.current_riddle = random.choice(st.session_state.all_riddles)
        st.rerun()

# شاشة اللعب
else:
    col1, col2 = st.columns(2)
    col1.metric("❤️ القلوب المتبقية", st.session_state.lives)
    col2.metric("🏆 رصيد الإجابات", st.session_state.score)

    st.markdown(f'<div class="riddle-box">{st.session_state.current_riddle["q"]}</div>', unsafe_allow_html=True)

    user_ans = st.text_input("اكتب إجابتك هنا وكن دقيقاً:")

    if st.button("تحقق ✅"):
        if user_ans.strip() == st.session_state.current_riddle["a"]:
            st.balloons()
            st.success("إجابة صحيحة! ننتقل للغز التالي...")
            st.session_state.score += 1
            st.session_state.current_riddle = random.choice(st.session_state.all_riddles)
            st.rerun()
        else:
            st.session_state.lives -= 1
            # حفظ اللغز في قائمة الأخطاء قبل الانتقال
            st.session_state.wrong_answers.append(st.session_state.current_riddle)
            if st.session_state.lives > 0:
                st.warning(f"خطأ! فقدت قلباً. تبقى لك {st.session_state.lives}")
                st.session_state.current_riddle = random.choice(st.session_state.all_riddles)
            st.rerun()
