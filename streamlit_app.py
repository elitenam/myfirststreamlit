import streamlit as st

st.title("👋🏻 Streamlit 연습앱 만들기!!!!!")
st.subheader("이 페이지는 첫 실습 페이지입니다.")
st.write("안녕하세요. 중학교 과학교사입니다. 오늘 정신이 없습니다.")

st.link_button("남상훈의 깃허브 바로가기!", "https://github.com/elitenam")

# st.success("초록색 창")
# st.error("빨간색 창")
st.info("파란색 창")
# st.warning("노란색 창") # ctrl+/ : 주석처리
st.image("https://media.giphy.com/media/2A1hY6Zlzg52BLGX5M/giphy.gif?cid=790b7611kjvfdbq57fmj3u3td5egj9d1sl5w08xwot3acag0&ep=v1_gifs_search&rid=giphy.gif&ct=g", caption="Welcome to coding world") 
st.video("https://www.youtube.com/watch?v=bVuRW-n_h5g")