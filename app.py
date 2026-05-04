import streamlit as st
import random

# إعدادات الواجهة
st.set_page_config(page_title="تحدي الذكاء | Assoumi", page_icon="🧠")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    .status-box { 
        padding: 20px; 
        border-radius: 10px; 
        border: 2px solid #00ffcc;
        text-align: center;
        font-size: 24px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 تحدي ذكاء المبرمج أسومي")
st.write("لقد اخترتُ رقماً سرياً بين **1 و 100**. هل ذكاؤك يكفي لمعرفته؟")

# تهيئة اللعبة
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

# مدخلات اللاعب
guess = st.number_input("أدخل تخمينك الآن:", min_value=1, max_value=100, step=1)

if st.button('تحقق من النتيجة 🚀'):
    st.session_state.attempts += 1
    
    if guess < st.session_state.secret_number:
        st.warning("📈 الرقم السري **أكبر** من ذلك! حاول مجدداً.")
    elif guess > st.session_state.secret_number:
        st.warning("📉 الرقم السري **أصغر** من ذلك! حاول مجدداً.")
    else:
        st.balloons()
        st.markdown(f"""
        <div class="status-box">
        🎊 مذهل! أنت عبقري! 🎊<br>
        لقد عرفت الرقم {st.session_state.secret_number}<br>
        في {st.session_state.attempts} محاولات فقط!
        </div>
        """, unsafe_allow_html=True)
        
        if st.button('لعب مرة أخرى 🔄'):
            del st.session_state.secret_number
            st.rerun()

# معلومات جانبية
st.sidebar.title("📊 إحصائيات اللعبة")
st.sidebar.write(f"عدد المحاولات الحالية: {st.session_state.attempts}")
st.sidebar.info("هذه اللعبة مبرمجة لتعمل بأقل استهلاك للذاكرة (تحسين لـ 2GB RAM)")

