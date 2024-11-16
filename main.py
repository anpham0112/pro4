import streamlit as st

with st.sidebar: #tạo thanh bên
##    Lấy ảnh và đưa ảnh lên trang web 
    image = "python4/python4_8.png"
    st.image(image,caption= "Đen Vâu")
    st.write("Họ và tên: Nguyễn Đức Cường")
    st.write("Nghệ danh: Đen Vâu")
    st.write("Nguyễn Đức Cường thường được biết đến với nghệ danh Đen Vâu hay Đen, là một nam rapper và nhạc sĩ người Việt Nam. Đen Vâu từng giành được giải cống hiến và là 'một trong số ít nghệ sĩ thành công từ làn  sóng underground và âm nhạc indie' của Việt Nam")
##tạo tiêu đề 
st.title ("Bài hát yêu thích")
##tên bài hát
st.write("Mưa trên những mái tôn")
##Lấy audio theo đường dẫn và đưa audio lên trang web
audio = open("python4/python4_8.mp3","rb")
st.audio(audio,format ='audio/mp3')
# tạo tiêu đề và tên mv
st.title ("MV yêu thích")
st.write("Đưa nhau đi trốn")
##lấy video theo đường dẫn, đưa video lên trang web
video = "https://www.youtube.com/watch?v=5e7e_KZINA4"
st.video(video,format ='video/mp4')
