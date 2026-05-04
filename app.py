import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Assoumi Tech 🚀", page_icon="💻", layout="wide")

# تصميم CSS احترافي (خلفية سوداء مع تأثيرات ضوئية)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(to right, #ff4b2b, #ff416c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
    }
    .welcome-card {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4b2b;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown('<h1 class="main-title">Assoumi Tech 🚀💻</h1>', unsafe_allow_html=True)

# تبويبات التنقل
tab1, tab2, tab3 = st.tabs(["🏠 الرئيسية", "🎮 مشاريعي", "📬 تواصل معي"])

with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="welcome-card">
        <h3>مرحباً بك في عالمي الرقمي 🇩🇿</h3>
        <p>أنا <b>أسومي</b>، مبرمج من الجزائر أتحدى المستحيل بـ 2 جيجا رام.</p>
        <p>هدفي هو تحويل الأفكار إلى واقع برمجي مذهل.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        # صورة رمزية (أفاتار مبرمج)
        st.image("https://dicebear.com", width=150)

with tab2:
    st.header("🛠️ مختبر الابتكار")
    st.write("هنا ستظهر ألعابي وتطبيقاتي التعليمية قريباً...")
    st.progress(40, text="جاري العمل على اللعبة الأولى 🎮")
    st.info("انتظروا لعبة بايثون القادمة قريباً على هذا الموقع!")

with tab3:
    st.header("🤝 لنتواصل")
    st.write("إذا كنت من فريق ASUS أو مهتماً بالتعاون، أنا بانتظارك:")
    st.link_button("زوروا قناتي على يوتيوب 🎥", "https://youtube.com")
    st.button("أرسل رسالة سريعة 📩")

st.markdown("---")
st.caption("صُنع بكل فخر بواسطة AssoumiDev 🇩🇿 | 2024")

