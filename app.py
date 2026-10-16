import streamlit as st

st.markdown('<meta name="google-site-verification" content="5xFzHMM8a7fZgofBrBytFHbfKy---XeJFHb-CZv_Oto" />',unsafe_allow_html=True)
# アプリのタイトル
st.title("ドッカンダメージ計算ツール")

# サイドバーまたはメイン画面に入力フォームを作る
st.subheader("入力パラメータ")

x = st.number_input("敵の攻撃値（万）", value=1600, step=100)
y = st.number_input("味方のdefence値（万）", value=250, step=10)
r = st.number_input("defence倍率（%up）", value=2.0, step=0.1) # 例: 2%なら2.0
z = st.selectbox("全ガード", options=[(0, "なし(0)"), (1, "あり(1)")], format_func=lambda x: x[1])[0]
k = st.number_input("軽減率（%）", value=30, step=1)

# 計算ボタン
if st.button("計算する"):
    # rを%から小数倍率に変換（元のコードに合わせて調整）
    r_val = r * 0.01 
    
    if z == 1:
        a = (((1 - k * 0.01) * x) * 0.80 - y * (r_val * 0.01 + 1.0)) * 0.5
    else:
        a = ((1 - k * 0.01) * x) - y * (r_val * 0.01 + 1.0)
    
    st.divider()
    st.subheader("【結果】")
    if a > 0:
        st.error(f"被ダメージ（万）: {a:.2f}")
    else:
        st.success(f"完封！ ({a:.2f})")
