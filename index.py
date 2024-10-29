'''
streamlit多页面程序的入口文件
'''
import streamlit as st
st.title("AI大模型应用产品网")
col,col1 = st.columns(2)
#
with col:
    st.image("https://c.cidianwang.com/file/shufa/kaishu/zhaomengfu/2016110142041725.gif",use_column_width=True)
    flag = st.button("绘言",use_container_width=True)
    if flag:
        st.switch_page("pages/huiyan.py")
#
with col1:
    st.image("https://th.bing.com/th/id/R.79f953ec6e8506dd397d474e5a629687?rik=iPeNMYyganekWQ&riu=http%3a%2f%2fc.cidianwang.com%2ffile%2fshufa%2fkaishu%2ffae2e6a99479b04e.gif&ehk=IVuUixhvGmRj7o%2fMGE9%2bmItXoVplI9QkPttP3yNxhfQ%3d&risl=&pid=ImgRaw&r=0", use_column_width=True)
    flag = st.button("绘图",use_container_width=True)
    if flag:
        st.switch_page("pages/textToImage.py")
# c1,c2,c3,c4 = st.columns(4)
# with c1:
#     flag = st.button("基础版")
#     if flag:
#         st.switch_page("pages/demo.py")
# with c2:
#     flag1 = st.button("进阶版")
#     if flag1:
#         st.switch_page("pages/demo01.py")
# with c3:
#     flag2 = st.button("最终版")
#     if flag2:
#         st.switch_page("pages/huiyan.py")
# with c4:
#     flag3 = st.button("文生图")
#     if flag3:
#         st.switch_page("pages/textToImage.py")