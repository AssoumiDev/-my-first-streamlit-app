import streamlit as st

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Assoumi Tech | المبرمج أسومي", page_icon="🔥", layout="centered")

# إضافة لمسات CSS للمؤثرات البصرية
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #121212 100%);
        color: white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff4b2b, #ff416c);
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 30px;
        transition: 0.3s;
        font-weight: bold;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0px 0px 20px rgba(255, 75, 43, 0.5);
    }
    .title-text {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        background: -webkit-linear-gradient(#eee, #333);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeIn 3s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# واجهة الترحيب
st.markdown('<p class="title-text">Assoumi Tech 🚀</p>', unsafe_allow_html=True)

st.write("---")

# مراحل التعريف بالمشروع (Tabs)
tab1, tab2, tab3 = st.tabs(["🏠 الرئيسية", "🛠️ مشاريعي", "📧 تواصل معي"])

with tab1:
    st.header("مرحباً بك في عالمي الرقمي")
    st.info("أنا أسومي، مبرمج من الجزائر أتحدى المستحيل بـ 2 جيجا رام لصناعة المستقبل.")
    st.image("https://giphy.com", use_column_width=True)

with tab2:
    st.header("مختبر الابتكار")
    st.write("هنا ستظهر ألعابي وتطبيقاتي التعليمية قريباً...")
    st.progress(40, text="جاري العمل على اللعبة الأولى 🎮")

with tab3:
    st.header("لنصنع شيئاً عظيماً")
    st.write("إذا كنت من فريق ASUS أو مهتماً بالتعاون:")
    st.button("أرسل لي رسالة سريعة")

# تذييل الصفحة
st.markdown("<br><hr><center>صُنع بكل فخر بواسطة AssoumiDev 🇩🇿</center>", unsafe_allow_html=True)
